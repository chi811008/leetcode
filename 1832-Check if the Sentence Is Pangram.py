sentence = "g"
mapping = [0] * 26
for c in sentence:
    mapping[ord(c) - ord("a")] = 1
if all(mapping):
    print(True)
else:
    print(False)