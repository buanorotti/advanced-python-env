source = input().strip()
pattern = input().strip()

length = len(pattern)
all_rotations = set()

double_pattern = pattern + pattern
for pos in range(length):
    all_rotations.add(double_pattern[pos:pos + length])

result = 0
for start in range(len(source) - length + 1):
    if source[start:start + length] in all_rotations:
        result += 1

print(result)
