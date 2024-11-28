# Password Checker Application

This Python script is a **Password Checker Application** that evaluates the strength of a password entered by the user. It ensures that the password meets essential security criteria and provides feedback to the user if the password is not strong.

## Features
- Checks if a password is at least **8 characters long**.
- Validates that the password contains at least one:
  - **Lowercase letter**.
  - **Uppercase letter**.
  - **Number**.
  - **Special symbol** (e.g., `!@#$%^&*()`).
- Provides detailed feedback on missing elements if the password is weak.
- User-friendly console-based interface.

## How It Works
1. The script repeatedly prompts the user to enter a password.
2. The password is evaluated against the following conditions:
   - Minimum length of 8 characters.
   - Inclusion of:
     - At least one lowercase letter.
     - At least one uppercase letter.
     - At least one numeric digit.
     - At least one special character.
3. If all conditions are satisfied, the password is considered **strong**, and the program exits.
4. If the password is weak, the program informs the user of the missing elements and prompts them to try again.

## Requirements
- Python 3.x
- `string` library (built-in)

## How to Run
1. Clone the repository or download the script file.
2. Open a terminal or command prompt in the script's directory.
3. Run the script using:
   ```bash
   python password_checker.py
