# pkgExtractor
## A tool to extract links for retail packages from a PS4's entitlement.db file.

Only supports games which have their .pkg links in .json, not .xml *(for now)*

The database **must** be called "entitlement.db" and put in the folder the script is ran in, and it will generate a file called links.txt in this folder.

This script requires the requests library (as is listed in the requirements.txt file).

Enjoy :)