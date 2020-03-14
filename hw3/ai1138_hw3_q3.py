def find_duplicates(lst):
    x = []
    for i in range(len(lst)): 
        if lst[abs(lst[i])] >= 0: 
            lst[abs(lst[i])] = -lst[abs(lst[i])]
        if lst[abs(lst[i])] == 0:
            lst[abs(lst[i])] = lst[abs(lst[i])]
        else:
            x.append(abs(lst[i]))
    return x
