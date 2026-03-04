# Amazon Price Tracker

A Python tool that scrapes Amazon product data and sends email alerts when prices drop below a defined threshold.  
Demonstrates web scraping, secure environment handling, and SMTP-based notifications.

---

## 🚀 Overview

Automates price tracking for a single product:

- Sends HTTP requests to a product page
- Parses HTML with BeautifulSoup
- Extracts product title and price
- Cleans text & converts price to float
- Compares price against a threshold
- Sends email alert if below threshold

---

## 🛠 Tech Stack

- Python 3.10+
- requests, beautifulsoup4, smtplib, python-dotenv, re

---

## 📁 Project Structure

```
amazon-price-tracker/
│
├── main.py
├── requirements.txt
├── .env (not committed)
├── .gitignore
└── README.md
```

---

## 🔐 Setup

1. Create `.env`:

```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
EMAIL_TO_ADDRESS=recipient_email@gmail.com
```

2. Add `.env` to `.gitignore`:

```
venv/
.env
__pycache__/
```

---

## 📦 Installation

```
git clone https://github.com/bhoffart/amazon-price-tracker
cd amazon-price-tracker
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Run Script

```
python main.py
```

Sends email if price falls below threshold (e.g., $100).

---

## 📧 Example Email

```
Subject: Amazon Price Alert!

Instant Pot Duo 7-in-1 Electric Pressure Cooker is now $89.99.
https://product-link
```

---

## ⚠ Limitations

- Single product only
- No historical data storage
- Depends on static HTML structure
- No request headers (may get blocked)

---

## 📈 Future Improvements

- Add headers to reduce blocking
- Track multiple products
- Store price history (CSV/DB)
- Logging instead of prints
- Configurable threshold via env
- Schedule with cron/Task Scheduler
- Modular functions
- Simple Flask dashboard

---

## 💼 Key Skills Demonstrated

- Web scraping & data extraction
- Regex text cleaning
- Float conversion & numeric comparison
- SMTP authentication & secure env handling
- Conditional automation logic
- Clean Python scripting from concept to execution