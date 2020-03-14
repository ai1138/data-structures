def findChange(lst01):
    left = 0
    right = len(lst01)-1
    finder = False
    while(not(left > right) or not(right < left)):
        mid = (left + right)//2
        if(lst01[mid] == 1):
            if(lst01[mid-1] == 0):
                return mid
            else:
                right = mid 
        else:
            left = mid 
