def longest_substring_length(s):
    n = len(s)
    if n == 0:
        return 0

    max_length = 0
    start = 0
    char_set = set()

    for end in range(n):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage:
s = "abcabcbb"
print(longest_substring_length(s))  # Output: 3

