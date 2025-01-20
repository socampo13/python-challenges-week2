## 🗂️ **Challenge 1: collections**
##* Use the `collections.Counter` class to find the most common word in a list of words and its count.
##* Expected function: `most_common_word(words: list[str]) -> tuple[str, int]`.

from collections import Counter

def most_common_word(words: list[str]) -> tuple[str, int]:
    if not words:
        raise ValueError("List of words is empty")
    
    word_counts = Counter(words)
    most_common = word_counts.most_common(1)[0]
    return most_common

## Test
if __name__ == "__main__":
    words_list = ["computer", "keyboard", "mouse", "monitor", "chair", "headphones", "mousepad"]
    print(most_common_word(words_list))