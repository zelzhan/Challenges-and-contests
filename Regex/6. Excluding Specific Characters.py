Regex_Pattern = r'^\D[^aeiou][^bcDF][^s\r\n\t\f][^AEIOU][^\.,]$'	# Do not delete 'r'.
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
