def generate_audit_report(stdout_log: str):
    findings = []

    if "401" in stdout_log or "Missing required X-Gateway-Auth" in stdout_log:
        findings.append({
            "severity": "HIGH",
            "rule": "DPI-SEC-01: Unsigned API Request",
            "description": "Workload attempted to transact without including mandatory cryptographic header.",
            "remediation": "Include 'X-Gateway-Auth' signature generated via registered private key."
        })

    sensitive_keywords = ["private_key", "secret", "bearer", "password"]
    for kw in sensitive_keywords:
        if kw in stdout_log.lower():
            findings.append({
                "severity": "CRITICAL",
                "rule": "DPI-SEC-02: Secret Leak in Stdout",
                "description": f"Detected reference to sensitive key material ('{kw}') in console logs.",
                "remediation": "Mask or remove all authorization tokens and private keys from debug print statements."
            })
            break

    print("\n" + "=" * 50)
    print("       DPI COMPLIANCE & SECURITY AUDIT REPORT")
    print("=" * 50)
    if not findings:
        print("\n[+] STATUS: PASSED. No baseline security issues detected.")
    else:
        print(f"\n[-] STATUS: FAILED ({len(findings)} issues found)\n")
        for idx, f in enumerate(findings, 1):
            print(f"[{idx}] {f['severity']} - {f['rule']}")
            print(f"    Issue: {f['description']}")
            print(f"    Fix:   {f['remediation']}\n")
    print("=" * 50 + "\n")