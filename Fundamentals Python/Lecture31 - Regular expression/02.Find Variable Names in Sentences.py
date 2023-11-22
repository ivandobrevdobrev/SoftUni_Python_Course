import re

text = input()
pattern = r'\b_([A-Za-z0-9]+)\b'  # we need to start with underscore any letters and digits

matches = re.findall(pattern, text) # findall() will get only the group - what is in the ()

print(",".join(matches))
