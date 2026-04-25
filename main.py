from colorama import Fore, Style, init
from tools import port_scanner, hash_identifier

init(autoreset=True)

def banner():
    print(f"""
{Fore.CYAN}{'='*50}
{Fore.CYAN}   ____  ____  _____   _____           _ _    _ _   
{Fore.CYAN}  / ___||  _ \|_   _| |_   _|__   ___ | | | _(_) |_ 
{Fore.CYAN}  \___ \| |_) | | |     | |/ _ \ / _ \| | |/ / | __|
{Fore.CYAN}   ___) |  __/  | |     | | (_) | (_) | |   <| | |_ 
{Fore.CYAN}  |____/|_|     |_|     |_|\___/ \___/|_|_|\_\_|\__|
{Fore.CYAN}
{Fore.CYAN}        Python Security Toolkit v1.0
{Fore.CYAN}
{Fore.CYAN}{'='*50}
""")

def main():
    banner()
    while True:
        print(f"\n{Fore.YELLOW}SELECT A TOOL:")
        print(f"  {Fore.GREEN}1{Style.RESET_ALL} — Port Scanner")
        print(f"  {Fore.GREEN}2{Style.RESET_ALL} — Hash Identifier")
        print(f"  {Fore.RED}3{Style.RESET_ALL} — Exit")

        choice = input(f"\n{Fore.CYAN}Enter choice: {Style.RESET_ALL}").strip()

        if choice == "1":
            port_scanner.run()
        elif choice == "2":
            hash_identifier.run()
        elif choice == "3":
            print(f"\n{Fore.CYAN}Goodbye.\n")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Try again.")

if __name__ == "__main__":
    main()