import re

# simple patterns for prompt injection
malicious_patterns = [
    r"ignore previous instructions",
    r"reveal .*password",
    r"bypass security",
    r"act as .*dan",
    r"give admin access"
]

def detect_prompt_injection(prompt):
    risk_score = 0
    
    for pattern in malicious_patterns:
        if re.search(pattern, prompt.lower()):
            risk_score += 30

    if risk_score >= 50:
        return "BLOCKED", risk_score
    else:
        return "SAFE", risk_score


prompt = input("Enter prompt: ")

result, score = detect_prompt_injection(prompt)

print("Risk Score:", score)
print("Result:", result)
