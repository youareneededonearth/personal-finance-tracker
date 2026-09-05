# Personal Finance Tracker

A lightweight and robust console application written in Python to track personal income and expenses. This project was developed with a strong focus on software architecture, resource optimization, and strict user input validation.

---

## 🚀 Features (Функціонал)

* **Income & Expense Tracking:** Log transactions easily. The app automatically manages transaction signs (positive/negative) for a better user experience (UX).
* **Real-Time Balance:** View your current financial state instantly.
* **Formatted History:** View complete transaction history with clean, readable string formatting.
* **Crash Resilience:** The program is fully protected against invalid user input (e.g., entering text instead of numbers) using Python's built-in exception handling.

---

## 🛠️ Technical Details & Architecture (Технічні особливості та архітектура)

* **Language:** Python 3.x (Pure Python, zero external dependencies. Runs seamlessly on any computer).
* **DRY Principle (Don't Repeat Yourself):** Created a universal `get_safe_float` function that accepts a `prompt_text` argument. This single function dynamically handles unique text messages for both income and expenses securely.
* **Exception Handling (`try-except ValueError`):** Catches text-input errors in numeric fields, preventing the application from crashing.
* **Hardware Optimization:** The internal validation loop utilizes the blocking `input()` function. This safely pauses the thread while waiting for user interaction, reducing CPU usage to 0% during idle times.

---

## 💻 How to Run (Як запустити)

1. Ensure Python 3.x is installed on your machine.
2. Download the project file (e.g., `main.py`).
3. Open your terminal or IDE (like IDLE) and run:
   ```bash
   python main.py
   ```

====================================================================

# Консольний менеджер особистих фінансів (Українська версія)

Простий та надійний консольний додаток на Python для відстеження особистих доходів та витрат. Проєкт створено з фокусом на архітектуру коду, оптимізацію ресурсів та обробку помилок користувача.

## 🚀 Функціонал
* Додавання доходів та витрат (автоматичне керування знаком суми для зручності UX).
* Перегляд поточного балансу в реальному часі.
* Зберігання та вивід повної історії операцій із красивим форматуванням рядків.
* **Стійкість до збоїв:** Програма захищена від некоректного введення даних (тексту замість чисел) за допомогою механізму обробки винятків.

## 🛠️ Технічні особливості та архітектура
* **Мова:** Python 3.x (чистий код, без зовнішніх залежностей, працює на будь-якому ПК).
* **Валідація даних:** Створено універсальну функцію `get_safe_float` з параметром `prompt_text`. Вона реалізує принцип DRY (Don't Repeat Yourself) — одна функція безпечно обробляє різні текстові запити для доходів і витрат.
* **Обробка винятків (`try-except ValueError`):** Захищає програму від падіння у випадку введення літер у поля для сум.
* **Оптимізація для заліза:** Внутрішній цикл валідації використовує блокуючу функцію `input()`. Це дозволяє програмі "засинати" під час очікування дій користувача, що знижує навантаження на процесор (CPU) до 0%.
