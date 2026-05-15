# Python Bootcamp

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: Educational](https://img.shields.io/badge/License-Educational-yellow.svg)](https://opensource.org/licenses/Educational)

A comprehensive 8-week Python bootcamp program covering programming fundamentals to advanced data science and web development. This repository contains hands-on examples, practice exercises, and project files.

## Overview

This bootcamp is designed for learners progressing from beginner to intermediate Python skills. Each week builds upon previous concepts, culminating in full-stack web applications and data analysis projects.

```
Total Duration: 8 Weeks
Target Audience: Beginners to Intermediate Learners
Prerequisites: Basic computer literacy
```

## Curriculum Structure

| Week | Topic | Key Technologies |
|------|-------|-----------------|
| **Week 01** | Python Fundamentals | Variables, Data Types, Conditionals |
| **Week 02** | Control Flow & Functions | Loops, Functions, Error Handling |
| **Week 03** | File Operations | File I/O, JSON, CSV Processing |
| **Week 04** | Database Management | SQLite, SQL Queries, ORM |
| **Week 05** | Web Scraping | Requests, BeautifulSoup, Selenium |
| **Week 06** | Web Development | Flask, Templates, Forms |
| **Week 07** | Data Analysis | Pandas, Matplotlib, Seaborn |
| **Week 08** | Scientific Computing | NumPy, Advanced Visualization |

## Repository Structure

```
Python-BootCamp/
├── Week01/          # Fundamentals (3 lessons)
├── Week02/          # Control structures (3 lessons)
├── Week03/          # File operations & data formats
├── Week04/          # SQLite databases
├── Week05/          # Web scraping techniques
├── Week06/          # Flask web applications (12 examples)
├── Week07/          # Data visualization & analysis
├── Week08/          # NumPy & scientific computing
└── Practice/        # Weekly practice questions & notebooks
```

### Week 01: Python Fundamentals
- **Lesson 01** (2025-09-15): Introduction, `print()` function, comments, basic data types
- **Lesson 02** (2025-09-17): Variables, type conversion, user input
- **Lesson 03** (2025-09-20): Conditional statements, logical operators

### Week 02: Control Flow & Functions
- **Lesson 04** (2025-09-22): `for`/`while` loops, list operations
- **Lesson 05** (2025-09-24): Function definitions, parameters, return values
- **Lesson 06** (2025-09-27): String methods, exception handling

### Week 03: File Operations
- **Lesson 07** (2025-09-29): File I/O operations
- **Lesson 08** (2025-10-01): File handling continued
- **Lesson 09** (2025-10-04): JSON and CSV data processing

### Week 04: Database Management
- **Lesson 10** (2025-10-06): SQLite fundamentals
- **Lesson 11** (2025-10-08): SQL queries (SELECT, INSERT, UPDATE, DELETE)
- **Lesson 12** (2025-10-11): Object-Relational Mapping (ORM)

### Week 05: Web Scraping
- **Lesson 13** (2025-10-13): HTTP requests library
- **Lesson 14** (2025-10-15): BeautifulSoup data extraction
- **Lesson 15** (2025-10-18): Selenium browser automation

### Week 06: Flask Web Development
12 progressive examples covering:
- Basic routing and template rendering
- URL parameters and dynamic pages
- Form handling (GET/POST)
- Error handling and redirects
- Database integration with SQLite

### Week 07: Data Analysis & Visualization
- Matplotlib visualizations
- Pandas data manipulation
- Seaborn statistical plots

### Week 08: Scientific Computing
- NumPy array operations
- Advanced data visualization techniques

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

### Run Flask Examples (Week 06)

```bash
cd Week06/Example08
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

**Available Routes:**
- `/` - Home page
- `/about` - About page
- `/user/<name>` - Dynamic user page
- `/contact` - Contact form (GET/POST)
- `/main` - Redirect example

### Launch Jupyter Notebooks

```bash
jupyter notebook Practice/
# or
jupyter notebook Week07/Section01/lesson01.ipynb
```

## Practice Exercises

The `Practice/` directory contains:
- **Section 05**: Functions and string manipulation (Q1-Q11)
- **Section 06**: Data structures and algorithms (Q1, Q4)
- **Interactive notebooks**: Hands-on coding exercises with solutions

## Learning Path Recommendations

1. **Beginners**: Follow weeks sequentially, complete all exercises
2. **Intermediate**: Focus on Weeks 04-08 for data science and web development
3. **Developers**: Jump to Week 06 for Flask applications, Week 07-08 for data analysis

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| Flask app not loading | Check virtual environment is activated |
| Jupyter kernel issues | Run `python -m ipykernel install --user --name=.venv` |

## Contributing

This is an educational repository. Feel free to:
- Submit pull requests for improvements
- Report issues with code examples
- Suggest additional practice problems

## License

This project is for **educational purposes only**. Attribution is appreciated when reusing code or materials.

## Acknowledgments

- TechIstanbul for curriculum design
- Ecodation for training partnership
- All contributors and students who helped improve this material

---

<div align="center">

**Happy Coding! 🐍**

</div>