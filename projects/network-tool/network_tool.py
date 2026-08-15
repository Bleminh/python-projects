import argparse
import requests
import subprocess
import socket

def clean_host(host):
    if not host:
        return ""
    cleaned = host.replace("http://", "").replace("https://", "")
    cleaned = cleaned.split('/')[0]
    return cleaned

def run_ping(host):
    if not host:
        print("Error: You must specify a host to ping!")
        return
    print(f"Preparing to ping: {host}")
    print(f"Ping {host} (4 packets...)")
    # Use -c 4 so it stops after 4 pings
    # capture_output grabs the terminal text, text=True turns it into a string
    result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)

    if result.returncode == 0:
        print(result.stdout)
    else:
        # If it failed, print the error output
        print("Ping failed.")
        print(result.stderr)

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        ip_data = response.json()
        print("Fetching your public IP address...")
        print(f"Your public IP is: {ip_data['ip']}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch IP: {e}")

def run_dns(host):
    if not host:
        print("Error: You must specify a host for DNS lookup")
        return
    print("Looking up DNS records for: {host}")
    result = subprocess.run(["dig", "+short", host], capture_output=True, text=True)

    if result.returncode == 0 and result.stdout.strip():
        print(result.stdout.strip())
    else:
        print("DNS lookup failed or no records found")

def scan_ports(host):
    if not host:
        print("Error: You must specify a host to scan")
        return

    print(f"Scanning ports 22, 80, and 443 on {host}...")
    ports = [22, 80, 443]

    for port in ports:
        # Create a new TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # 2-second timeout so it doesn't hang forever on dropped packets
            s.settimeout(2.0) 
            # connect_ex returns 0 if the connection succeeded
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"  [+] Port {port}: OPEN")
            else:
                print(f"  [-] Port {port}: CLOSED / FILTERED")

def run_traceroute(host):
    if not host:
        print("Error: You must specify a host to trace")
        return
    print(f"Tracing route to {host} (this may take a minute)...")
    try:
        subprocess.run(["traceroute", host])
    except FileNotFoundError:
        print("Error: 'traceroute command not found on this system")

def main():
    parser = argparse.ArgumentParser(description="A custom network diagnostics CLI.")
    parser.add_argument("action", choices=["ping", "dns", "ip", "ports", "traceroute"])
    parser.add_argument("host", nargs="?", default="")
    args = parser.parse_args()

    target_host = clean_host(args.host)

    try:
        if args.action == "ping":
            run_ping(target_host)
            
        elif args.action == "dns":
            run_dns(target_host)
            
        elif args.action == "ip":
            get_public_ip()
            
        elif args.action == "ports":
            scan_ports(target_host)
            
        elif args.action == "traceroute":
            run_traceroute(target_host)

    except KeyboardInterrupt:
        # This catches Ctrl+C
        print("\n Scan cancelled by user. Exiting gracefully.")
    except Exception as e:
        # This catches any other weird Python crashes
        print(f"\n An unexpected error occurred: {e}")
        
if __name__ == "__main__":
    main()    