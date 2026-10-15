# 1. Immutable Approved Models (Tuple)
approved_models = ("MacBook Pro", "Dell XPS", "ThinkPad")

# 2. Dynamic Device Storage (List)
device_inventory = []

# 3. Persistent Menu (While Loop)
while True:
    print("\n--- IT Procurement System ---")
    print("1: Add")
    print("2: Remove")
    print("3: View")
    print("4: Exit")

    choice = input("Choose an action (1-4): ").strip()

    # 4. Add a Device (with Approved Model Validation)
    if choice == "1":
        print("Approved models:", ", ".join(approved_models))
        device_name = input("Enter a device name to add: ").strip()

        if device_name in approved_models:
            device_inventory.append(device_name)
            print(f"Success: {device_name} added to inventory.")
        else:
            print("Error: Device model not approved for company use.")

    # 5. Safely Remove a Device
    elif choice == "2":
        device_to_remove = input("Enter a device name to remove: ").strip()

        if device_to_remove in device_inventory:
            device_inventory.remove(device_to_remove)
            print(f"Success: {device_to_remove} removed from inventory.")
        else:
            print("Device not found.")

    # 4. View the Current Inventory
    elif choice == "3":
        print("Current device inventory:", device_inventory)

    # Exit the Program
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")