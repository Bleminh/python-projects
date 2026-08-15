# Network Diagnostics CLI

A Python-based command-line interface for network troubleshooting and diagnostics. Built using `argparse`, `subprocess`, and raw TCP sockets.

## Features
* **Ping**: Check host reachability using ICMP.
* **DNS**: Perform domain name resolution (via `dig`).
* **IP**: Fetch the network's public IPv4 address.
* **Port Scanner**: Verify standard web and SSH ports (22, 80, 443) using TCP socket connections.
* * **Traceroute**: Map the network path to a target host at Layer 3.

## Prerequisites
* Python 3.x
* A Unix-based environment (macOS/Linux) for `ping` and `dig` utilities.

## Usage

Run the tool via the terminal by passing an action and a target host.

```bash
# View the help menu
python network_tool.py -h

# Fetch your public IP
python network_tool.py ip

# Ping a host
python network_tool.py ping github.com

# Lookup DNS records
python network_tool.py dns openai.com

# Scan common ports
python network_tool.py ports hust.edu.vn

# Trace the network path
python network_tool.py traceroute google.com