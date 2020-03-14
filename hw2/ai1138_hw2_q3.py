def factors(num):
    yield 1.0
    for i in range(int(num**1/2) + 1,0,-1):
        if(num % i == 0):
            yield num/i
   
   
