import hashlib
import json
import os
from datetime import datetime

def  calculate_hash(file_path):
    with open(file_path,"rb") as file:
        hasher = hashlib.sha256()

        while chunk := file.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

def log_event(message):
    timestamp =datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs/fim.log","a") as log_file:
        log_file.write(f"{timestamp} | {message}\n")





def create_baseline():
    files = [
        "sample_files/employee_record.txt",
        "sample_files/finance_report.txt",
        "sample_files/security_policy.txt"
    ]

    baseline = {}

    for file_path in files:
        baseline[file_path] = calculate_hash(file_path)
    with open("baseline.json","w") as file:
        json.dump(baseline,file,indent=4)


def check_integrity():
    with open("baseline.json","r") as file:
        baseline = json.load(file)

    for file_path,original_hash in  baseline.items():

        if not os.path.exists(file_path):
            print("\n🚨 FILE DELETED")
            print("File:", file_path)
            print("Status: FILE MISSING\n")

            log_event(
                f"ALERT | FILE DELETED | {file_path}"
            )

            continue

        current_hash = calculate_hash(file_path)
        if  current_hash == original_hash:
            print(" ✅ INTEGRITY OK : ", file_path)
        else:
            print("\n🚨 FILE MODIFIED")
            print("File:", file_path)
            print("Expected SHA-256:", original_hash)
            print("Current SHA-256 :", current_hash)
            print("Status: INTEGRITY VIOLATION\n")

            log_event(
                f"ALERT | FILE MODIFIED | {file_path} | "
                f"Expected: {original_hash} | Current: {current_hash}"
            )

    baseline_files = set(baseline.keys())

    for file_name in os.listdir("sample_files"):
        file_path = os.path.join("sample_files", file_name)

        if file_path not in baseline_files:
            print("\n🚨 NEW FILE DETECTED")
            print("File:", file_path)
            print("Status: NOT IN BASELINE\n")

            log_event(
                f"ALERT | NEW FILE | {file_path}"
            ) 

check_integrity()

