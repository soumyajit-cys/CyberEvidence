# Automated Digital Forensics Investigation Framework for Kali Linux

## Overview

The **Automated Digital Forensics Investigation Framework (ADFIF)** is a modular cybersecurity tool designed to automate the process of digital evidence collection, analysis, and reporting on a Linux system. The framework is specifically designed to run on **Kali Linux** and assists investigators in performing rapid forensic analysis during incident response or security investigations.

This system collects forensic artifacts from the system, analyzes files, examines system logs, inspects network traffic, extracts metadata from digital media, and stores the evidence in a structured database. Investigators can access the results through a **Flask-based web dashboard** and generate an automated forensic investigation report.

The project demonstrates core concepts used in **Digital Forensics and Incident Response (DFIR)**, including artifact collection, log analysis, file hashing, network packet inspection, and forensic reporting.

---

# Key Features

### Automated Evidence Collection

The system automatically collects files and artifacts from critical system directories including:

* `/var/log`
* `/home`
* `/tmp`
* `/etc`

These directories are commonly analyzed during forensic investigations.

### File System Forensics

The framework performs file analysis including:

* Directory scanning
* File hashing using **SHA256**
* Detection of suspicious files
* Detection of hidden files
* Identification of recently modified files

All results are stored in the forensic database.

### Log Analysis

The log analyzer investigates important Linux security logs such as:

* `/var/log/auth.log`

It detects:

* Failed login attempts
* Suspicious sudo activity
* Unauthorized access attempts
* Potential brute force attacks

### Network Forensics

Using **Scapy**, the system analyzes network capture files (PCAP) to identify:

* Source and destination IP addresses
* Protocol usage
* Suspicious connections
* Possible port scanning activity

### Metadata Extraction

The framework extracts metadata from digital images including:

* Camera/device information
* Creation timestamps
* GPS coordinates

This information is useful in investigations involving digital media.

### Evidence Database

All forensic evidence is stored in an **SQLite database** which includes the following tables:

* Files
* Logs
* Network
* Metadata

This allows investigators to query and analyze forensic artifacts efficiently.

### Investigation Dashboard

A **Flask web dashboard** provides an investigator-friendly interface that displays:

* Evidence overview
* File analysis results
* Security log events
* Network activity
* Metadata artifacts

### Automated Forensic Report

The system automatically generates an **HTML forensic investigation report** summarizing all detected artifacts and security events.

---

# Project Architecture

```
Evidence Collection
        │
        ▼
File Forensics ─ Log Analysis ─ Network Analysis ─ Metadata Extraction
        │
        ▼
SQLite Evidence Database
        │
        ▼
Flask Investigation Dashboard
        │
        ▼
Automated Forensic Report
```

---

# Project Structure

```
digital-forensics-framework
│
├── app.py
├── run_scan.py
├── config.py
├── requirements.txt
│
├── modules
│   ├── evidence_collector.py
│   ├── file_forensics.py
│   ├── log_analyzer.py
│   ├── network_analyzer.py
│   ├── metadata_extractor.py
│
├── database
│   ├── db_manager.py
│   └── evidence.db
│
├── reports
│   └── report_generator.py
│
├── dashboard
│   └── templates
│       ├── dashboard.html
│       ├── files.html
│       ├── logs.html
│       ├── network.html
│       ├── metadata.html
│
└── scans
```

---

# Technology Stack

| Component            | Technology |
| -------------------- | ---------- |
| Programming Language | Python 3   |
| Operating System     | Kali Linux |
| Web Framework        | Flask      |
| Database             | SQLite     |
| Network Analysis     | Scapy      |
| Metadata Extraction  | ExifRead   |
| System Monitoring    | Psutil     |

---

# Installation

### 1. Clone the Repository

```
git clone https://github.com/yourusername/digital-forensics-framework.git

cd digital-forensics-framework
```

### 2. Install Dependencies

```
pip3 install -r requirements.txt
```

---

# Running the Framework

## Step 1 — Run the Forensic Scan

```
python3 run_scan.py
```

This command performs:

* Evidence collection
* File analysis
* Log analysis
* Network packet analysis
* Metadata extraction
* Report generation

---

## Step 2 — Start the Dashboard

```
python3 app.py
```

Open your browser:

```
http://127.0.0.1:5000/dashboard
```

---

# Example Output

The framework produces the following outputs:

### Evidence Database

```
database/evidence.db
```

### Investigation Report

```
reports/forensic_report.html
```

### Dashboard Pages

* `/dashboard`
* `/files`
* `/logs`
* `/network`
* `/metadata`

---

# Example Investigation Results

The system may detect artifacts such as:

* Suspicious executable files
* Hidden scripts in temporary directories
* Multiple failed SSH login attempts
* Unauthorized sudo activity
* Suspicious external network connections
* Image files containing GPS metadata

---

# Advanced Features (Future Improvements)

Possible enhancements include:

* Malware detection using **YARA rules**
* Timeline reconstruction of forensic events
* Memory forensics integration using **Volatility**
* Machine learning based anomaly detection
* Real-time monitoring and alerting

---

# Use Cases

This framework can be used for:

* Digital forensic investigations
* Incident response analysis
* Security research
* Cybersecurity learning projects
* Academic DFIR demonstrations

---

# Learning Outcomes

This project demonstrates practical knowledge in:

* Digital forensics automation
* Linux artifact analysis
* File hashing and integrity verification
* Log analysis
* Network packet investigation
* Database evidence management
* Web-based investigation dashboards

---

# Author

Soumyajit Dutta

Cybersecurity | Digital Forensics | Python Security Development

---

# License

This project is released for educational and research purposes.
