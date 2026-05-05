from flask import Flask, jsonify, render_template
from parser import get_failed_logins
from detector import detect_bruteforce
import psutil

app = Flask(__name__)

def get_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        processes.append(proc.info)
    return processes

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/alerts")
def alerts():
    ips = get_failed_logins()
    suspicious = detect_bruteforce(ips)
    return jsonify(suspicious)

# ✅ NEW API
@app.route("/processes")
def processes():
    return jsonify(get_processes())

if __name__ == "__main__":
    app.run(debug=True)
