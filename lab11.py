import os
import matplotlib.pyplot as plt

# Global variables for storing data
student_names = []  
student_ids = []
assignment_names = []
assignment_ids = []
assignment_points = []
submission_student_ids = []
submission_assignment_ids = []
submission_scores = []

# Read the students file into lists
with open('data/students.txt', 'r') as file:
    for line in file:
        # Get just the ID (first 3 characters)
        id = line[0:3]
        # Get just the name (everything after ID)
        name = line[3:].strip()
        student_ids.append(id)
        student_names.append(name)

# Read the assignments file into lists
with open('data/assignments.txt', 'r') as file:
    lines = file.readlines()
    i = 0
    while i < len(lines):
        name = lines[i].strip()
        id = lines[i + 1].strip()
        points = int(lines[i + 2].strip())
        assignment_names.append(name)
        assignment_ids.append(id)
        assignment_points.append(points)
        i = i + 3

# Read all submission files
for filename in os.listdir('data/submissions'):
    with open(os.path.join('data/submissions', filename), 'r') as file:
        line = file.read().strip()
        parts = line.split('|')
        submission_student_ids.append(parts[0])
        submission_assignment_ids.append(parts[1])
        submission_scores.append(float(parts[2]))

# Main program
print("1. Student grade")
print("2. Assignment statistics")
print("3. Assignment graph")
choice = input("Enter your selection: ")

if choice == "1":
    name = input("What is the student's name: ")
    
    if name not in student_names:
        print("Student not found")
    else:
        # Get student's ID
        student_index = student_names.index(name)
        student_id = student_ids[student_index]
        
        # Calculate their total points
        total_points = 0
        earned_points = 0
        
        for i in range(len(submission_student_ids)):
            if submission_student_ids[i] == student_id:
                # Find which assignment this was
                assignment_index = assignment_ids.index(submission_assignment_ids[i])
                total_points += assignment_points[assignment_index]
                earned_points += (submission_scores[i] / 100) * assignment_points[assignment_index]
        
        # Calculate final grade
        grade = round((earned_points / total_points) * 100)
        print(f"{grade}%")

elif choice == "2":
    name = input("What is the assignment name: ")
    
    if name not in assignment_names:
        print("Assignment not found")
    else:
        # Get assignment ID
        assignment_index = assignment_names.index(name)
        assignment_id = assignment_ids[assignment_index]
        
        # Collect all scores for this assignment
        scores = [
            submission_scores[i] 
            for i in range(len(submission_assignment_ids)) 
            if submission_assignment_ids[i] == assignment_id
        ]
        
        # Calculate stats
        min_score = min(scores)
        max_score = max(scores)
        avg_score = sum(scores) / len(scores)
        
        print(f"Min: {min_score}%")
        print(f"Avg: {round(avg_score)}%")
        print(f"Max: {max_score}%")

elif choice == "3":
    name = input("What is the assignment name: ")
    
    if name not in assignment_names:
        print("Assignment not found")
    else:
        # Get assignment ID
        assignment_index = assignment_names.index(name)
        assignment_id = assignment_ids[assignment_index]
        
        # Collect all scores for this assignment
        scores = [
            submission_scores[i] 
            for i in range(len(submission_assignment_ids)) 
            if submission_assignment_ids[i] == assignment_id
        ]
        
        # Make the graph
        plt.hist(scores, bins=[0, 25, 50, 75, 100])
        plt.show()
