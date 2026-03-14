from prompt_firewall import detect_prompt_injection

prompt = input("Enter prompt: ")

result, score = detect_prompt_injection(prompt)

print("Risk Score:", score)
print("Status:", result)
