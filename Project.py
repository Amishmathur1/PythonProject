import csv

class MarksheetData:
    def __init__(self, filename):
        self.filename = filename
        self.all_rows = []
        self.load_csv()

    def load_csv(self):
        """Reads the CSV file and stores rows in a list."""
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.all_rows.append(row)
        except FileNotFoundError:
            print("Error: File not found.")

class AcademicRecord(MarksheetData):
    def __init__(self, filename):
        super().__init__(filename)
        # Grade to Point mapping
        self.grade_points = {
            'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 
            'B': 6, 'C': 5, 'P': 4, 'F': 0
        }

    def get_subjects_by_semester(self, sem_num):
        """Filters rows for a specific semester."""
        subjects = []
        for row in self.all_rows:
            if row['Semester'] == str(sem_num):
                subjects.append(row)
        return subjects

    def calculate_metrics(self, target_sem):
        """Calculates SGPA and CGPA using standard if-else blocks."""
        
        current_sem_subjects = self.get_subjects_by_semester(target_sem)
        curr_total_credits = 0
        curr_weighted_points = 0

        for sub in current_sem_subjects:
            credit = float(sub['Credit'])
            grade = sub['Grade']
            points = self.grade_points.get(grade, 0)
            curr_total_credits += credit
            curr_weighted_points += (credit * points)

        if curr_total_credits > 0:
            sgpa = curr_weighted_points / curr_total_credits
            sgpa = round(sgpa, 3)
        else:
            sgpa = 0
            
        cum_total_credits = 0
        cum_weighted_points = 0

        current_range = range(1, target_sem + 1)
        for s in current_range:
            sem_subjects = self.get_subjects_by_semester(s)
            for sub in sem_subjects:
                credit = float(sub['Credit'])
                grade = sub['Grade']
                points = self.grade_points.get(grade, 0)
                cum_total_credits += credit
                cum_weighted_points += (credit * points)

        if cum_total_credits > 0:
            cgpa = cum_weighted_points / cum_total_credits
            cgpa = round(cgpa, 3)
        else:
            cgpa = 0
        
        return sgpa, cgpa

    def display_sem_report(self, sem_num):
        """Prints the report for a specific semester."""
        subjects = self.get_subjects_by_semester(sem_num)
        
        if len(subjects) == 0:
            print("\nNo data found for Semester", sem_num)
        else:
            print("\n" + "="*20 + " SEMESTER " + str(sem_num) + " REPORT " + "="*20)
            print("Code       | Description                                   | Cr  | Grade")
            print("-" * 75)
            
            for sub in subjects:
                code = sub['Code']
                desc = sub['Description']
                credit = sub['Credit']
                grade = sub['Grade']
                print(code.ljust(10), "|", desc.ljust(45)[:45], "|", credit.ljust(3), "|", grade)
            
            sgpa, cgpa = self.calculate_metrics(sem_num)
            print("-" * 75)
            print("RESULT: SGPA:", sgpa, "| Cumulative CGPA (Sem 1-" + str(sem_num) + "):", cgpa)
            print("-" * 75)

def run_menu():
    record = AcademicRecord('/home/amish/Documents/Coding Stuff/Python/marksheet.csv')
    
    while True:
        print("\n--- ACADEMIC MANAGER ---")
        print("1. View Semester 1")
        print("2. View Semester 2")
        print("3. View Semester 3")
        print("4. View Semester 4")
        print("5. View Semester 5")
        print("6. View All Semesters")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            record.display_sem_report(1)
        elif choice == '2':
            record.display_sem_report(2)
        elif choice == '3':
            record.display_sem_report(3)
        elif choice == '4':
            record.display_sem_report(4)
        elif choice == '5':
            record.display_sem_report(5)
        elif choice == '6':
            all_sems = [1, 2, 3, 4, 5]
            for s in all_sems:
                record.display_sem_report(s)
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    run_menu()
