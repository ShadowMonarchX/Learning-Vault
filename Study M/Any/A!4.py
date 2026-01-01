def rabin_karp(text, pattern):
    d = 256  # number of characters in the input alphabet
    q = 101  # a prime number for hash calculation

    n = len(text)
    m = len(pattern)
    h_pattern = 0  # hash value for pattern
    h_text = 0  # hash value for text

    # Calculate the hash value of the pattern and the first window of text
    for i in range(m):
        h_pattern = (d * h_pattern + ord(pattern[i])) % q
        h_text = (d * h_text + ord(text[i])) % q

    # Slide the pattern over the text one by one
    for i in range(n - m + 1):
        # Check if hash values match
        if h_pattern == h_text:
            # Check character by character for a match
            if text[i:i + m] == pattern:
                print("Pattern found at index", i)

        # Calculate hash value for next window of text
        if i < n - m:
            h_text = (d * (h_text - ord(text[i]) * pow(d, m - 1, q)) + ord(text[i + m])) % q
            if h_text < 0:
                h_text += q

# Example usage:
text = "AABAACAADAABAABA"
pattern = "AABA"
rabin_karp(text, pattern)
