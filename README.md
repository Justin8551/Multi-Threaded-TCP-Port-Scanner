# Multi-Threaded-TCP-Port-Scanner

This is a simple but effective multi-threaded TCP Port Scanner developed in Python. It allows you to identify open ports on a target host by sending TCP SYN packets and analyzing the responses. This tool demonstrates core networking concepts, socket programming and robust error handling.

Features:
  -DNS Resolution: Automatically resolves hostnamesto IPv4 addresses.
  -Socket Optimization: Implements custom timeouts to ensure fast scanning without hanging on unresponsive ports.
  -Professional Logging: Provides a detailed report including start time, target IP, and a list of open ports.

Usage:

Prerequisites
    -Python 3.x installed on your system.
Run the scanner
    - "python3 scanner.py <target_ip_or_hostname>"

