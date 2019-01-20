Regex_Pattern = r'^(Mr\.|Ms\.|Dr\.|Er\.|Mrs\.)[A-Za-z]+$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
