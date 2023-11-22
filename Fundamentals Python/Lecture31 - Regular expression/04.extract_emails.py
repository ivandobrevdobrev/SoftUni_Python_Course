import re

text = input()

pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"  # обединяваме всичко в една голяма група ()
#[('s.miller@mit.edu', 's.miller', 'mit', '.edu'), ('j.hopking@york.ac.uk', 'j.hopking', 'york', '.uk')]
# принтна тюпъл с различните групи, като самия емаил е на индекс 0

extracted_emails = re.findall(pattern,text)

for emails in extracted_emails:
    print(emails[0])
# обикаляме тюпъла за да принтнем само имейла който ни трябва