def classify_intent(user_input):
    if not user_input or user_input.strip() == "":
        return {
            "intent": None,
            "agent": None,
            "status": "REJECTED",
            "reason": "Empty input"
        }

    user_input = user_input.lower()

    intent_map = {
        "summarize": ["summarize", "summary", "brief"],
        "translate": ["translate", "in hindi", "in english"],
        "risk": ["risk", "danger", "evaluate risk"],
        "format": ["format", "structure", "arrange", "clean"]
    }

    detected = []

    for intent, keywords in intent_map.items():
        for word in keywords:
            if word in user_input:
                detected.append((intent, word))

    if len(detected) == 0:
        return {
            "intent": None,
            "agent": None,
            "status": "REJECTED",
            "reason": "No matching keyword found"
        }

    if len(detected) > 1:
        intents_found = list(set([i[0] for i in detected]))
        return {
            "intent": None,
            "agent": None,
            "status": "REJECTED",
            "reason": f"Conflicting intents detected: {intents_found}"
        }

    intent, keyword = detected[0]

    agent_map = {
        "summarize": "Text Summarizer",
        "translate": "Language Translator",
        "risk": "Risk Evaluator",
        "format": "Data Formatter"
    }

    return {
        "intent": intent,
        "agent": agent_map[intent],
        "status": "ROUTED",
        "reason": f"Keyword '{keyword}' detected"
    }