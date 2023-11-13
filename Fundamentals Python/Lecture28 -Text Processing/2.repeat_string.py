text = input().split()

repeated = [txt * len(txt) for txt in text]

print("".join(repeated))