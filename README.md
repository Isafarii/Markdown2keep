# Markdown2keep

A Python script for converting Markdown files to Google Keep notes.

## Overview

This script automates the process of converting Markdown (.md) files into Google Keep notes. It extracts content from each Markdown file, converts it to HTML using the markdown2 library, and creates a corresponding note in Google Keep.

## Features

- **Google Keep Integration:** Automates the creation of notes in Google Keep.
- **User Interaction:** Prompts the user to place the cursor in Google Keep before initiating the conversion.

## Prerequisites

- Python 3.x
- Having a folder of (markdown .md) files
## Usage

1. Place your Markdown files in the same directory as the script.
2. Run the script.
3. Follow on-screen instructions to place the cursor in Google Keep. Click on 'take a note' and press backspace on that line.
4. The script will create notes for each Markdown file in Google Keep. May take a long time for many files; roughly 10 conversions per minute.

## Configuration

- Adjust the sleep duration between note creations in the script (`time.sleep(seconds)`) based on your needs.

## Troubleshooting
- If you encounter issues with Google Keep connectivity, consider increasing the sleep duration.


Feel free to reach out with any questions or suggestions.
