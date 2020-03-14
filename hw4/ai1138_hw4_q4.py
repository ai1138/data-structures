def list_min(lst, low, high):
    if (low == high):
        return lst[low]
    else:
        if lst[low] < lst[high]:
            return list_min(lst, low, high-1)
        elif lst[low] > lst[high]:
            return list_min(lst, low + 1, high)
        else:
            return list_min(lst, low, high-1)
