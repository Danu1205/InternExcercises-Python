def password_strength(password):
    score = 0
    if len(password) > 8:
        score += 1
    if any(ch.isupper() for ch in password):
        score += 1
    if any(ch.isdigit() for ch in password):
        score += 1
    if any(ch in "!@#$%^&*()-_+=" for ch in password):
        score += 1
    if score <= 1:
        print("⭐Weak password")
    elif score <= 3:
        print("⭐⭐Medium password")
    else:
        print("⭐⭐⭐Strong password")
psd = input("Enter password: ")
password_strength(psd)
