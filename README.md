# Spell Counter 📝

A simple Python utility that analyzes a string of text to provide a detailed frequency count of every letter in the alphabet and the total word count.

## Features
* **Case-Insensitive Analysis**: Converts all input to lowercase so 'A' and 'a' are counted together.
* **Alphabetical Breakdown**: Iterates through the entire English alphabet (A-Z) and counts occurrences for each.
* **Word Count**: Calculates the total number of words in the provided text.
* **Clean Output**: Displays results in a numbered list for easy reading.

## How It Works
The script follows a straightforward logic:
1.  **Input**: It prompts the user to enter a string.
2.  **Normalization**: It converts the string to lowercase to ensure accuracy.
3.  **Iteration**: It loops through a predefined string of the alphabet.
4.  **Comparison**: For every letter in the alphabet, it scans the user's text and increments a counter whenever a match is found.
5.  **Reporting**: It prints the final count for each letter and the total word count.

## Usage
1. Ensure you have Python installed on your system.
2. Run the script:
   ```bash
   python Spell_Counter.py
