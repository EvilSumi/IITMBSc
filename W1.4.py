# Sample inputs
word1 = "Wingardium"
word2 = "Leviyosa"
word3 = "Silver"
sentence = "Learning python is fun"
n1 = 6
n2 = 4

# String manipulations
output1 = word1 + " " + word2  # Join words with space
output2 = word1[:4] + "-" + word2[-4:]  # Join first 4 and last 4 letters with hyphen
output3 = word3 + " " + str(n1)  # Join word and number with space
output4 = "-" * 50  # Repeat hyphen 50 times
output5 = "-" * n2  # Repeat hyphen based on n2
output6 = str(n1) * n2  # Repeat number n1, n2 times
are_all_words_equal = word1 == word2 == word3  # Check if all words are equal
is_word1_comes_before_other_two = word1 < word2 and word1 < word3  # Check alphabetical order (assuming unique words)
has_h = "h" in word1.lower()  # Check for lowercase or uppercase 'h'
ends_with_a = word1.lower().endswith("a")  # Check if lowercase word ends with 'a'
has_the_word_python = "python" in sentence.lower()  # Check if sentence contains lowercase "python"

# Print outputs
print(f"output1: {output1}")
print(f"output2: {output2}")
print(f"output3: {output3}")
print(f"output4: {output4}")
print(f"output5: {output5}")
print(f"output6: {output6}")
print(f"All words equal: {are_all_words_equal}")
print(f"Word1 comes before: {is_word1_comes_before_other_two}")
print(f"Word1 has 'h': {has_h}")
print(f"Word1 ends with 'a': {ends_with_a}")
print(f"Sentence has 'python': {has_the_word_python}")
