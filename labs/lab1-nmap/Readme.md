# Lab 1 - Nmap Basics

## Objective  
Learn how to perform basic port scanning, service detection, and OS fingerprinting with Nmap.

## Setup  
- Target: Metasploitable 2 VM  
- Attacker: Kali Linux VM

## Tasks Completed  
- TCP connect scan on target IP  
- Service and version detection  
- OS fingerprinting

## Summary  
- Found open ports: 21, 22, 80, 445...  
- FTP service running vsFTPd 2.3.4 vulnerable to backdoor exploit  
- OS detected as Linux Ubuntu

## Screenshots  
![Nmap Scan](screenshots/nmap_scan.png)

## Notes  
- Nmap is extremely versatile for reconnaissance.  
- Use `-sV` for version detection and `-O` for OS detection.  
- Save results with `-oN filename.txt`.

## Commands Used  
nmap -sT -p- -O 192.168.56.101
nmap -sV -p21,22,80 192.168.56.101

