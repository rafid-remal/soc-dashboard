# 🛡️ SOC Mini Security Monitoring Dashboard

A lightweight **Security Operations Center (SOC) simulation project** built using Python and Flask. It analyzes Linux system logs, detects failed login attempts, identifies brute-force attacks, and visualizes security events in a web dashboard.

---

## 🚀 Features

- 🔐 Failed login detection from system logs  
- 🚨 Brute-force attack detection (IP-based thresholding)  
- 🖥️ Process monitoring (running system processes)  
- 📊 Log visualization using charts (Chart.js)  
- ⚡ Real-time security alerts via Flask API  

---

## 🧠 Real-world analogy

This project simulates a **Security Operations Center (SOC)**:

- Log collection → like SIEM ingestion  
- Detection engine → like threat analysis system  
- Dashboard → like SOC monitoring screen used by analysts  

---

## 🛠️ Tech Stack

- Python 3  
- Flask  
- Linux Log Analysis (journalctl / auth logs)  
- Chart.js (frontend visualization)  
- psutil (process monitoring)

---

## 📁 Project Structure

```text
soc-dashboard/
│
├── app.py               # Flask backend
├── parser.py            # Log extraction logic
├── detector.py          # Brute-force detection logic
│
├── templates/
│   └── index.html       # Dashboard UI
│
├── static/
│   ├── style.css        # UI styling
│   └── script.js       # Frontend logic
│
└── README.md


---

# 🔥 What I improved for you

✔ Added full installation commands  
✔ Added run instructions  
✔ Added testing commands  
✔ Added project structure  
✔ Clean professional formatting  
✔ Made it GitHub-ready (CV-level)

---

If you want next upgrade, I can help you

👉 Follow the installation steps below

# 🛡️ SOC Mini Security Monitoring Dashboard

## ⚙️ How to Run This Project

### 1. Clone the repository

```bash
git clone git@github.com:YOUR_USERNAME/soc-dashboard.git
cd soc-dashboard

### 2. Create virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate

### 3. Create virtual environment (Windows)

```bash
venv\Scripts\activate

### 4. Install dependencies

```bash
pip install flask psutil

### 5. Run the application

```bash
python app.py

### 6. Open in browser

```bash
http://127.0.0.1:5000

### 7. 🧪 Testing the project

```bash
ssh wronguser@localhost


