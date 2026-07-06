import socket
import datetime

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return True 
        return False
    except:
        return False

def get_service(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown"

def run_scanner():
    print("=" * 80)
    print("       TIMOBEST PORT SCANNER")
    print("=" * 80)
    
    host = input("\nEnter target IP or hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    testing_name = str(input("Scanner Name:"))
    
    print(f"\nScanning {host} from port {start_port} to {end_port} by {testing_name}")
    print(f"Started at: {datetime.datetime.now()}")
    print("-" * 80)
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            service = get_service(port)
            open_ports.append(port)
            print(f"[OPEN] Port {port} --> {service}")
    
    print("-" * 50)
    print(f"\nScan complete!")
    print(f"Total open ports found: {len(open_ports)}")
    print(f"Finished at: {datetime.datetime.now()}")
    print("=" * 50)

run_scanner()

