# 🧠 Regex Pattern Finder & Validator

This Python project validates various types of text data using **Regular Expressions (regex)**. It reads lines from input files and checks each line for correctness based on regex patterns for:

- 💲 Currency amounts
- 📞 Phone numbers
- 🏷️ HTML tags
- 📧 Email addresses
- 🌐 URLs
-    Time

---

## 📦 Features

- Menu-driven command-line interface
- Validates text line-by-line from `.txt` files
- Built-in support for multiple formats (e.g., phone number formats)
- Clean output showing whether each line is valid or invalid

---

## 🛠️ Requirements

- Python 3.x  
(No external libraries required)

---

## 📁 File Structure
 - extract.py
 - currency.txt
 - emailaddress.txt
 - HTMltags.txt
 - phone.txt
 - urls.txt
 - time.txt
 - README.md 


---

## 🚀 How to Run

1. **Clone or download** this repository.
2. Make sure the `.txt` files contain the lines you want to validate.
3. Open a terminal and run:

```bash
python main.py
4. Choose an option from the menu to start validating.

📄 Sample Menu Output

		Welcome To The Regex Pattern Finder & Checker!

1. check Currency Amount From currency.txt
2. check Phone Number From phones.txt
3. check HTML Tag From htmltags.txt
4. check Email Address From emails.txt
5. check URL Address From urls.txt
6. Close The Program

Please select an option from the menu(1-6):


✅ Example File Content
emails.txt


user@example.com
firstname.lastname@company.co.uk
invalid@com


Line 1: 'user@example.com' ---- Valid
Line 2: 'firstname.lastname@company.co.uk' ---- Valid
Line 3: 'invalid@com' ---- Invalid


📌 Notes
Ensure the .txt files exist in the same directory as main.py.

Regex patterns are strict by design — malformed or incomplete entries will be marked invalid.

💻 Author
Made by ALU student Emeka Onugha

📜 License
This project is licensed under the MIT License.

---

Let me know if you'd like me to:
- Add badge icons (for Python version, license, etc.)
- Create a sample `LICENSE` file
- Write a script to generate all sample `.txt` files for testing

Ready to help with next steps like publishing to GitHub!
