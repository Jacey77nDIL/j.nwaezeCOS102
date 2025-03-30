# Data for girls
girls_names = ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
girls_ages = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
girls_heights = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5]
girls_scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

# Data for boys
boys_names = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
boys_ages = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
boys_heights = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
boys_scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

# Combine data into a single list of dictionaries
students = []
for i in range(10):
    students.append({
        "Name": girls_names[i],
        "Age": girls_ages[i],
        "Height": girls_heights[i],
        "Score": girls_scores[i]
    })
    students.append({
        "Name": boys_names[i],
        "Age": boys_ages[i],
        "Height": boys_heights[i],
        "Score": boys_scores[i]
    })

# Print the table header
print("Name | Age | Height | Score")
print("-" * 30)

# Print the data in tabular format
for student in students:
    print(f"{student['Name']} | {student['Age']} | {student['Height']} | {student['Score']}")