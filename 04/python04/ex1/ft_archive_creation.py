def create_new_archive():
    filename = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"Initializing new storage unit: {filename}")
    try:
        vault = open(filename, "w")
        print("Storage unit created successfully...")
        entries = [
            "[ENTRY 001] New quantum algorithm discovered",
            "[ENTRY 002] Efficiency increased by 347%",
            "[ENTRY 003] Archived by Data Archivist trainee"
        ]
        print("Inscribing preservation data...")
        for entry in entries:
            vault.write(entry + "\n")
            print(entry)
        vault.close()
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
    except Exception as e:
        print(f"CRITICAL ERROR: Failed to initialize storage unit. {e}")


if __name__ == "__main__":
    create_new_archive()
