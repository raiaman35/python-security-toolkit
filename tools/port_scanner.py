import socket
import threading
from colorama import Fore, Style, init
from tabulate import tabulate

init(autoreset=True)

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 3306: "MySQL",
    3389: "RDP", 5432: "PostgreSQL", 8080: "HTTP-Alt",
    8443: "HTTPS-Alt", 27017: "MongoDB"
}

open_ports = []
lock = threading.Lock()

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown")
            with lock:
                open_ports.append([port, service, "OPEN"])
    except:
        pass

def run():
    print(f"\n{Fore.CYAN}{'='*45}")
    print(f"{Fore.CYAN}        PORT SCANNER")
    print(f"{Fore.CYAN}{'='*45}")

    host = input("Target IP or hostname: ").strip()
    start = int(input("Start port (e.g. 1): ").strip())
    end   = int(input("End port (e.g. 1024): ").strip())

    print(f"\n{Fore.CYAN}Scanning {host} ports {start}-{end}...")

    open_ports.clear()
    threads = []
    for port in range(start, end + 1):
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)
        t.start()
        if len(threads) % 100 == 0:
            for th in threads:
                th.join()
            threads = []

    for t in threads:
        t.join()

    open_ports.sort(key=lambda x: x[0])

    print(f"\n{Fore.GREEN}Scan complete.")
    if open_ports:
        print(f"{Fore.RED}Open ports found: {len(open_ports)}\n")
        print(tabulate(open_ports, headers=["Port","Service","Status"], tablefmt="grid"))

        with open("reports/port_scan_report.txt", "w") as f:
            f.write(f"PORT SCAN REPORT\nTarget: {host}\n")
            f.write(f"Range: {start}-{end}\n\n")
            for p in open_ports:
                f.write(f"Port {p[0]} | {p[1]} | {p[2]}\n")
        print(f"\n{Fore.GREEN}Report saved to reports/port_scan_report.txt")
    else:
        print(f"{Fore.YELLOW}No open ports found in range {start}-{end}")