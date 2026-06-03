from scanner import scan_ports
from service_mapper import SERVICES
from risk_analyzer import analyze_risk
from report_generator import generate_report

def main():

    print("=" * 40)
    print("Network Port Monitoring System")
    print("=" * 40)

    ip = input("Enter IP Address: ")

    print("\nScanning ports...")
    print("Please wait...\n")

    open_ports = scan_ports(ip, 1, 1000)

    if not open_ports:
        print("No open ports found.")
        return

    print("Open Ports Found")
    print("-" * 30)

    for port in open_ports:

        service = SERVICES.get(
            port,
            "Unknown Service"
        )

        print(f"Port {port:<5} Service: {service}")
    risk_level, warnings = analyze_risk(open_ports)
    print("\n" + "=" * 40)
    print("Risk Assessment")
    print("=" * 40)

    print(f"Risk Level: {risk_level}")

    if warnings:

        print("\nWarnings:")

        for warning in warnings:
            print("-", warning)

    else:
        print("\nNo major risks detected.")

    report_file = generate_report(  
        ip,
        open_ports,
        risk_level,
        warnings
    )   

    print(f"\nReport saved as: {report_file}")


if __name__ == "__main__":
    main()