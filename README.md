# Stamps Mini Test Submission

This repository contains my solutions for the mini test as part of the recruitment process for the Developer role at Stamps.

## 📌 Overview

There are two tasks included in this submission:

### 1. Small Program (Foo / Bar Logic)

A program that:

* Generates numbers from 1 to 100 in reverse order
* Skips prime numbers
* Replaces:

  * Multiples of 3 → `Foo`
  * Multiples of 5 → `Bar`
  * Multiples of both 3 and 5 → `FooBar`
* Outputs the result in a single horizontal line

### 2. Weather Forecast (OpenWeather API)

A program that:

* Fetches weather forecast data for Jakarta using OpenWeather API
* Displays the forecast for the next 5 days
* Shows only one temperature per day
* Uses simple filtering (prefers data at 12:00:00)

---

## ⚙️ Requirements

* Python 3.x
* Internet connection (for API request)

---

## 🔑 API Key

Before running the weather script, please set your API key:

```python
API_KEY = "5cdd4a52b1df0367a9a1ba57bc156392"
```

You can get a free API key from:
https://openweathermap.org/api

---

## ▶️ How to Run

### Run Test 1

```bash
py small_program.py
```

### Run Test 2

```bash
py weather_forecast.py
```

---

## 📊 Example Output

### Test 1

```
FooBar 98 Foo 96 Bar ...
```

### Test 2

```
Weather Forecast:
Thu, 02 Apr 2026: 30.05°C
Fri, 03 Apr 2026: 29.95°C
...
```

---

## 📝 Notes

* The solution is implemented using simple and readable Python code.
* The focus is on clarity and correctness rather than over-engineering.
* Weather data is filtered to ensure one temperature per day.

---

## 📷 Screenshots

Screenshots of the program outputs are included in the `screenshots/` folder.

---

Thank you for reviewing my submission.
