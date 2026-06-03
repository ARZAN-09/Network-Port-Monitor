from datetime import datetime


def generate_report(ip, open_ports, risk_level, warnings):

    filename = "report.txt"

    with open(filename, "w") as file:

        file.write("NETWORK PORT MONITORING REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write(
            f"Scan Date: {datetime.now()}\n"
        )

        file.write(
            f"Target IP: {ip}\n\n"
        )

        file.write("OPEN PORTS\n")
        file.write("-" * 20 + "\n")

        if open_ports:

            for port in open_ports:
                file.write(f"{port}\n")

        else:
            file.write("No open ports found\n")

        file.write("\n")

        file.write(
            f"Risk Level: {risk_level}\n\n"
        )

        file.write("WARNINGS\n")
        file.write("-" * 20 + "\n")

        if warnings:

            for warning in warnings:
                file.write(
                    warning + "\n"
                )

        else:
            file.write(
                "No major risks detected\n"
            )

    return filename