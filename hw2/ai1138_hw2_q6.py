def two_sums(srt_lst,target):
    left = 0
    right = len(srt_lst)-1
    while(not(left > right) or not(right < left)):
        if(left == right):
            return none
        if(srt_lst[left] + srt_lst[right] == target):
            return (left,right)
        elif(srt_lst[left] + srt_lst[right] > target):
            right-=1
        elif(srt_lst[left] + srt_lst[right] < target):
            left+=1
    return none
