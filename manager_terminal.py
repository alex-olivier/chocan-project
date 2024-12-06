from input_validation import prompt_until_valid


# TODO: Fix manager_terminal() to call the correct functions
def manager_terminal():
        print("\n---------------------------------------------------")
        print("Manager Terminal")
        print("---------------------------------------------------")
        print("Manager Terminal:")
        print("  1. Report Management")
        print("  2. Generate EFT Data")
        print("  3. Generate Provider Directory")
        print("  4. Exit")
        choice = prompt_until_valid(
            r'^[1-4]$',
            "\nEnter your choice: ",
            "Invalid choice. Please try again."
        )
        if choice == "1":
            pass  # Report Management
        elif choice == "2":
            pass  # Generate EFT Data
        elif choice == "3":
            pass  # Generate Provider Directory
        elif choice == "4":
            print("Exiting... Goodbye!")
        else:
            print("Error occurred. Exiting...")