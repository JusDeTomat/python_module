
def vault_security_operations():
    classified_source = "classified_data.txt"
    security_log = "security_report.txt"
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")
    try:
        with open(classified_source, "r") as vault_in:
            print("SECURE EXTRACTION:")
            content = vault_in.read()
            print(content)
        with open(security_log, "w") as vault_out:
            print("\nSECURE PRESERVATION:")
            entry = "[CLASSIFIED] New security protocols archived"
            vault_out.write(entry + "\n")
            print(entry)
        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except FileNotFoundError:
        print(f"\nERROR: Vault {classified_source} not found. Access denied.")
    except Exception as e:
        print(f"\nCRITICAL ERROR: Security breach during operation: {e}")


if __name__ == "__main__":
    vault_security_operations()
