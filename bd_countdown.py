def calculate_average(scores):
    return sum(scores) / len(scores)

def get_highest_and_lowest(scores):
    return max(scores), min(scores)

def analyze_performance(avg):
    if avg >= 70:
        return "Good performance"
    elif avg >= 50:
        return "Average performance"
    else:
        return "Poor prformance"

# Sample score
scores = [65, 70, 85, 50, 90, 45]

# Using the functions
average = calculate_average(scores)
highest, lowest = get_highest_and_lowest(scores)
performance = analyze_performance(average)

# Display results
print(f"Scores: {scores}")
print(f"Average Score: {average}")
print(f"Highest Score: {highest}")
print(f"lowest Score: {lowest}")
print(f"Performance Analysis: {performance}")