# File Integrity Monitoring System

A beginner-friendly cybersecurity project that detects unauthorized changes to critical files using SHA-256 cryptographic hashing.

##  Project Overview

File Integrity Monitoring (FIM) is a defensive security mechanism used to detect changes to important files.

This project creates a trusted baseline by calculating the SHA-256 hash of monitored files. During subsequent integrity checks, the current hash of each file is compared with its baseline hash.

The system can detect:

- Modified files
- Deleted files
- Newly introduced files
- Integrity violations

Detected security events are recorded in a security event log.

##  Objectives

- Understand file integrity monitoring concepts
- Implement SHA-256 hashing using Python
- Create and maintain a trusted file baseline
- Detect unauthorized file modifications
- Detect deleted protected files
- Detect newly introduced files
- Record security events for investigation
- Demonstrate a controlled attack-and-detection scenario

## 🛠️ Technologies Used

- Python 3
- SHA-256
- JSON
- Linux / Ubuntu
- Bash
- Git & GitHub

##  How the System Works

The FIM follows this process:

```text
                    ┌──────────────────┐
                    │ Protected Files  │
                    └────────┬─────────┘
                             │
                             ▼
                    Calculate SHA-256
                             │
                             ▼
                    ┌──────────────────┐
                    │ Trusted Baseline │
                    │   baseline.json  │
                    └────────┬─────────┘
                             │
                             ▼
                    Periodic Integrity Check
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
          Modified        Deleted        New File
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                       Security Alert
                             │
                             ▼
                       Event Logging



##  SHA-256 Integrity Verification

Each monitored file is converted into a SHA-256 cryptographic hash.

Example:

File:
sample_files/finance_report.txt

Trusted SHA-256:

21ff010c04cb619a902869227068a2a2198207f067cccd419f721b78e55332bf

If even a small part of the file changes, its SHA-256 hash changes.

The FIM compares:

Expected Hash
      ↓
Current Hash
      ↓
Match? ── Yes ──> Integrity OK
      │
      No
      ↓
Integrity Violation

##  Detection Capabilities

### 1. File Modification

If a monitored file is modified, the system compares its current SHA-256 hash with the trusted baseline.

Example alert:

🚨 FILE MODIFIED
File: sample_files/finance_report.txt
Expected SHA-256: <baseline hash>
Current SHA-256 : <current hash>
Status: INTEGRITY VIOLATION

### 2. File Deletion

If a file present in the baseline is missing from the monitored directory:

🚨 FILE DELETED
File: sample_files/security_policy.txt
Status: FILE MISSING

### 3. New File Detection

The system also checks the monitored directory for files that are not present in the trusted baseline.

Example:

🚨 NEW FILE DETECTED
File: sample_files/backup.txt
Status: NOT IN BASELINE

The detection does not depend on the filename containing words such as "unauthorized".

A file is considered new because it was not present in the trusted baseline.

## 📝 Security Event Logging

Security events are recorded for investigation.

Example:

ALERT | FILE MODIFIED | sample_files/finance_report.txt
ALERT | FILE DELETED | sample_files/security_policy.txt
ALERT | NEW FILE | sample_files/backup.txt

The log provides useful information for a defensive security investigation.

##  Proof of Concept

A controlled PoC was performed to demonstrate:

1. Trusted baseline
2. File modification
3. Modification detected
4. Event logged
5. File recovered
6. File deletion
7. Deletion detected
8. Event logged
9. File recovered
10. New file introduced
11. New file detected
12. Final integrity verification

### Final Result

After recovery and cleanup:

✅ INTEGRITY OK : sample_files/employee_record.txt
✅ INTEGRITY OK : sample_files/finance_report.txt
✅ INTEGRITY OK : sample_files/security_policy.txt

##  Project Structure

File-integrity-monitor/
├── README.md
├── monitor.py
├── baseline.json
├── requirements.txt
├── sample_files/
│   ├── employee_record.txt
│   ├── finance_report.txt
│   └── security_policy.txt
├── evidence/
│   └── before_attack/
├── screenshots/
└── demo/

## ▶Installation

Clone the repository:

git clone <repository-url>
cd File-integrity-monitor

Check Python:

python3 --version

## ▶ Usage

Run the FIM:

python3 monitor.py

The program compares the current state of monitored files against baseline.json.

##  Evidence

The project contains evidence collected during controlled testing, including:

- Original trusted files
- SHA-256 hashes
- Modification detection
- File deletion detection
- New file detection
- Security event logs
- Recovery verification
- Project structure

Screenshots are available in the screenshots/ directory.

## ⚠ Disclaimer

This project is intended for educational and defensive cybersecurity purposes.

All attack simulations were performed against locally created test files in a controlled environment.

##  Future Improvements

Possible future enhancements include:

- Real-time file monitoring using filesystem events
- Email or Telegram alerts
- SIEM integration
- MITRE ATT&CK mapping
- File metadata monitoring
- Automated baseline management
- Centralized logging
- Web-based monitoring dashboard
- Alert severity classification
