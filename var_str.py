# Step 1: Get user input
full_name = input("Enter your full name: ")
birth_year = (input("Enter your year of birth"))

# Step 1: Get user input
name_lower = full_name.upper()
name_no_space = name_lower.replace(" ", "")
name_length = len(name_no_space)


# Step 3: String slicing
first3 = name_no_space[:3]         # First 3 letters
year_suffix = birth_year[-2:]      # last 2 digits of birth year

# Step 4: Create username with concatenation
username = first3 + year_suffix

# Step 5:Output with f-strings
print("\n===== USER INFO =====")
print(f"Original Name : {full_name}")
print(f"UserName      : {username}")
print(f"Name length   : {name_length} characters (excluding spaces)")
print("=" * 17)
