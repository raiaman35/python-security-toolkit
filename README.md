
# Python Security Toolkit
A command-line security toolkit built in Python.


## Tools Included
**Port Scanner**
- Scans target host for open ports (1-1024)
- Identifies services on open ports (SSH, HTTP, FTP etc)
- Uses multithreading for fast concurrent scanning
- Exports results to text report

**Hash Identifier**
- Identifies hash type (MD5, SHA1, SHA256, SHA512)
- Generates MD5, SHA1, SHA256 hashes for any file
- Supports malware analysis workflows
## Libraries Used

| Library | Purpose |
|---------|---------|
| `socket` | Built-in Python library — handles TCP connections for port scanning |
| `threading` | Built-in Python library — runs multiple port scans simultaneously for speed |
| `hashlib` | Built-in Python library — generates MD5, SHA1, SHA256 file hashes |
| `re` | Built-in Python library — regex pattern matching for hash validation |
| `colorama` | Third-party — adds color to terminal output for better readability |
| `tabulate` | Third-party — formats scan results into clean readable tables |
| `os` | Built-in Python library — handles file path checking |




## Usage

```bash
python3 main.py
```
## Disclaimer
Port scanner must only be used on systems you own 
or have explicit written permission to test. 
Never scan external systems without authorization.