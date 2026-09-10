# import socket  # standard library module for low-level networking

# # Option C: Basic Port Scanner (LOCAL TEST TARGET ONLY -- e.g. "127.0.0.1")
# def check_ports(host, ports):  # define a function checking a fixed list of ports on host
#     """Print open/closed for each port in ports on host. (floor)"""
#     for port in ports:  # loop over each port to check
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a TCP/IPv4 socket
#         sock.settimeout(0.5)  # cap how long to wait for a connection attempt
#         result = sock.connect_ex((host, port))  # try to connect; returns 0 on success, an error code otherwise
#         sock.close()  # release the socket
#         status = "open" if result == 0 else "closed"  # translate the result code into a human-readable status
#         print(f"{host}:{port} -> {status}")  # print the host:port and its status

# def scan_range(host, start_port, end_port):  # define a function scanning a contiguous range of ports
#     """Scan a small range and report open/closed cleanly. (ceiling)"""
#     check_ports(host, range(start_port, end_port + 1))  # reuse check_ports over the inclusive port range

import socket  # standard library module for low-level networking

# Option C: Basic Port Scanner (LOCAL TEST TARGET ONLY -- e.g. "127.0.0.1")
def check_ports(host, ports):  # define a function checking a fixed list of ports on host
    """Print open/closed for each port in ports on host. (floor)"""
    for port in ports:  # loop over each port to check
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a TCP/IPv4 socket
        sock.settimeout(0.5)  # cap how long to wait for a connection attempt
        result = sock.connect_ex((host, port))  # try to connect; returns 0 on success, an error code otherwise
        sock.close()  # release the socket
        status = "open" if result == 0 else "closed"  # translate the result code into a human-readable status
        print(f"{host}:{port} -> {status}")  # print the host:port and its status

def scan_range(host, start_port, end_port):  # define a function scanning a contiguous range of ports
    """Scan a small range and report open/closed cleanly. (ceiling)"""
    check_ports(host, range(start_port, end_port + 1))  # reuse check_ports over the inclusive port range


# --- Actually run it ---

target = "127.0.0.1"  # local test target only

# A fixed list of specific ports to check
ports_to_check = [21, 22, 23, 25, 53, 80, 443, 3306, 8080]

check_ports(target, ports_to_check)