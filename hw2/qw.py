def e_approx(n):
    temp = 1
    eSum = 1
    for i in range(1,n+1):
        eSum += 1/(temp*i)
        temp = temp*i
    return eSum
     
def factors(num):
    lst = []
    yield 1.0
    for i in range(1,int(num**1/2)+1):
        if(num % i == 0):
            lst.append(i)   
    for i in range(len(lst)-1,-1,-1):
        yield num/lst[i]
    
    print(lst)
def split_parity(lst):
    pos = 0 
    for i in range(len(lst)):
        if(i%2 == 0):
            lst[i],lst[pos] = lst[pos],lst[i]
            pos+=1
    return lst

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
	

def main():
    lst = [1,2,3,4]
    print(split_parity(lst))
main()
