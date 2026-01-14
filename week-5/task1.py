from collections import Counter
import re

INPUT_FILE = "text.txt"
OUTPUT_FILE = "analysis.txt"

def normalize_text(text: str) -> list[str]:
    words = re.findall(r"\b\w+\b", text.lower())
    return words

def main() -> None:
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    line_count = len(lines)

    words_list: list[str] = []
    for line in lines:
        words_list += normalize_text(line)

    word_count = len(words_list)
    word_freq = Counter(words_list)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as result:
        result.write(f"Total lines: {line_count}\n")
        result.write(f"Total words: {word_count}\n")
        result.write("\nWord frequency:\n")

        for word, count in word_freq.most_common():
            result.write(f"{word}: {count}\n")

    print(f"Analysis completed. Data saved to '{OUTPUT_FILE}'")

if __name__ == "__main__":
    main()
