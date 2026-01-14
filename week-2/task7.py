purchases = input().split()

frequency = {}
for product in purchases:
    frequency[product] = frequency.get(product, 0) + 1

print("Purchase frequency:")
for product, count in frequency.items():
    print(f"{product}: {count}")

most_popular_item = max(frequency, key=frequency.get)
print("\nMost popular item:", most_popular_item)

purchased_once = [product for product, count in frequency.items() if count == 1]
print("\nPurchased once:", " ".join(purchased_once))

print("\nSorted by frequency:")
for product, count in sorted(frequency.items(), key=lambda x: -x[1]):
    print(product, count)
