from collections import Counter

def detect_bruteforce(ip_list):
    counts = Counter(ip_list)

    alerts = {}
    for ip, count in counts.items():
        if count > 3:
            alerts[ip] = count

    return alerts
