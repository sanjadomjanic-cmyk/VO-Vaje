import zipfile
import argparse
import os

def crack_zip(zip_path, wordlist_path):
    if not os.path.exists(zip_path):
        print(f"[-] ZIP file not found: {zip_path}")
        return

    if not os.path.exists(wordlist_path):
        print(f"[-] Wordlist not found: {wordlist_path}")
        return

    try:
        with zipfile.ZipFile(zip_path) as zf:
            with open(wordlist_path, "r", encoding="latin-1") as f:
                for i, line in enumerate(f, 1):
                    password = line.strip()
                    try:
                        zf.extractall(pwd=password.encode())
                        print(f"\n[+] Password found: {password}")
                        print(f"[+] Extracted to current directory")
                        return password
                    except:
                        if i % 50 == 0:
                            print(f"[*] Tried {i} passwords...")

        print("\n[-] Password not found in wordlist")

    except zipfile.BadZipFile:
        print("[-] Invalid ZIP file")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple ZIP Password Cracker")
    parser.add_argument("-z", "--zip", required=True, help="Path to ZIP file")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist")

    args = parser.parse_args()

    crack_zip(args.zip, args.wordlist)