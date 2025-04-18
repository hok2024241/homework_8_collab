def replace_last(numbers):
    ...
    if len(numbers) <= 1:
        return numbers
    return [numbers[-1]] + numbers[:-1]
numbers = [4,1,2,3]
print(replace_last(numbers))
