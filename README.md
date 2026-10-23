# AI-Ready Code Quality Reviewer

A Python-based static analysis tool designed to mimic the core responsibilities of an AI Code Trainer. This script automates code reviews by scanning Python source files line by line, detecting anti-patterns, scope violations, and missing documentation.

## 🚀 Features
- **Documentation Verification:** Scans for function definitions (`def`) lacking immediate docstrings or comments.
- **Scope Analysis:** Detects unsafe or poor usage of the `global` keyword.
- **Line-by-Line Parsing:** Enumerates and tracks file data efficiently without relying on heavy external dependencies.

## 🛠️ Tech Stack
- **Python 3**
- **OS Module** (File system validation)
- **Built-in I/O Operations** (Text stream parsing)

## 📁 How to Run
1. Put the Python file you want to inspect in the same directory.
2. Open `reviewer.py` and set your target file name at the bottom:
   ```python
   analyze_file("your_code.py")
   ```
3. Execute the script via terminal:
   ```bash
   python reviewer.py
   ```
