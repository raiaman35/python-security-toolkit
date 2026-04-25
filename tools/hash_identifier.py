import hashlib
import re
import os
from colorama import Fore, Style, init

init(autoreset=True)

def identify_hash(hash_string):
    hash_string = hash_string.strip()
    length = len(hash_string)

    if not re.match(r'^[a-fA-F0-9]+$', hash_string):
        return f"{Fore.RED}Not a valid hash — contains non-hex characters"

    types = {
        32:  "MD5",
        40:  "SHA1",
        56:  "SHA224",
        64:  "SHA256",
        96:  "SHA384",
        128: "SHA512",
    }

    result = types.get(length, f"Unknown — {length} chars")
    print(f"\n{Fore.CYAN}Hash:   {Style.BRIGHT}{hash_string}")
    print(f"{Fore.GREEN}Type:   {Style.BRIGHT}{result}")
    print(f"{Fore.YELLOW}Length: {length} characters")
    return result

def hash_a_file(filepath):
    if not os.path.exists(filepath):
        print(f"{Fore.RED}File not found: {filepath}")
        return

    with open(filepath, 'rb') as f:
        data = f.read()

    md5    = hashlib.md5(data).hexdigest()
    sha1   = hashlib.sha1(data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()

    print(f"\n{Fore.CYAN}File:   {filepath}")
    print(f"{Fore.GREEN}MD5:    {md5}")
    print(f"{Fore.GREEN}SHA1:   {sha1}")
    print(f"{Fore.GREEN}SHA256: {sha256}")
    return {"MD5": md5, "SHA1": sha1, "SHA256": sha256}

def run():
    print(f"\n{Fore.CYAN}{'='*45}")
    print(f"{Fore.CYAN}        HASH IDENTIFIER")
    print(f"{Fore.CYAN}{'='*45}")
    print("1. Identify a hash type")
    print("2. Hash a file")
    choice = input("\nChoice: ").strip()

    if choice == "1":
        h = input("Enter hash: ").strip()
        identify_hash(h)
    elif choice == "2":
        path = input("Enter file path: ").strip()
        hash_a_file(path)
    else:
        print(f"{Fore.RED}Invalid choice")