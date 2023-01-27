#!/usr/bin/env python3

import os
import json
from templates import login_page


# print('Content-Type: text/plain')  # let browser know to expect plain text
# print()
# print(os.environ)

print('Content-Type: application/json')
print()
print(json.dumps(dict(os.environ), indent=2))

# print('Content-Type: text/html')
# print()
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

# print('Content-Type: text/html')
# print()
# print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")
