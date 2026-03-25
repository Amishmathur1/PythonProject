Step 1: Preparing your Marksheet Data

To get your grades into the program, follow these exact steps:

    Login: Go to the SRM Student Portal.

    Navigate: Go to the Grade/Mark & Credit section.

    Copy Data: Highlight and copy all the entries (the table containing Semester, Course Code, Description, Credits, and Grade).

    Create Excel: Open Microsoft Excel and Paste the data.

    Format Check: Ensure your columns are in this order: Semester, Month / Year, Code, Description, Credit, Grade.

    Save File: * Go to File > Save As.

        Choose the folder where you saved the Python script.

        Set the "Save as type" to CSV (Comma delimited) (*.csv).

        Name the file marksheet.csv.

Step 2: Configuring the Python Script

If you saved the marksheet.csv file in the same folder as the Python script, the program will find it automatically.

If you saved it somewhere else, do the following:

    Locate your marksheet.csv file.

    Right-click the file and select Copy as path (on Windows) or Get Info (on Mac).

    Open the Python script and look for this line at the very bottom:
    record = AcademicRecord('marksheet.csv')

    Replace 'marksheet.csv' with your copied path (e.g., 'C:/Users/Name/Documents/marksheet.csv').
