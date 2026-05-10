# Python Bootcamp

Hands-on repository for an 8-week Python bootcamp program organized in collaboration between TechIstanbul and Ecodation. Contains application files and sample code for the training program.

## Overview

This repository covers a broad spectrum of Python programming from fundamentals to advanced topics, featuring weekly lesson notes, example code, and practice questions.

## Repository Structure

### **`Week01/`**
- **Lesson01 - 2025.09.15**: Python introduction, print function, comments, basic data types
- **Lesson02 - 2025.09.17**: Variables, type conversion, user input
- **Lesson03 - 2025.09.20**: Conditional statements (if-else), logical operators
- **Examples**: `example01.py` to `example19.py`

### **`Week02/`**
- **Lesson04 - 2025.09.22**: Loops (for, while), list operations
- **Lesson05 - 2025.09.24**: Functions, parameters, return values
- **Lesson06 - 2025.09.27**: String methods, error handling
- **Examples**: `example00.py` to `example13.py`

### **`Week03/`**
- **Lesson07 - 2025.09.29**: File operations (read/write)
- **Lesson08 - 2025.10.01**: File operations continued
- **Lesson09 - 2025.10.04**: JSON and CSV formats
- **Sample data**: `file.txt`, `file2.txt`, `game.txt`, `shopping_list.txt`, `students.csv`, `students.json`

### **`Week04/`**
- **Lesson10 - 2025.10.06**: SQLite database fundamentals
- **Lesson11 - 2025.10.08**: SQL queries, SELECT/INSERT/UPDATE/DELETE
- **Lesson12 - 2025.10.11**: ORM (Object-Relational Mapping)
- **Databases**: `library.db`, `library_orm.db`, `links.db`, `school.db`

### **`Week05/`**
- **Lesson13 - 2025.10.13**: Web scraping, requests library
- **Lesson14 - 2025.10.15**: Data extraction with BeautifulSoup
- **Lesson15 - 2025.10.18**: Selenium automation
- **HTML samples**: `deneme.html`, `googlecom.html`

### **`Week06/`**
- Flask web framework examples (12 different examples)
- **Example01-08**: Basic routes, template rendering, form handling
- **Example09-12**: Database integration, CRUD operations
- **Templates**: `base.html`, `index.html`, `about.html`, `user.html`, `404.html`, `contact.html`
- **Static**: `style.css`

### **`Week07/`**
- **Section01**: Data visualization (matplotlib, seaborn)
- **Section02**: Pandas for data analysis
- **Section03**: Advanced data analysis techniques

### **`Week08/`**
- **Section01**: NumPy fundamentals, array operations
- **Section02**: Matplotlib plotting
- **Section03**: Advanced data visualization

### **`Practice/`**
- Weekly practice questions (Q1, Q4-Q11)
- Interactive Jupyter notebooks

## Prerequisites

- Python 3.10+ (recommended)
- Virtual environment tool (`venv` or `conda`)

## Quick Start

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\Activate.ps1   # Windows
   ```

2. Install required packages:
   ```bash
   pip install flask jupyter pandas matplotlib seaborn numpy requests beautifulsoup4
   ```

## Flask Demo (Week06/Example08)

```bash
cd Week06/Example08
python app.py
```

Open http://127.0.0.1:5000 in your browser.

**Routes:**
- `/` → `templates/index.html`
- `/about` → `templates/about.html`
- `/user/<username>` → `templates/user.html`
- `/contact` → GET/POST form handling
- `/main` → redirects to `/`

## License

This repository is for educational purposes. Attribution is appreciated when reusing code.
