## CTI IPv4 Indicator Info Script

This Python script retrieves and displays information about an IPv4 address via the AlienVault OTX (Open Threat Exchange) DirectConnect API.

## Overview

# Project Name: CTI IPv4 Indicator Info Script

Language: Python 3

Purpose: Query the OTX API to fetch the general section of an IPv4 indicator and print the formatted JSON response.

# Prerequisites

Python 3.6 or higher

requests library

OTX API key (obtainable from your AlienVault OTX account)

# Installation

Install dependencies

pip install requests

Configure your API key

Open cti_ioc.py

Replace the placeholder in API_KEY with your actual OTX API key:

API_KEY = "YOUR_OTX_API_KEY"

# Usage

Run the script:

python cti_ioc.py

When prompted, enter the IPv4 address you want to look up, for example:

Enter the IPV4 address: 1.1.1.1 ; 8.8.8.8

The script will print the general section returned by the OTX API in JSON format:

{
  "address": "1.1.1.1",
  "reputation": 0,
  "geo": {...},
  "malware": {...},
  "general": {...}
}

# Future Customization

Note: Currently, this script only supports IPv4 indicators. Future versions will include support for other indicator types (IPv6, domains, URLs, file hashes, etc.).

# Contributing

Contributions are welcome! Feel free to:

Open an issue to report bugs or suggest enhancements

Submit a pull request (fork the repo, create a branch, commit changes, and open a PR)

# License

This project is licensed under the MIT License. See the LICENSE file for details.
