# 🚀 QA Selenium Test Automation Framework

This project is a **modular and maintainable test automation framework** developed using **Selenium**, **PyTest**, and the **Page Object Model (POM)** design pattern. It includes basic login scenarios, reusable components, and setup-teardown logic managed through fixtures.

---

## 📁 Project Structure

QA_Framework_Project/
├── base_page.py # Base class with generic Selenium actions
├── login_page.py # Page object for login functionality
├── test_login_valid.py # Positive login test
├── test_login_invalid.py # Negative login test
├── conftest.py # Browser setup and teardown fixture
├── requirements.txt # Project dependencies
└── README.md # Project overview


---

## ✅ Features

- 🧱 **Page Object Model (POM)** structure
- 🔁 Valid & invalid login test cases
- 🔧 `conftest.py` for centralized fixture management
- ⚙️ `requirements.txt` for environment setup
- 🧪 Structured with **PyTest**
- 📸 Ready for integration with screenshot or logging tools (can be added later)

---

## 🧪 How to Run Tests

1. ✅ Install dependencies:

```bash
pip install -r requirements.txt


📦 Requirements
Python 3.8+

Selenium

PyTest

ChromeDriver (or any supported WebDriver)
