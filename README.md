# Penetration_testing_toolkit

## COMPANY: CODTECH IT SOLUTIONS

## NAME: GOURAHARI SAHOO

## INTERN ID: CTIS9570

## DOMAIN: CYBER SECURITY & ETHICAL HACKING

## DURATION: 6 WEEKS

## MENTOR: NEELA SANTOSH KUMAR

# Penetration_testing_toolkit

A lightweight penetration testing toolkit for basic network scanning, service banner detection, and credential brute forcing.

## Features

- Port scanning using TCP connect checks
- Service banner grabbing for remote hosts
- SSH brute force attack tool
- HTTP Basic Auth brute forcing tool
- Interactive menu launcher for easy access to tools

## Requirements

- Python 3.8+
- `paramiko`
- `requests`

## Installation

1. Create and activate a Python virtual environment in `spk_toolkit`:

```powershell
python -m venv .venv
activate the virtual environment.

# .\.venv\Scripts\Activate.ps1 for window
```

2. Install the required packages:

```powershell
python -m pip install -r requirements.txt
```

## Usage

### Interactive menu launcher

Run the toolbox menu to choose tools interactively:

```powershell
python menu.py
```

### Command-line toolkit

Run the main toolkit script with subcommands:

```powershell
python spk_toolkit.py scan --target 192.168.1.10 --ports 22,80,443 --threads 10
```

```powershell
python spk_toolkit.py brute --service ssh --target 192.168.1.10 --user admin --wordlist passwords.txt
```

```powershell
python spk_toolkit.py brute --service http --target example.com --user admin --wordlist passwords.txt --path /login
```

```powershell
python spk_toolkit.py detect --target 192.168.1.10 --port 22
```

### Commands

- `scan`
  - `--target`: target IP or hostname
  - `--ports`: comma-separated list of ports (default: `21,22,80,443`)
  - `--threads`: number of worker threads (default: `10`)

- `brute`
  - `--service`: `ssh` or `http`
  - `--target`: target host or URL
  - `--user`: username to test (default: `admin`)
  - `--wordlist`: path to a password list file
  - `--path`: HTTP path for HTTP brute force (default: `/`)

- `detect`
  - `--target`: target IP or hostname
  - `--port`: port number for banner grabbing

## Notes

- `ssh` brute force requires a valid `paramiko` installation.
- `http` brute force uses HTTP Basic Auth via `requests`.
- Running the toolkit from the repository root is supported by the included path handling in `spk_toolkit.py`.

## Example

```powershell
python spk_toolkit.py scan --target 127.0.0.1 --ports 22,80
python spk_toolkit.py detect --target 127.0.0.1 --port 22
python spk_toolkit.py brute --service http --target example.com --user admin --wordlist wordlist.txt --path /login
```
