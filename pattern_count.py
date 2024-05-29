def pattern_count(text, pattern):
    len_text = len(text)
    len_pattern = len(pattern)
    
    count = 0
    
    for i in range(len_text - len_pattern + 1):
        # Bandingkan substring teks dengan pola
        if text[i:i + len_pattern] == pattern:
            count += 1
    
    return count


text = input("Masukan Teks: ")
pattern = input("Masukan Pattern: ")

result = pattern_count(text, pattern)
print(result)
