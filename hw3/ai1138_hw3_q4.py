def remove_all(lst, value):
    if value not in lst:
        raise ValueError("Value not present")
    for i in range(len(lst)):



def main():
    lst = [2,2,5,64,3,2]
    remove_all(lst,2)
    print(lst)
main()
