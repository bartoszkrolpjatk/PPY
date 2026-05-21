from collections import defaultdict
from pathlib import Path

with open(Path.home() / 'englishWords.txt') as f:
    list_of_words = [line.rstrip() for line in f]
    sorted_text_words = defaultdict(list)
    for word in list_of_words:
        sorted_text_words[''.join(sorted(word))].append(word)
    max_anagrams_list = max(sorted_text_words.values(), key=lambda words: len(words))
    print(max_anagrams_list)