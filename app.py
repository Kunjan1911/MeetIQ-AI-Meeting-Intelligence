from src.visualization import generate_wordcloud
from src.visualization import keyword_frequency
from src.pdf_generator import create_pdf
import matplotlib.pyplot as plt
from src.summarizer import generate_summary
from src.analytics import analyze_sentiment
from src.intelligence import extract_action_items
from src.intelligence import productivity_score
from src.summarizer import generate_summary
from src.transcription import transcribe_audio
import streamlit as st
st.set_page_config(
    page_title="MeetSense AI",
    page_icon="🎤",
    layout="wide"
)
st.markdown("""
<style>

.main-title{
    font-size:42px;
    font-weight:bold;
    color:#1E88E5;
}

.sub-title{
    font-size:20px;
    color:gray;
}

.metric-card{
    background-color:#F5F7FA;
    padding:18px;
    border-radius:15px;
    text-align:center;
    box-shadow:2px 2px 8px rgba(0,0,0,0.15);
}

</style>
""", unsafe_allow_html=True)
st.markdown(
    '<p class="main-title">🎤 MeetSense AI</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">AI Powered Meeting Intelligence Platform</p>',
    unsafe_allow_html=True
)

st.divider()
st.sidebar.title("MeetSense AI")

st.sidebar.info(
"""
Upload a meeting recording and automatically generate

• Transcript

• Executive Summary

• Action Items

• Sentiment Analysis

• Productivity Score

• Analytics
"""
)
uploaded_file = st.file_uploader(
    "📂 Upload Meeting Audio",
    type=["mp3", "wav", "m4a", "mp4"]

)
transcript=""
summary=""
sentiment=""
action_items=[]
score=0
if uploaded_file is not None:

    st.success("✅ Audio uploaded successfully!")

    with st.spinner("🎤 Transcribing Audio..."):

        transcript = transcribe_audio(uploaded_file)

    with st.spinner("📝 Generating Summary..."):

        summary = generate_summary(transcript)

    with st.spinner("😊 Analyzing Sentiment..."):

        sentiment = analyze_sentiment(transcript)

    action_items = extract_action_items(transcript)

    score = productivity_score(action_items)

    st.success("✅ AI Analysis Completed")
st.subheader("📊 Meeting Overview")

col1,col2,col3,col4=st.columns(4)

with col1:

    if sentiment:
        st.metric(
            "😊 Sentiment",
            sentiment["label"]
        )
    else:
        st.metric("😊 Sentiment","-")

with col2:

    st.metric(
        "📌 Action Items",
        len(action_items)
    )

with col3:

    st.metric(
        "📊 Productivity",
        f"{score}/100"
    )

with col4:

    if transcript:
        st.metric(
            "📝 Words",
            len(transcript.split())
        )
    else:
        st.metric("📝 Words",0)
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🏠 Dashboard",
        "📄 Transcript",
        "📋 AI Report",
        "📊 Analytics"
    ]
)
with tab1:

    st.header("📊 Meeting Dashboard")

    if transcript:

        st.success("Meeting processed successfully.")

        st.write("### AI Insights")

        st.write("😊 **Sentiment:**", sentiment["label"])

        st.write("📊 **Productivity Score:**", score)

        st.write("📌 **Action Items:**", len(action_items))

        st.write("📝 **Total Words:**", len(transcript.split()))

    else:

        st.info("Upload an audio file to generate AI-powered meeting insights.")
with tab2:

    st.header("📄 Meeting Transcript")

    if transcript:

        st.text_area(
            "Transcript",
            transcript,
            height=350
        )

    else:

        st.info("Please upload an audio file.")
with tab3:

    st.header("📝 Executive Summary")

    if summary:

        st.write(summary)

        st.divider()

        st.subheader("📌 Action Items")

        if len(action_items) == 0:

            st.info("No Action Items Found")

        else:

            for item in action_items:

                st.write("✅", item)


        st.divider()

        st.subheader("📄 Download Meeting Report")

        pdf = create_pdf(
            summary,
            sentiment,
            action_items,
            score
        )

        with open(pdf, "rb") as f:

            st.download_button(
                "📥 Download AI Report",
                data=f,
                file_name="Meeting_Report.pdf",
                mime="application/pdf"
            )


    else:

        st.info("Upload audio first.")
with tab4:

    st.header("📊 Meeting Analytics")

    if transcript:

        st.subheader("Meeting Statistics")

        col1,col2=st.columns(2)

        with col1:
            st.metric("Total Words",len(transcript.split()))

        with col2:
            st.metric("Characters",len(transcript))

        st.divider()

        st.subheader("Top Keywords")

        keywords=keyword_frequency(transcript)

        for word,count in keywords:

            st.write(f"**{word}** : {count}")

        st.divider()

        st.subheader("Word Cloud")

        fig=generate_wordcloud(transcript)

        st.pyplot(fig)

    else:

        st.info("Upload audio first.")