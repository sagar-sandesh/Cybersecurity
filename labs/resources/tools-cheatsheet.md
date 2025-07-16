# Cybersecurity Tools Cheatsheet

## Nmap  
- Scan all TCP ports: `nmap -sT -p- <target>`  
- Service detection: `nmap -sV <target>`  
- OS detection: `nmap -O <target>`  

## Wireshark  
- Capture packets: start capture on interface  
- Filter example: `http` or `tcp.port==80`  


## Metasploit  
- Start msfconsole: `msfconsole`  
- Search exploit: `search <service>`  
- Use exploit: `use exploit/<path>`  
- Set target: `set RHOST <target_ip>`  
- Run exploit: `run` or `exploit`  
