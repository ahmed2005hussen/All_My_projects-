# Simple Games Collection 🎮

This repository contains simple, beginner-friendly games implemented in Python and C++. These projects were developed to practice problem-solving and programming logic. The repository includes the following games:

---

## **1. Simple Substitution Cipher (C++)**
A substitution cipher program to encode or decode messages using a custom key.

### **Features**
- Encrypt a message using a substitution key.
- Decrypt a message back to its original form.
- Validates the key to ensure it's unique and adheres to constraints.

### **How to Use**
1. Run the program.
2. Choose:
   - **1**: Cipher a message.
   - **2**: Decipher a message.
   - **3**: Exit the program.
3. Enter the required input as prompted (sentence and a key of 5 unique letters).

![Cipher GIF](https://media.giphy.com/media/v1-YOUR_LINK_HERE)  
> Placeholder for GIF showing how the program runs.

---

## **2. Number Scrabble (Python)**
A fun two-player game where each player selects numbers from 1 to 9, trying to sum 15 using exactly three numbers.

### **Rules**
1. The game is played by **2 players**.
2. Players take turns picking a number from 1 to 9.
3. A number cannot be reused after selection.
4. A player wins by forming **exactly 15** using three selected numbers.
5. If no player achieves this and all numbers are used, the game ends in a **draw**.

### **How to Use**
1. Run the Python script.
2. Players take turns entering numbers from the displayed list.
3. The game announces the winner or ends in a draw.

![Number Scrabble GIF](https://media.giphy.com/media/v1-YOUR_LINK_HERE)  
> Placeholder for GIF showing gameplay.

---

## **How to Run the Games**

### **For the Cipher Program (C++):**
1. Ensure you have a C++ compiler installed (e.g., GCC, Visual Studio).
2. Compile the code:
   ```bash
   g++ -o cipher SimpleSubstitutionCipher.cpp
