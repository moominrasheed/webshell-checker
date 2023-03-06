#!/usr/bin/env python3

import argparse
import concurrent.futures
import os
import re
import signal
import sys
from termcolor import colored
from tqdm import tqdm

import requests


# Define the function to check URLs
def check_url(url):
    try:
        # Check if the URL exists
        r = requests.head(url, timeout=5)
        if r.status_code in [404, 403]:
            return colored(f"[SKIP] {url} - 404 Not Found", "yellow")
        else:
            # Check if the URL contains a shell signature
            r = requests.get(url, timeout=10)
            if re.search(r"Webshell|0byt3m1n1|IndoXploit|Shell|shell|wso|Upload Please|title", r.text, re.IGNORECASE):
                with open("done.txt", "a") as f:
                    f.write(url + "\n")
                return colored(f"[OK!] {url}", "green")
            else:
                return colored(f"[BAD] {url}", "yellow")
    except Exception as e:
        return colored(f"[ERROR] {url} - {e}", "red")


# Define the signal handler for SIGINT (Ctrl-C)
def sigint_handler(sig, frame):
    print("Exiting...")
    sys.exit(0)


# Parse the command line arguments
parser = argparse.ArgumentParser(description="Check a list of URLs for web shells.")
parser.add_argument("input_file", help="the input file containing the URLs")
args = parser.parse_args()

# Set up the signal handler for SIGINT (Ctrl-C)
signal.signal(signal.SIGINT, sigint_handler)

# Read the URLs from the input file
with open(args.input_file) as f:
    urls = [line.strip() for line in f if line.strip().startswith("http")]

# Check the URLs in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    for url in urls:
        futures.append(executor.submit(check_url, url))
    with tqdm(total=len(urls)) as progress_bar:
        for future, url in zip(concurrent.futures.as_completed(futures), urls):
            if future.result().startswith("[OK!]"):
                progress_bar.set_description(f"Checking: {url}  Status: OK")
            else:
                progress_bar.set_description(f"Checking: {url}  Status: {future.result()}")
            progress_bar.update(1)

# Print a final message
print("Done checking URLs.")
