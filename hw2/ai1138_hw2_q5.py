def split_parity(lst):
    pos = 0
    if(len(lst) == 1):
        return lst
    for i in range(len(lst)):
        if(i%2 == 0):
            lst[i],lst[pos] = lst[pos],lst[i]
            pos+=1
    return lst
