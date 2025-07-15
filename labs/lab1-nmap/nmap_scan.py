import nmap
import datetime
import os

def run_nmap_scan(target_ip, output_dir='labs/lab1-nmap/nmap_scan_reports'):
    os.makedirs(output_dir, exist_ok=True)
    nm = nmap.PortScanner()
    print(f"Starting Nmap scan on {target_ip} ...")
    print("Running TCP connect scan on all ports...")
    nm.scan(target_ip, arguments='-sT -p-')
    tcp_scan_report = nm.csv()
    common_ports = '21,22,80,445'
    print(f"Running service/version detection on ports: {common_ports} ...")
    nm.scan(target_ip, arguments=f'-sV -p {common_ports}')
    svc_scan_report = nm.csv()
    print("Running OS detection...")
    nm.scan(target_ip, arguments='-O')
    os_info = nm[target_ip]['osmatch'][0] if nm[target_ip].has_os_match() else None
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    tcp_file = os.path.join(output_dir, f'tcp_scan_{timestamp}.csv')
    svc_file = os.path.join(output_dir, f'service_scan_{timestamp}.csv')
    os_file = os.path.join(output_dir, f'os_detection_{timestamp}.txt')
    with open(tcp_file, 'w') as f:
        f.write(tcp_scan_report)
    print(f"TCP scan results saved to {tcp_file}")
    with open(svc_file, 'w') as f:
        f.write(svc_scan_report)
    print(f"Service/version scan results saved to {svc_file}")
    with open(os_file, 'w') as f:
        if os_info:
            f.write(f"OS Match: {os_info['name']} (Accuracy: {os_info['accuracy']}%)\n")
            f.write(f"OS Class: {os_info['osclass'][0]['osfamily']} - {os_info['osclass'][0]['osgen']}\n")
        else:
            f.write("No OS information detected.\n")
    print(f"OS detection results saved to {os_file}")
    print("Nmap scan completed.")

if __name__ == "__main__":
    target = input("Enter target IP address: ").strip()
    run_nmap_scan(target)
