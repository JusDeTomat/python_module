def recover_ancient_data():
    filename = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {filename}")
    try:
        vault = open(filename, "r")
        print("Connection established...\n")
        data = vault.read()
        print("RECOVERED DATA:")
        print(data)
        vault.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except Exception:
        print("ERROR: Unauthorized access or data corruption detected.")


if __name__ == "__main__":
    recover_ancient_data()
