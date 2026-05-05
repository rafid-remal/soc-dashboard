import subprocess
import re

def get_failed_logins():
    result = subprocess.run(
        "journalctl | grep 'Failed password'",
        shell=True,
        capture_output=True,
        text=True
    )

    lines = result.stdout.split("\n")
    ips = []

    for line in lines:
        match = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
        if match:
            ips.append(match[0])

    return ips
