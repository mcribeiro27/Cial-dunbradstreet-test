import sys
from lib.phone import FindUrls

urls = sys.stdin.readlines()
ur = [url.strip() for url in urls if url.strip() != ""]
for u in ur:
    print(u)
    file = FindUrls.json(u)
    print(file)
