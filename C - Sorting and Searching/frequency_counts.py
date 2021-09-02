"""
cd "C - Sorting and Searching"
python frequency_counts.py

Try not to use libraries
Algorithm Efficiency : O(n)
"""

input_text = "FarhanHaiKhan"
sample_space = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"

char_frequency = {} # or dict

for each_letter in input_text:
    if each_letter in char_frequency:
        char_frequency[each_letter] = char_frequency[each_letter] + 1
    else:
        char_frequency[each_letter] = 1

sorted_char_frequency = {k: v for k, v in sorted(x.items(), key=lambda item: item[0])}
print(sorted_char_frequency)
