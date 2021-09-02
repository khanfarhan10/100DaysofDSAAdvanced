"""
cd "C - Sorting and Searching"
python frequency_counts.py

Try not to use libraries
Algorithm Efficiency : O(n)

Different Approach to remove if statement:
1. Insert All Chars as Frequency Nil (0)
2. Perform Linear Traversal with Incremental Frequency
3. Remove Nil Values from the Frequency Dict

# Filter dictionary by keeping elements whose values are more than 0
newDict = dict(filter(lambda elem: elem[1] > 0, old_dict.items()))
"""
input_text = "FarhanHaiKhan"

# APPROACH 1

char_frequency = {} # or dict

for each_letter in input_text:
    if each_letter in char_frequency:
        char_frequency[each_letter] = char_frequency[each_letter] + 1
    else:
        char_frequency[each_letter] = 1

sorted_char_frequency = {k: v for k, v in sorted(x.items(), key=lambda item: item[0])}
print(sorted_char_frequency)


print("----------------------")

# APPROACH 2

sample_space = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"

char_frequency = {} # or dict
for each_letter in sample_space:
    char_frequency[each_letter] = 0
# CONSTANT ORDER (O(2*26))


for each_letter in input_text:
    char_frequency[each_letter] = char_frequency[each_letter] + 1
# LINEAR ORDER (O(n))

filtered_char_frequency = dict(filter(lambda elem: elem[1] > 0, char_frequency.items()))
print(filtered_char_frequency)
# CONSTANT ORDER (O(2*26))