text = input().strip()
arrow_total = 0

for pos in range(len(text) - 4):
    part = text[pos:pos + 5]
    if part == ">>-->" or part == "<--<<":
        arrow_total += 1

print(arrow_total)
