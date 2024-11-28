def list_statistics(numbers):
 
    sorted_numbers = sorted(numbers)

    min_value = min(numbers)
    max_value = max(numbers)
    
    average = sum(numbers) / len(numbers)
    
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    
    return (min_value, max_value, average, median)

result = list_statistics([1, 2, 3, 4, 5])
print(result)  # (1, 5, 3.0, 3)
