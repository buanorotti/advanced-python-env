text = input().strip()

matches = 0
for index in range(len(text) - 4):
    if text[index:index + 5] == ">>-->":
        matches += 1
    if text[index:index + 5] == "<--<<":
        matches += 1

print(matches)

