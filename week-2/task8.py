first_string = input().strip()
second_string = input().strip()

if sorted(first_string) == sorted(second_string):
    print("YES")
else:
    print("NO")