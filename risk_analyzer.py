HIGH_RISK_PORTS = {
    21: "FTP",
    23: "Telnet",
    139: "NetBIOS",
    445: "SMB",
    3306: "MySQL"
}


def analyze_risk(open_ports):

    warnings = []
    risk_score = 0

    for port in open_ports:

        if port in HIGH_RISK_PORTS:

            warnings.append(
                f"Port {port} ({HIGH_RISK_PORTS[port]}) is exposed"
            )

            risk_score += 20

    if risk_score == 0:
        risk_level = "Low"

    elif risk_score <= 40:
        risk_level = "Medium"

    else:
        risk_level = "High"

    return risk_level, warnings