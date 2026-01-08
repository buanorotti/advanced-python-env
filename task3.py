string = input().strip()
sub = input().strip()
count = 0
sub_len = len(sub)
for i in range(len(string) - sub_len + 1):
    if string[i:i + sub_len] == sub:
        count += 1
print(count)