def pad_to_equal_length(strings):
    max_length = max(len(s) for s in strings)
    return [s + "_" * (max_length - len(s)) for s in strings]

if __name__ == "__main__":
    animals = ["cat", "dog", "monkey"]
    print(pad_to_equal_length(animals))
