# Unfollowers Checker

## Description
The Instagram Unfollowers Checker is a Python script that helps you identify users on Instagram who are not following you back. It does so by extracting your followers and following lists from exported HTML files and then comparing them to find the users who are not reciprocating your follow.

## Prerequisites
- Python 3.x
- BeautifulSoup library (install via `pip install beautifulsoup4`)

## How to Use
1. Export your Instagram followers and following lists as HTML files.
2. Place the exported HTML files in a zip archive for example purposes in the code mine is named `ayeitsshreya data.zip`.
3. Run the Python script `UnfollowersChecker.py`.
4. The script will extract usernames from the HTML files, compare them, and display the users who are not following you back.

## File Structure
- `unfollowers_checker.py`: Python script containing the main functionality to extract usernames and find unfollowers.
- `ayeitsshreya data.zip`: Zip archive containing exported HTML files of followers and following lists.
- `README.md`: This file providing information about the script.

## Usage
```bash
python UnfollowersChecker.py

Developed By Shreya Thyagaraju
