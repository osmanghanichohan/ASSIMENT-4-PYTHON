# Ask the user to enter their age
age = int(input("Enter your age: "))

# Categorize the age
if age < 13:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teen"
elif 20 <= age <= 59:
    category = "Adult"
else:
    category = "Senior"

# Output the category
print(f"You are categorized as: {category}")
