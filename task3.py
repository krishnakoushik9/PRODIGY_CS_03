import re

while True:
    password = input("Enter a password to check (or 'q' to quit): ")
    if password.lower() == 'q':
        break

    score = 0
    feedback = []
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    elif len(password) >= 12:
        score += 2
        feedback.append("Good length!")
    else:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters for stronger password.")


    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters for stronger password.")


    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers for stronger password.")


    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters for stronger password.")


    if score < 2:
        strength = "Very Weak"
    elif score < 3:
        strength = "Weak"
    elif score < 4:
        strength = "Moderate"
    elif score < 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Great password! No additional feedback.")
    print()
