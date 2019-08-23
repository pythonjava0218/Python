def search_list(v, a):
    n = len(v)
    result = []
    for i in range(n):
        if a == v[i]:
            result.append(i)
    return result

v = [17, 92, 18, 33, 58, 7, 33, 42]
 

print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))

