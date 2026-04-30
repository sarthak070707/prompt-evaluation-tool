
import json

def get_response(prompt):
    prompt_lower = prompt.lower()

    if "api" in prompt_lower:
        return "APIs allow different software systems to communicate by sending requests and receiving structured responses."

    elif "json" in prompt_lower:
        return "JSON is a lightweight data format used to store and exchange data between systems in a structured way."

    elif "artificial intelligence" in prompt_lower or " ai " in f" {prompt_lower} ":
        return "AI works by training models on data to identify patterns and make predictions or decisions."

    elif "database" in prompt_lower:
        return "A database is an organized collection of data that can be stored, managed, and retrieved efficiently."

    elif "cloud" in prompt_lower:
        return "Cloud computing is the delivery of computing services like storage and processing over the internet instead of local systems."

    else:
        return f"This is a general response for: '{prompt}'. It provides basic information but may lack depth."


def evaluate_response(response):
    score = 0
    reasons = []

    response_lower = response.lower()

    # 1. Depth
    if len(response.split()) >= 12:
        score += 1
        reasons.append("Good length")
    else:
        reasons.append("Too short")

    # 2. Smarter clarity detection
    definition_patterns = [" is ", " are ", " allow ", " allows ", " refers to ", " works by "]
    if any(pattern in response_lower for pattern in definition_patterns):
        score += 1
        reasons.append("Clear explanation")
    else:
        reasons.append("Lacks clear explanation")

    # 3. Technical relevance
    keywords = ["data", "system", "model", "communication", "format", "requests", "collection", "internet"]
    if any(word in response_lower for word in keywords):
        score += 1
        reasons.append("Technically relevant")
    else:
        reasons.append("Low technical relevance")

    # 4. Strong penalty for vague responses
    vague_phrases = [
        "general response",
        "may lack depth",
        "basic response",
        "not detailed"
    ]

    if any(phrase in response_lower for phrase in vague_phrases):
        score -= 2
        reasons.append("Strong penalty for vague response")

    score = max(0, min(score, 3))

    return score, reasons


# Test prompts
prompts = [
    "Explain APIs in simple terms",
    "What is JSON?",
    "How does AI work?",
    "Explain databases",
    "What is cloud computing?",
    "Explain blockchain"
]

history = []

for prompt in prompts:
    response = get_response(prompt)
    score, reasons = evaluate_response(response)

    print("\nPrompt:", prompt)
    print("\nResponse:", response)
    print("Score:", score, "/3")
    print("Reasons:", ", ".join(reasons))
    print("-" * 50)

    history.append({
        "prompt": prompt,
        "response": response,
        "score": score,
        "reasons": reasons
    })


# Save results to JSON (important for project credibility)
with open("results.json", "w") as f:
    json.dump(history, f, indent=4)

print("\nResults saved to results.json")


# Summary
print("\n=== Summary ===")
for i, item in enumerate(history):
    print(f"{i+1}. {item['prompt'][:35]}... → Score: {item['score']}/3")