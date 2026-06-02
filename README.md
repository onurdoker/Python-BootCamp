# Python Bootcamp

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive 8-week Python bootcamp program covering programming fundamentals to advanced data science and web development. This repository contains hands-on examples, practice exercises, and project files.

## Overview

This bootcamp is designed for learners progressing from beginner to intermediate Python skills. Each week builds upon previous concepts, culminating in full-stack web applications and data analysis projects.

```
Total Duration: 8 Weeks
Target Audience: Beginners to Intermediate Learners
Prerequisites: Basic computer literacy
Total Examples: 218 Python files + 10 Jupyter Notebooks
```

## Curriculum Structure

| Week | Topic | Key Technologies | Lessons | Examples |
|------|-------|-----------------|---------|----------|
| **Week 01** | Python Fundamentals | Variables, Data Types, Conditionals | 3 | 59 |
| **Week 02** | Control Flow & Functions | Loops, Functions, Error Handling | 3 | 67 |
| **Week 03** | File Operations | File I/O, JSON, CSV Processing | 3 | 45 |
| **Week 04** | Database Management | SQLite, SQL Queries, ORM | 3 | 52 |
| **Week 05** | Web Scraping | Requests, BeautifulSoup, Selenium | 3 | 25 |
| **Week 06** | Web Development | Flask, Templates, Forms | 3 | 14 |
| **Week 07** | Data Analysis | Pandas, Matplotlib, Jupyter | 3 | 3 notebooks |
| **Week 08** | Scientific Computing | NumPy, Seaborn, Visualization | 3 | 4 notebooks |

## Repository Structure

```
Python-BootCamp/
├── Week01/          # Python Fundamentals (2025.09.15 - 2025.09.20)
│   ├── Lesson01 - 2025.09.15/  # Introduction, print(), comments
│   ├── Lesson02 - 2025.09.17/  # Variables, type conversion, input()
│   └── Lesson03 - 2025.09.20/  # Conditional statements
├── Week02/          # Control Flow & Functions (2025.09.22 - 2025.09.27)
│   ├── Lesson04 - 2025.09.22/  # Lists, loops
│   ├── Lesson05 - 2025.09.24/  # Functions, parameters
│   └── Lesson06 - 2025.09.27/  # Strings, exception handling
├── Week03/          # File Operations (2025.09.29 - 2025.10.04)
│   ├── Lesson07 - 2025.09.29/  # File I/O operations
│   ├── Lesson08 - 2025.10.01/  # File handling continued
│   └── Lesson09 - 2025.10.04/  # JSON and CSV processing
├── Week04/          # Database Management (2025.10.06 - 2025.10.11)
│   ├── Lesson10 - 2025.10.06/  # SQLite fundamentals
│   ├── Lesson11 - 2025.10.08/  # SQL queries (SELECT, INSERT, UPDATE, DELETE)
│   └── Lesson12 - 2025.10.11/  # Object-Relational Mapping (ORM)
├── Week05/          # Web Scraping (2025.10.13 - 2025.10.18)
│   ├── Lesson13 - 2025.10.13/  # HTTP requests, REST APIs
│   ├── Lesson14 - 2025.10.15/  # BeautifulSoup data extraction
│   └── Lesson15 - 2025.10.18/  # Selenium browser automation
├── Week06/          # Flask Web Development (2025.10.20 - 2025.10.25)
│   ├── Lesson16 - 2025.10.20/  # Flask routing, templates
│   ├── Lesson17 - 2025.10.22/  # Forms, POST/GET methods
│   └── Lesson18 - 2025.10.25/  # Database integration
├── Week07/          # Data Analysis (2025.10.27 - 2025.10.29)
│   ├── Lesson19 - 2025.10.27/  # Pandas data manipulation
│   ├── Lesson20 - 2025.10.29/  # Matplotlib visualizations
│   └── Lesson21 - 2025.11.01/  # Seaborn statistical plots
└── Week08/          # Scientific Computing (2025.11.03 - 2025.11.08)
    ├── Lesson22 - 2025.11.03/  # NumPy array operations
    ├── Lesson23 - 2025.11.05/  # Advanced data visualization
    └── Section24 - 2025.11.08/  # Comprehensive analysis project
└── Practice/        # Weekly practice questions & notebooks
    ├── Section05-Q1.py through Q11.py
    ├── Section06-Q1.py, Q4.py
    └── Section01-04.ipynb  # Interactive coding exercises
```

## Prerequisites

- Python 3.10 or higher
- Git (for cloning the repository)
- Virtual environment tool (`venv` or `conda`)

Recommended: Basic familiarity with command line operations

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ecodation/Python-BootCamp.git
   cd Python-BootCamp
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   # or
   .venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install flask jupyter pandas matplotlib seaborn numpy requests beautifulsoup4 selenium
   ```

## Quick Start

### Run Python Examples

```bash
# Run any example file
python Week01/Lesson01\ -\ 2025.09.15/example01.py
```

### Launch Jupyter Notebooks

```bash
jupyter notebook Practice/
# or
jupyter notebook Week07/Lesson19\ -\ 2025.10.27/lesson.ipynb
```

## Week-by-Week Content

### Week 01: Python Fundamentals
- Basic syntax and `print()` function
- Comments and code documentation
- Variables, data types, and type conversion
- User input handling
- Conditional statements and logical operators

### Week 02: Control Flow & Functions
- Lists, tuples, and dictionaries
- For and while loops
- Function definitions and parameters
- String methods and manipulation
- Exception handling with try/except

### Week 03: File Operations
- Reading and writing files
- File handling best practices
- JSON data processing
- CSV file operations

### Week 04: Database Management
- SQLite database operations
- SQL queries (SELECT, INSERT, UPDATE, DELETE)
- Object-Relational Mapping (ORM) concepts

### Week 05: Web Scraping
- HTTP requests and REST APIs
- BeautifulSoup HTML parsing
- Selenium browser automation

### Week 06: Flask Web Development
- Flask application setup
- Route decorators and URL parameters
- Template rendering
- Form handling (GET/POST)
- Database integration

### Week 07: Data Analysis
- Pandas DataFrame operations
- Matplotlib data visualization
- Seaborn statistical plots

### Week 08: Scientific Computing
- NumPy array operations
- Advanced visualization techniques
- Data analysis projects

## Practice Exercises

The `Practice/` directory contains:
- **Section 05**: Functions and string manipulation exercises (Q1-Q11)
- **Section 06**: Data structures and algorithms exercises (Q1, Q4)
- **Interactive notebooks**: Hands-on coding exercises with solutions (Section01-04)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install flask jupyter pandas matplotlib seaborn numpy requests beautifulsoup4 selenium` |
| Flask app not loading | Check virtual environment is activated |
| Jupyter kernel issues | Run `python -m ipykernel install --user --name=.venv` |

## Contributing

This is an educational repository. Feel free to:
- Submit pull requests for improvements
- Report issues with code examples
- Suggest additional practice problems

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

## Acknowledgments

- TechIstanbul for curriculum design
- Ecodation for training partnership
- All contributors and students who helped improve this material

---

<div align="center">

**Happy Coding! 🐍**

</div>
