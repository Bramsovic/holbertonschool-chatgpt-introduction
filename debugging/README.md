# Debugging Module

This directory contains code samples that illustrate debugging tasks as part of the **Holberton School - ChatGPT Introduction** project. Each file showcases specific debugging scenarios where AI is used to identify and resolve errors in various programming languages and environments.

## Files in this Directory

### 1. `factorial.py`
- **Objective**: Fix an infinite loop in the factorial calculation and ensure the program correctly computes the factorial of the input number.
- **Bug**: Incorrect loop logic.
- **Fix**: Added decrement to prevent infinite loop.

### 2. `print_arguments.py`
- **Objective**: Modify the script to print only the command-line arguments, excluding the script's name.
- **Bug**: The program includes the script name in the output.
- **Fix**: Adjusted loop to exclude the first element of `sys.argv`.

### 3. `change_background.html`
- **Objective**: Correct the button's functionality to dynamically change the background color.
- **Bug**: Incorrect ID in the JavaScript code.
- **Fix**: Updated ID to match the button's actual ID.

### 4. `mines.py`
- **Objective**: Add a win condition to the Minesweeper game.
- **Bug**: Missing logic to detect when all non-mine cells are revealed.
- **Fix**: Implemented win condition logic.

### 5. `factorial_recursive.py`
- **Objective**: Add proper comments and documentation to explain the recursive factorial function.
- **Enhancement**: Added function description, parameter explanation, and return value details.

### 6. `checkbook.py`
- **Objective**: Add error handling to prevent the program from crashing on invalid input.
- **Bug**: Crashes on non-numeric input during deposit/withdraw actions.
- **Fix**: Added try-except blocks for input validation.

### 7. `tic.py`
- **Objective**: Debug a Tic Tac Toe game and ensure it handles all user inputs correctly.
- **Bug**: Various issues with input handling and winner detection.
- **Fix**: Corrected logic and added validation for input.

## How to Use
1. Navigate to the `debugging` directory.
2. Review and run each script to observe how errors were fixed.
3. Test the solutions with various inputs to understand the debugging process.

## Learning Objectives
- Improve problem-solving and debugging skills.
- Leverage AI tools like ChatGPT for code review and debugging.
- Gain hands-on experience with real-world coding issues.

---
