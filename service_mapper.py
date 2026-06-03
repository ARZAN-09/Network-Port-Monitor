import socket
def get_service_name(port, protocol="tcp"):
    """
    Dynamically looks up the service name for any given port.
    Falls back to 'Unknown Service' if the port isn't standard.
    """
    try:
        return socket.getservbyport(port, protocol).upper()
    except (OSError, OverflowError):
        return "Unknown Service"

def scan_ports(ip, start_port, end_port):
    open_ports = []
    start_port = int(start_port)
    end_port = int(end_port)
    
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    print(f"{'PORT':<10}{'STATUS':<15}{'SERVICE'}")
    print("-" * 40)
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) 
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            service = get_service_name(port)
            print(f"{port:<10}{'OPEN':<15}{service}")
            open_ports.append((port, service))
            
        sock.close()
    return open_ports
