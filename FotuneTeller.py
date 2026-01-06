import random
name = input("Enter your name: ")
print("Hello", name)
fortunes = {
    "Health": [
        "You will feel energetic",
        "Take care of your health."

    ],
    "Career": [
        "Success is coming.Work hard and stay focused."
    ],
    "Love": [
        "Love is around you.You will get Married This year",
    ],
    "Finance": [
        "Money matters will improve."
                ]
}
category = random.choice(list(fortunes.keys()))
prediction = random.choice(fortunes[category])
print("\nCategory:", category)
print("Prediction:", prediction)
file = open("fortune.txt", "a")
file.write(name + " - " + category + " - " + prediction + "\n")
file.close()
