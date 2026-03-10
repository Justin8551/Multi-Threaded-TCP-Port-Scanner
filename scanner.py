import socket
import sys
from datetime import datetime

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip,port))
            return result == 0
    except Exception:
        return False
    
def main():
    if(len(sys.argv)) == 2:
        target_input = sys.argv[1]
    else:
        print("Utilizeaza python3 scanner.py <ip_sau_host>")
        sys.exit()
    try:
        target = socket.gethostbyname(target_input)
    except socket.gaierror:
        print("Nu s a gasit numele.")
        sys.exit()
    print("-" * 25)
    print(f"Scanam: {target} ({target_input})")
    print(f"Scanarea a inceput la: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 25)
    
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389, 8080]
    
    try:
        for port in common_ports:
            if scan_port(target, port):
                print(f"[+] Port {port:5}: DESCHIS")
    except KeyboardInterrupt:
        print("Utilizatorul a intrerupt rularea.")
        sys.exit()

    print("-" * 25)

if __name__ == "__main__":
    main()
