def sort_mixed_array(arr):
    letters = [x for x in arr if isinstance(x, str)]
    numbers = [x for x in arr if isinstance(x, int)]
    
    letters.sort()
    numbers.sort()
    
    sorted_arr = letters + numbers
    return sorted_arr

array = [12, 9, 30, "A", "M", 99, 82, "J", "N", "B"]

sorted_array = sort_mixed_array(array)
print(sorted_array)
