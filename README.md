# 🛡️ Adaptive LLVM Code Obfuscation using Machine Learning

An intelligent LLVM-based software obfuscation framework that leverages **Machine Learning** to automatically select the most suitable obfuscation strategy based on program characteristics.

The framework operates on **LLVM Intermediate Representation (IR)** and combines compiler technology with **Machine Learning** to provide adaptive, secure, and efficient software protection against reverse engineering.

---

# 📑 Table of Contents

- [📌 Project Description](#-project-description)
- [✨ Project Highlights](#-project-highlights)
- [🏗️ Architecture / Workflow](#️-architecture--workflow)
- [🚀 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚡ Quick Start](#-quick-start)
- [📚 Documentation](#-documentation)
- [🔬 Research Paper](#-research-paper)
- [📘 Project Report](#-project-report)
- [🖼️ Screenshots](#️-screenshots)
- [🔮 Future Work](#-future-work)
- [👩‍💻 Author](#-author)
- [📄 License](#-license)

---

# 📌 Project Description

Adaptive LLVM Code Obfuscation using Machine Learning is an intelligent software protection framework developed to enhance the security of compiled applications against reverse engineering attacks.

The framework analyzes **LLVM Intermediate Representation (IR)**, extracts structural program features, predicts the most suitable obfuscation strategy using a **Random Forest classifier**, and applies compiler-level obfuscation techniques while preserving program functionality.

The project integrates compiler design, software security, and machine learning to provide an adaptive and research-oriented approach to code protection.

---

# ✨ Project Highlights

- 🛡 LLVM IR–based software protection
- 🤖 Machine Learning–driven obfuscation strategy selection
- 🌲 Random Forest classifier
- 🔀 Control Flow Flattening
- 🔄 Instruction Substitution
- 🔐 XOR-based String Encryption
- 📊 Obfuscation metrics generation
- 📈 Complexity and entropy analysis
- 🧩 Modular project architecture
- 🎓 Research-oriented implementation

---

# 🏗️ Architecture / Workflow

```text
                LLVM IR File (.ll)
                       │
                       ▼
                IR Parser Module
                       │
                       ▼
             Feature Extraction
                       │
                       ▼
          Random Forest Classifier
                       │
                       ▼
        Strategy Prediction Engine
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
 Control Flow   Instruction      String
 Flattening     Substitution     Encryption
        └──────────────┼──────────────┘
                       ▼
            Obfuscated LLVM IR
                       │
                       ▼
      Metrics & Visualization Report
```

### Workflow Overview

1. Parse LLVM IR.
2. Extract program features.
3. Predict the best obfuscation strategy.
4. Apply compiler-level obfuscation.
5. Generate evaluation metrics and reports.

---

# 🚀 Features

- LLVM IR Parsing
- Static Code Analysis
- Feature Extraction
- Machine Learning-Based Strategy Prediction
- Control Flow Flattening
- Instruction Substitution
- XOR-based String Encryption
- Obfuscation Metrics
- Visualization Reports
- Modular Architecture
- Command-Line Execution

---

# 📂 Repository Structure

```text
llvm-code-obfuscator/
│
├── docs/              # Documentation
├── ml/                # Machine Learning modules
├── obfuscation/       # Obfuscation techniques
├── paper/             # Research paper
├── parser/            # LLVM IR parser
├── report/            # Metrics and reporting
├── samples/           # Sample C and LLVM IR files
│
├── main.py
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚡ Quick Start

Clone the repository

```bash
git clone https://github.com/whysnavi/llvm-code-obfuscator.git
```

Navigate to the project

```bash
cd llvm-code-obfuscator
```

Run the framework

```bash
python main.py samples/hello.ll
```

> Detailed execution steps and sample commands will be added in the documentation.

---

# 📚 Documentation

Project documentation will be expanded in future updates.

- 📖 Execution Guide *(Coming Soon)*
- 📘 Project Report *(Coming Soon)*
- 📄 Research Paper
- 💻 Demo Commands
- 📊 Presentation

---

# 🔬 Research Paper

The complete research paper describing the adaptive LLVM obfuscation framework, methodology, implementation, and evaluation is included in the repository.

---

# 📘 Project Report

The detailed project report includes:

- Problem Statement
- Literature Survey
- System Design
- Methodology
- Implementation
- Results
- Future Scope

---

# 🖼️ Screenshots

Screenshots demonstrating the execution workflow, generated LLVM IR, obfuscation process, and output metrics will be added soon.

---

# 🔮 Future Work

- Support additional LLVM versions
- Deep Learning-based strategy prediction
- Reinforcement Learning for adaptive optimization
- GUI-based application
- Web dashboard
- Additional LLVM obfuscation passes
- Performance benchmarking
- Integration with LLVM optimization passes

---

# 👩‍💻 Author

**Vaishnavi Logishetty**

B.E. Artificial Intelligence & Data Science

Methodist College of Engineering & Technology

Hyderabad, Telangana, India

- GitHub: https://github.com/whysnavi
- LinkedIn: https://www.linkedin.com/in/vaishnavi-logishetty-501619336/

---

# 📄 License

This project is licensed under the **MIT License**.

---

⭐ If you find this project useful, consider giving it a **Star** on GitHub.
