## Features to Implement

- [ ] **Multi-threading**: Implement concurrent scanning to speed up subdomain brute-forcing.
- [ ] **Proxy Support**: Integrate proxy server support for anonymous connection.
- [ ] **User-Agent Rotation**: Use different user-agents to mimic a browser and enhance anonymity.
- [ ] **Download Wordlists**: Enable downloading wordlists from a GitHub repository in raw format.
  - [ ] **Progress Bar**: Display download progress with file size (y/n).
  - [ ] **Speed Indicator**: Show download speed in bytes (millisecond)
- [ ] **Custom Wordlist Path**: Allow users to specify a custom path for the wordlist using `--wordlist` argument.
- [ ] **IP and Host Information**: Fetch and display host IP and additional information using IPify API.
- [ ] **Cloudflare Detection**: Implement detection to identify if the domain is protected by Cloudflare.
- [ ] Log Results: Implement logging to save scan results to files within a log directory.
  - [ ] File Naming: Log files format into yyyy-mm-dd-hh-mm-ss-number.log.
- [ ] Verify if the domain is active
