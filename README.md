# Python for Security

Beginner-friendly Python exercises focused on cybersecurity fundamentals, log analysis, regular expressions, and security automation.

## Topics

- Reading and filtering log files
- Parsing log entries
- Extracting IP addresses with regular expressions
- Counting failed login attempts
- Finding the most common suspicious IP addresses
- Writing filtered security logs

## Project Structure

```text
python-for-security/
├── README.md
├── .gitignore
├── requirements.txt
├── notebooks/
│   └── day-1-activities.ipynb
├── notes/
│   └── day1.md
├── exercises/
│   └── day1/
│       ├── 01_filter_info_logs.py
│       ├── 02_parse_log_line.py
│       ├── 03_extract_ip_address.py
│       ├── 04_find_matching_lines.py
│       ├── 05_count_failed_logins.py
│       └── 06_top_failed_login_ips.py
└── data/
    ├── demo_service.log
    ├── drill_sample.log
    ├── exercise_log.log
    └── sample_auth.log
