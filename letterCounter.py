def count_and_sort_letters(user_input):
    letter_count = {}
    
    for char in user_input:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    
    sorted_letter_count = dict(sorted(letter_count.items(), key=lambda item: item[0].lower()))
    
    return sorted_letter_count

user_input = input("Input:")
result = count_and_sort_letters(user_input)

print(result)