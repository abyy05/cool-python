# cool-python
Hello Everyone ! Welcome to my python repository.


# Project 1 (String Reversal)

A simple Python program that takes a string input from the user and returns the reversed version of it using Python's slicing syntax.


## Features

- String manipulation
- User input
- Function definition and return values


## Installation

Run it as usual  .py file

```bash
  python string_reversal.py

```
    
## Example Usage

```bash
    Input:  enter a string: Hello World
    Output: dlroW olleH
```

## Tech Stack

**Python,** **Standard library only (no dependencies).** 


## Lessons Learned

- Clean function design
- User input validation
- Python String Slicing Techniques
- String Manipulation



# Project 2 (Temperature Conversion)

An interactive CLI (Command Line Interface) application to convert temperatures between Celsius and Fahrenheit.


## Features

- Convert from Fahrenheit to Celsius and vice versa
- Handles invalid input gracefully
- Runs up to 100 conversions in one session


## Installation

Run it as usual  .py file

```bash
  python Temperature_Conversion.py
```
    
## Example Usage

```bash
    Input:  Convert Temperature, units in large case
            Enter value: 44
            Enter unit (C for Celsius, F for Fahrenheit): C 
    Output: Your value in Fahrenheit is: 111.20 °F
```


## Tech Stack

**Python,** **Standard library only (no dependencies).** 


## Lessons Learned

- Basic control structures (if, while)
- CLI formatting for a better user experience



# Project 3 (Simple Calculator)

This Python script is a basic yet functional command-line calculator that performs: Addition, Subtraction, Multiplication, Division, Modulo.


## Features

- Easy-to-use menu-based interface

- Handles invalid inputs and division by zero

- Loop runs until the user chooses to exit

- Clean and readable Python logic


## Installation

Run it as usual  .py file

```bash
  python string_reversal.py
```


## Example Usage
A quick Snapshot of the complete code execution.

```bash
  1 - Addition
  2 - Subtraction
  3 - Multiplication
  4 - Division
  5 - Modulo
  6 - Exit
  Enter the option: 1
  Enter the value of a: 150
  Enter the value of b: 500
  Sum = 650.0
```


## Tech Stack

**Python,** **Standard library only (no dependencies).** 



## Lessons Learned

- Built logic using loops, conditionals, and functions.

- Practiced input validation and error handling.

- Created a user-friendly CLI menu.

- Improved code readability and structure.





# Project 3 (Palindrome Checker)

A simple Python CLI application that checks whether a word is a palindrome (reads the same backward as forward).


## Features

- Accepts user input
- Checks for alphabetic input only
- Determines if the input is a palindrome
- Runs continuously until manually stopped

## Installation

Run it as usual  .py file

```bash
  python string_reversal.py
```


## Example Usage

A quick Snapshot of the complete code execution.

```bash
  Enter a word: racecar
  racecar is a palindrome

  Enter a word: hello
  hello is not a palindrome

  Enter a word: 123abc
  Alphabets only

```


## Tech Stack

**Python,** **Standard library only (no dependencies).** 



## Lessons Learned

- String Slicing
- User Input Validation
- Basic Control Flow
- Input validation using .isalpha()
- Python string slicing
- Palindrome logic
- Use of infinite loops 






# Project 4 (File Organizer CLI Tool)

A simple Python CLI utility that **organizes files into folders by type and month** based on their creation date.

## Features

- Categorizes files into folders like `images`, `documents`, `code`, and `others`
- Groups files by **month of creation** (e.g., `2025-07`)
- Renames files with a **date-based unique format** to avoid duplication
- Automatically creates necessary folders
- Works recursively for all files in a given folder
- Logs all moved files with new names

## Installation

Run it as a regular `.py` file after replacing the `"your target file"` string with your target folder path.

```bash
  python file_organizer.py
```


## Example Usage

A quick snapshot of what happens when you run the code:

```bash
  Moved image1.jpg → images/2025-07/images_20250716_001.jpg
  Moved doc.txt → documents/2025-07/documents_20250716_001.txt
  Moved script.py → code/2025-07/code_20250716_001.py
  Moved random.xyz → others/2025-07/others_20250716_001.xyz
```

## Tech Stack

**Python**, **Standard Library Only**  
Modules used:
- `os`
- `shutil`
- `pathlib`
- `datetime`

## Lessons Learned

- File and folder manipulation with `pathlib` and `shutil`
- Categorizing by file extension
- Creating nested folders using `.mkdir(parents=True, exist_ok=True)`
- Timestamp formatting using `datetime`
- Unique file naming with counters
- Writing reusable utility functions











