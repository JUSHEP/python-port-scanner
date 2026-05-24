import socket
from datetime import datetime

target = input("Enter target IP or domain: ")

print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    target_ip = socket.gethostbyname(target)

    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        139: "NetBIOS",
        143: "IMAP",
        443: "HTTPS",
        445: "SMB",
        3306: "MySQL",
        3389: "RDP"
    }

    for port, service in common_ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"[OPEN] Port {port} ({service})")

        sock.close()

except socket.gaierror:
    print("Hostname could not be resolved.")

except KeyboardInterrupt:
    print("\nScan interrupted.")

except Exception as e:
    print(f"Error: {e}")