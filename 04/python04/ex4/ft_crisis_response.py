def crisis_handler(filename, mode="r"):
    if filename == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'")
    print("...")
    try:
        with open(filename, mode) as vault:
            content = vault.read().strip()
            print(f"SUCCESS: Archive recovered - \"{content}\"")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly - {e}")
        print("STATUS: Crisis handled, diagnostic logged")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
