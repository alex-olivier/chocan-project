from database_manager import DatabaseManager
from report_manager import ReportManager
from service_manager import ServiceManager
from utils import prompt_until_valid
from constants import DATABASE_URL, ACCOUNT_NUM_LEN


class ManagerTerminal:
    def __init__(self, db_url=None):
        self.db_manager = DatabaseManager(db_url or DATABASE_URL)

    def main_menu(self):
            print("\n---------------------------------------------------")
            print("Manager Terminal")
            print("---------------------------------------------------")
            print("Manager Terminal:")
            print("  1. Report Management")
            print("  2. Generate Provider Directory")
            print("  3. Exit")

            choice = prompt_until_valid(
                r'^[1-4]$',
                "\n>> Enter your choice: ",
                "Invalid choice. Please try again."
            )
            if choice == "1":  # Report Management
                self.report_management()
            elif choice == "2":  # Generate Provider Directory
                ServiceManager().view_services
                pass
            elif choice == "3":
                print("Exiting... Goodbye!")
            else:
                print("Error occurred. Exiting...")

    def report_management(self):
            report_manager = ReportManager(self.db_manager)
            print("\n---------------------------------------------------")
            print("Manager Terminal > Report Management")
            print("---------------------------------------------------")
            print("Manager Terminal:")
            print("  Report Management:")
            print("    1. Main Accounting Procedure")
            print("    2. Generate Summary Report")
            print("    3. Generate Member Report")
            print("    4. Generate Provider Report")
            print("    5. Generate EFT Data")
            print("    6. Exit")

            choice = prompt_until_valid(
                r'^[1-4]$',
                "\n>> Enter your choice: ",
                "Invalid choice. Please try again."
            )
            if choice == "1":  # Main Accounting Procedure
                print("\nRunning main acccounting procedure...")
                report_manager.main_accounting_procedure()
            elif choice == "2":  # Generate Summary Report
                print("\nGenerating summary report...")
                report_manager.generate_summary_report()
            elif choice == "3":  # Gemerate Member Report
                print("\nGenerating member report...")
                member_number = prompt_until_valid(
                    rf'^\d{{{ACCOUNT_NUM_LEN}}}$',
                    "\n>> Enter member number: ",
                    "Member number must be 9 digits."
                )
                report_manager.generate_member_report(member_number)
            elif choice == "4":  # Generate Provider Report
                print("\nGenerating provider report...")
                provider_number = prompt_until_valid(
                    rf'^\d{{{ACCOUNT_NUM_LEN}}}$',
                    "\n>> Enter provider number: ",
                    "Provider number must be 9 digits."
                )
                report_manager.generate_provider_report(provider_number)
            elif choice == "5":  # Generate EFT Data
                report_manager.generate_eft_data()
            elif choice == "6":
                print("Exiting... Goodbye!")
            else:
                print("Error occurred. Exiting...")

    def run(self):
            self.main_menu()