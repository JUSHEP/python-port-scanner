import socket
import time
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.CYAN}
██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝██║   ██║██████╔╝   ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║
██║     ╚██████╔╝██║  ██║   ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝

███████╗ ██████╗ █████╗ ███╗   ██╗
██╔════╝██╔════╝██╔══██╗████╗  ██║
███████╗██║     ███████║██╔██╗ ██║
╚════██║██║     ██╔══██║██║╚██╗██║
███████║╚██████╗██║  ██║██║ ╚████║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""

print(BANNER)

target = input(f"{Fore.YELLOW}Enter target IP or hostname: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print(f"{Fore.RED}Invalid hostname or IP address.")
    exit()

start_port = int(input(f"{Fore.YELLOW}Start port: "))
end_port = int(input(f"{Fore.YELLOW}End port: "))

print(f"\n{Fore.CYAN}Scanning target: {target_ip}")
print(f"{Fore.CYAN}Port range: {start_port}-{end_port}")
print(f"{Fore.CYAN}Starting scan...\n")

start_time = time.time()

try:
    for port in range(start_port, end_port + 1):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(0.5)

        result = scanner.connect_ex((target_ip, port))

        if result == 0:
            print(f"{Fore.GREEN}[OPEN] Port {port}")

        scanner.close()

except KeyboardInterrupt:
    print(f"\n{Fore.RED}Scan interrupted by user.")
    exit()

except Exception as e:
    print(f"{Fore.RED}Error: {e}")

end_time = time.time()
total_time = round(end_time - start_time, 2)

print(f"\n{Fore.MAGENTA}Scan completed in {total_time} seconds.")
print(Style.RESET_ALL)