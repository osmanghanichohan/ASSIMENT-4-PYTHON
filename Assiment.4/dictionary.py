# 1. Create an initial dictionary
my_dict = {"name": "Alice", "age": 25}
print("Original dictionary:", my_dict)

# 2. Use update() to add a new key-value pair or update an existing one
my_dict.update({"city": "New York"})
my_dict.update({"age": 26})  # updates the 'age'
print("After update:", my_dict)

# 3. Use pop() to remove a key and get its value
removed_value = my_dict.pop("city")
print("After pop:", my_dict)
print("Removed value:", removed_value)

# 4. Use values() to view all values in the dictionary
all_values = my_dict.values()
print("All current values:", list(all_values))

# 5. Update a value directly
my_dict["name"] = "Alicia"
print("After changing 'name':", my_dict)
