import socket


def scan_port(ip, port):
    """
    Checks whether a specific port is open.
    Returns True if open, False otherwise.
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(0.05)

    result = sock.connect_ex((ip, port))

    sock.close()

    return result == 0


def scan_ports(ip, start_port, end_port):
    """
    Scans a range of ports.
    Returns a list of open ports.
    """

    open_ports = []

    for port in range(start_port, end_port + 1):

        if scan_port(ip, port):
            open_ports.append(port)

    return open_ports