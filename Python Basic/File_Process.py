import csv

# Function to calculate the average score for a student
def calculate_average(scores):
    return sum(scores) / len(scores)

# Read the CSV file and process the data
def process_student_scores(file_name):
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        summary_report = []

        # Process each student record
        for row in csv_reader:
            student_name = row['Name']
            scores = [int(row[field]) for field in row if field != 'Name']
            avg_score = calculate_average(scores)
            summary_report.append((student_name, avg_score))

        return summary_report

# Function to print the summary report
def print_summary_report(summary_report):
    print("Student Summary Report")
    print("----------------------")
    for student, avg in summary_report:
        print(f"{student}: {avg:.2f}")

# Example of how to use the functions
if __name__ == "__main__":
    file_name = r'e:\Django\student_scores.csv'
    summary_report = process_student_scores(file_name)
    print_summary_report(summary_report)
