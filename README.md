# Adaptive LLVM Code Obfuscation Using Machine Learning

A Python-based application that performs adaptive code obfuscation on LLVM Intermediate Representation (IR) using a Machine Learning framework. The system analyzes program characteristics, extracts software metrics, and automatically selects the most suitable obfuscation strategy using a Random Forest classifier.

## Features

- Automatic LLVM IR parsing
- Feature extraction from LLVM IR
- Random Forest–based obfuscation strategy selection
- Control Flow Flattening
- Instruction Substitution
- XOR-based String Encryption
- Obfuscation metrics generation
- Visual performance reports

## Tech Stack

- Python
- LLVM Intermediate Representation (IR)
- Scikit-learn
- NumPy
- Pandas
- Matplotlib

## Project Structure

```
llvm-code-obfuscator/
│
├── ml/
├── obfuscation/
├── parser/
├── report/
├── samples/
├── main.py
└── .gitignore
```

## How It Works

1. Parse the LLVM IR file.
2. Extract structural program features.
3. Predict the optimal obfuscation strategy using a Random Forest classifier.
4. Apply the selected obfuscation.
5. Generate metrics and performance reports.

## Running the Project

```bash
python main.py samples/hello.ll
```
## 🚀 Demo & Execution Guide

A step-by-step command reference is available for running and demonstrating the project.

### Included

- Project setup
- Running sample LLVM IR files
- Viewing generated metrics
- Inspecting obfuscated LLVM IR
- Running the project on new C programs

📄 **Demo Commands Cheat Sheet:**  
[demo_commands_cheatsheet.html](docs/demo_commands_cheatsheet.html)

**Adaptive LLVM-Based Code Obfuscation Using a Random Forest Selection Framework**

Published in the **International Journal for Research in Applied Science & Engineering Technology (IJRASET)**.

## Author

**Vaishnavi Logishetty**

Artificial Intelligence & Data Science  
Methodist College of Engineering and Technology
