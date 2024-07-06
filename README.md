# DO

DO is a Python script designed to brute-force subdomains for a specified domain using custom wordlists. It utilizes the requests library to check HTTP status codes for each subdomain.

## Usage

1. Clone the repository:
   ```
   git clone https://codeberg.org/UmmIt/DO
   ```

2. Running the Scanner

    To scan subdomains for a domain, run the script `main.py` with the `--site` argument followed by the target domain. For example:

    ```
    python main.py --site google.com
    ```

## Wordlist

The script uses wordlists stored in the `./wordlists` directory. Each text file in this directory contains a list of subdomains to be scanned.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
