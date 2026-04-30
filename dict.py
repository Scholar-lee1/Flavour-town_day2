# Step 1: Create a dictionary
student_scores = {
    "Aisha": 85,
    "Bola": 90,
    "Emeka": 78,
    "Zainab": 92,
    "Joe": 10,
    "Yusuf": 100
}

# Step 2: Display all scores
print("Student score")
for name,score in student_scores.items():
    print(f"{name}:  {score}")

# Step 3: Check specific score
search_name = input("\nEnter a student's name to view score: ")
if search_name in student_scores:
    print(f"{search_name}'s score is {student_scores[search_name]}")
else:
    print(f"search_name not found in the record.")

# Step 4: Update or add a student's score
update_name = input("\nEnter student name to update/add: ")
new_score = int(input(f"\nEnter new score for {update_name}: "))
student_scores[update_name] = new_score
print(f"Record Updated: {update_name}: {student_scores[update_name]}")

# Step 5: Find highest scorer
highest_scorer = max(student_scores, key=student_scores.get)
print(f"\nHighest Scorer: {highest_scorer} with {student_scores[highest_scorer]} points")