import argparse
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from port_scanner import run_scanner
from brute_forcer import ssh_bruteforce, http_bruteforce
from service_detector import grab_banner
try:
    # local menu launcher (added separately)
    from menu import main as menu_main
except Exception:
    menu_main = None

def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Scan Command
    scan_parser = subparsers.add_parser("scan", help="Scan ports")
    scan_parser.add_argument("--target", required=True, help="Target IP/Hostname")
    scan_parser.add_argument("--ports", default="21,22,80,443", help="Comma-separated ports")
    scan_parser.add_argument("--threads", type=int, default=10, help="Number of threads")

    # Brute Command
    brute_parser = subparsers.add_parser("brute", help="Brute-force credentials")
    brute_parser.add_argument("--service", choices=["ssh", "http"], required=True)
    brute_parser.add_argument("--target", required=True)
    brute_parser.add_argument("--user", default="admin")
    brute_parser.add_argument("--wordlist", required=True, help="Path to password file")
    brute_parser.add_argument("--path", default="/", help="HTTP path (for http only)")

    # Detect Command
    detect_parser = subparsers.add_parser("detect", help="Detect service banner")
    detect_parser.add_argument("--target", required=True)
    detect_parser.add_argument("--port", type=int, required=True)

    args = parser.parse_args()

    if args.command == "scan":
        ports = [int(p.strip()) for p in args.ports.split(",") if p.strip()]
        open_ports = run_scanner(args.target, ports=ports, threads=args.threads)
        print(f"[+] Open ports on {args.target}: {open_ports}")

    elif args.command == "brute":
        if args.service == "ssh":
            ssh_bruteforce(args.target, args.user, args.wordlist)
        elif args.service == "http":
            http_bruteforce(args.target, args.user, args.wordlist, args.path)

    elif args.command == "detect":
        banner = grab_banner(args.target, args.port)
        print(f"[+] Banner on {args.target}:{args.port} -> {banner}")
    else:
        parser.print_help()
        return 1

if __name__ == "__main__":
    # If no args provided, open the interactive menu if available.
    if len(sys.argv) == 1 and menu_main:
        sys.exit(menu_main() or 0)
    main()