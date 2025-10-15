#! /usr/bin/env python3

import psutil
import sys
import shutil
import socket
import emails

# check if CPU usage is over 80%
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

# check if available disk space is lower than 20%
def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    free_percent = (free / total) * 100
    return free_percent

# check if available memory is less than 100MB
def check_free_memory():
    available_memory = psutil.virtual_memory().available
    available_memory_mb = available_memory / (1024 * 1024)
    return available_memory_mb

# check if the hostname "localhost" cannot be resolved to "127.0.0.1"
def check_hostname_resolved():
    hostname = "localhost"
    ip = "127.0.0.1"

    try:
        result = socket.gethostbyname(hostname)
        return True if result == ip else False
    except socket.gaierror:
        return False  # Hostname cannot be resolved

def main(argv):
    error_messages = []
    checks = [
        (check_cpu_usage() > 80, "Error - CPU usage is over 80%"),
        (check_disk_space() < 20, "Error - Available disk space is less than 20%"),
        (check_free_memory() < 100, "Error - Available memory is less than 100MB"),
        (not check_hostname_resolved(), "Error - localhost cannot be resolved to 127.0.0.1")
    ]

    for condition, message in checks:
        if condition:
            error_messages.append(message)

    if error_messages:
        sender = "automation@example.com"
        receiver = "student@example.com"
        body = "Please check your system and resolve the issue as soon as possible."
        for subject_line in error_messages:
            subject = subject_line
            message = emails.generate_email(sender, receiver, subject, body)
            emails.send_email(message)


if __name__ == "__main__":
    main(sys.argv)