import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# Ensure the script is being run with the correct parameters
if len(sys.argv) != 3 or sys.argv[1] not in ['-s', '-c']:
    print("Error: Invalid input. Use -s <student_id> or -c <course_id>")
    exit()

# Read the CSV file
data = pd.read_csv("data.csv")

# Function to generate HTML for student details
def generate_student_html(student_id):
    student_data = data[data['Student id'] == student_id]
    if student_data.empty:
        return f"<h2>Error: No data found for Student ID {student_id}</h2>"
    
    total_marks = student_data[' Marks'].sum()
    html = "<h2>Student Details</h2><table border='1'><tr><th>Student id</th><th>Course id</th><th>Marks</th></tr>"
    
    for index, row in student_data.iterrows():
        html += f"<tr><td>{row['Student id']}</td><td>{row[' Course id']}</td><td>{row[' Marks']}</td></tr>"
    
    html += f"<tr><td colspan='2'>Total Marks</td><td>{total_marks}</td></tr></table>"
    return html

# Function to generate HTML for course details
def generate_course_html(course_id):
    course_data = data[data[' Course id'] == course_id]
    if course_data.empty:
        return f"<h2>Error: No data found for Course ID {course_id}</h2>"
    
    average_marks = course_data[' Marks'].mean()
    max_marks = course_data[' Marks'].max()
    
    # Create histogram
    plt.figure()
    plt.hist(course_data[' Marks'], bins=10, color='blue', alpha=0.7)
    plt.title(f'Marks Distribution for Course ID {course_id}')
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    
    # Save histogram as image
    histogram_path = "histogram.png"
    plt.savefig(histogram_path)
    plt.close()
    
    html = f"<h2>Course Details</h2><table border='1'><tr><th>Average Marks</th><th>Maximum Marks</th></tr>"
    html += f"<tr><td>{average_marks:.2f}</td><td>{max_marks}</td></tr></table>"
    html += f"<img src='histogram.png' alt='Histogram of Marks'>"
    
    return html

# Main logic based on command line argument
if sys.argv[1] == '-s':
    student_id = int(sys.argv[2])
    output_html = generate_student_html(student_id)
elif sys.argv[1] == '-c':
    course_id = int(sys.argv[2])
    output_html = generate_course_html(course_id)

# Write the output HTML file
with open("output.html", "w") as file:
    file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Output</title>\n</head>\n<body>\n")
    file.write(output_html)
    file.write("\n</body>\n</html>")
