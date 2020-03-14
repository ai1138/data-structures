def e_approx(n):
    temp = 1
    eSum = 1
    for i in range(1,n+1):
        eSum += 1/(temp*i)
        temp = temp*i
    return eSum
