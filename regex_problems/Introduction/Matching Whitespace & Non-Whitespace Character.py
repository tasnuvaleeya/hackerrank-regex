import re
Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"

print(str(bool(re.search(Regex_Pattern, input()))).lower())