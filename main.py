import requests
import argparse
import os
import signal
import sys

# ANSI color escape codes
class colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DARK_RED = '\033[31m'
    GREY = '\033[90m'
    BLUE = '\033[94m'
    END = '\033[0m'

# Function to read subdomains from a wordlist file
def read_wordlist(filename):
    with open(filename, 'r') as f:
        subdomains = f.read().splitlines()
    return subdomains

# Function to check HTTP and HTTPS status code
def check_subdomain(domain, subdomain):
    protocols = ['http', 'https']
    found = False
    for protocol in protocols:
        url = f"{protocol}://{subdomain}.{domain}"
        sys.stdout.write(colors.BLUE + f"\rTrying {url} ..." + colors.END)
        sys.stdout.flush()  # Flush the buffer to ensure immediate display
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                sys.stdout.write('\r' + ' ' * (len(f"Trying {url} ...")))  # Clear the line
                print(colors.GREEN + f"\r[+] Found new: {subdomain}.{domain}" + colors.END)  # Print success message
                found = True
                break
        except requests.ConnectionError:
            pass
    
    if not found:
        sys.stdout.write('\r' + ' ' * (len(f"Trying {url}...")))  # Clear the line
        print(colors.YELLOW + f"\r[-] Subdomain Not found: {subdomain}.{domain}" + colors.END) # Print failed message

# Main function
def main():
    parser = argparse.ArgumentParser(description="Domain subdomain scanner")
    parser.add_argument('--site', dest='domain', required=True, help='Specify the domain to scan against')
    args = parser.parse_args()

    print(f"{colors.BLUE}Target information{colors.END}:")
    print(f"{colors.BLUE}Target Domain{colors.END}: {args.domain}\n")

    print(colors.YELLOW + "[!] Running scanning ..." + colors.END)
    
    # Signal handler for Ctrl+C
    def signal_handler(sig, frame):
        print(f"\n{colors.YELLOW}[!] Exiting the program...{colors.END}")
        sys.exit(0)

    # Register signal handler
    signal.signal(signal.SIGINT, signal_handler)

    wordlist_dir = './wordlists/'  # Directory where wordlists are stored
    wordlist_files = os.listdir(wordlist_dir)

    for filename in wordlist_files:
        if filename.endswith('.txt'):  # Assuming wordlists have .txt extension
            print(f"\nUsing wordlist {filename}...")
            wordlist_path = os.path.join(wordlist_dir, filename)
            subdomains = read_wordlist(wordlist_path)
            for subdomain in subdomains:
                check_subdomain(args.domain, subdomain)

if __name__ == "__main__":
    main()
