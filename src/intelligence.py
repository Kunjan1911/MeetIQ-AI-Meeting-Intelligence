import re

def extract_action_items(transcript):

    sentences = re.split(r'(?<=[.!?])\s+', transcript)

    action_keywords = [
        "will",
        "should",
        "need to",
        "complete",
        "finish",
        "prepare",
        "start",
        "integrate",
        "develop",
        "finalize",
        "perform",
        "update",
        "push",
        "submit",
        "review",
        "test"
    ]

    action_items = []

    for sentence in sentences:

        if any(keyword in sentence.lower() for keyword in action_keywords):
            action_items.append(sentence)

    return action_items


def productivity_score(action_items):

    score = 50

    score += min(len(action_items) * 8, 40)

    return min(score,100)