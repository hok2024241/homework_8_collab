def index_power(numnbers, n):
    if n < len(numnbers):
        return numnbers[n] ** n
    return -1
print(index_power([1, 2, 3, 4], 2)) 
print(index_power([1, 3, 10, 100], 3))   
