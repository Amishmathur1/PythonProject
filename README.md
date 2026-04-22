# 📊 SRM Academic Marksheet Manager

This program helps you view your semester grades, calculate SGPA for a specific semester, and track your Cumulative CGPA (from Semester 1 up to your chosen semester).

---

## 🚀 How to Set Up (No Git Required)

Since you don't have Git installed, follow these steps to manually set up the project on your computer:

### 1. Create the Project Folder
* Create a new folder on your computer (e.g., Desktop or Documents) and name it `PythonProject`.

### 2. Copy the Python Code
* Click on the file named `Project.py` here on GitHub.
* Click the **"Raw"** button (top right of the code block).
* Press `Ctrl + A` (Select All) then `Ctrl + C` (Copy).
* Open **Notepad** or **VS Code** on your laptop, paste the code, and save it as `Project.py` inside your `PythonProject` folder.

### 3. Prepare your Marksheet (The CSV File)
The program needs your grades in a specific format to work.
1. **Login:** Go to the **SRM Student Portal**.
2. **Navigate:** Go to the **Grade/Mark & Credit** section.
3. **Copy Data:** Highlight and copy the entire table (Semester, Code, Description, Credit, Grade).
4. **Excel:** Open Excel and **Paste** the data.
5. **Format Check:** Ensure your columns are: `Semester`, `Month / Year`, `Code`, `Description`, `Credit`, `Grade`.
6. **Save:** Go to **File > Save As**. 
   * Select your `PythonProject` folder.
   * Change "Save as type" to **CSV (Comma delimited) (*.csv)**.
   * Name it exactly: `marksheet.csv`

---

## 🛠️ How to Run the Program

### If you have VS Code:
1. Open VS Code.
2. Go to **File > Open Folder** and select your `PythonProject` folder.
3. Open `Project.py` and click the **Play button** (top right).

### If you are using the Terminal/CMD:
1. Open Command Prompt or Terminal.
2. Type `cd` followed by the path to your folder (Example: `cd Desktop/PythonProject`).
3. Type `python Project.py` and press **Enter**.

---

## 📖 Features
- **Menu Driven:** Easy options to select Semesters 1-5.
- **Auto-Calculation:** Calculates SGPA and Cumulative CGPA instantly.
- **Summary View:** Option to view all semesters at once.

*Note: Make sure `Project.py` and `marksheet.csv` are always in the same folder!*

---

# ⚡ Electricity Bill Calculator

This program calculates your electricity bill based on slab rates provided in a CSV file (`ElecBill.csv`). It calculates the consumption by taking previous and current meter readings and provides a detailed cost breakdown.

## 🚀 How to Set Up

### 1. File Preparation
* Ensure both `Assignment2.py` and `ElecBill.csv` are in the same folder.

### 2. The Slab Data (`ElecBill.csv`)
The program reads rates from `ElecBill.csv`. The file should follow this structure:
- **From Unit**: Starting unit of the slab.
- **To Unit**: Ending unit of the slab (use "Above" for the final slab).
- **Rate (Rs.)**: The cost per unit for that range.

## 🛠️ How to Run
1. Open your terminal or VS Code in the project folder.
2. Run the command: `python Assignment2.py`
3. Enter the requested meter readings.

## 📖 Features
- **Slab-based Logic:** Handles complex multi-tier billing automatically.
- **Detailed Invoice:** Displays a formatted table with ranges, units consumed, rates, and costs.
- **Error Handling:** Prevents incorrect data entry (e.g., current reading lower than previous).

