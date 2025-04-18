def reverse_ascending(numbers):
    result = []
    subseq = []

    for i, num in enumerate(numbers):
        if not subseq or num > subseq[-1]:
            subseq.append(num)
        else:
            result.extend(reversed(subseq))
            subseq = [num]

    if subseq:
        result.extend(reversed(subseq))
    
    return result



the_list = [5, 7, 10, 4, 2, 7, 8, 1, 3]
result = reverse_ascending(the_list)

print(result)
