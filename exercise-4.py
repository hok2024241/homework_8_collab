def chunking_by(numbers, chunck):
    inside_list = []
    chunked_list = []
    
    for i in numbers:
        inside_list.append(i)
        if len(inside_list) == chunck:
            chunked_list.append(inside_list)
            inside_list = []

    if inside_list != []:
        chunked_list.append(inside_list)

    return chunked_list

# Example Test
print(chunking_by([5, 4, 7, 3, 4, 5, 4], 3))
