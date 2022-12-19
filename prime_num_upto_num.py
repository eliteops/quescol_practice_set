num = int(input('Enter num to find out prime numbers ?'))
for iter_num in range(1, num+1):                            # num+1 because because range function runs 1 less , so num-1
                                                            # if range(25), then it will run till 24 
                                                            
    flag = 0                                                # flag,  variable is used to verify if prime 
                                                            # then flag = 1 otherwise flag = 0 
                                                            
    for iter_div in range(2, iter_num//2+1):                # divisor will be half of the iter_num, 
    
                                                            # if iter_num = 23 then iter_div = 11+1 = 12  because range consider 1 less.  
        if iter_num % iter_div == 0:                        # if iter_num completely divisible from that iter_div and remainder = 0
        
            flag = 1                                        # then flag will be assign 1.
            
            break                                           # and break is used to go for next iter_num.
        
    if flag == 0:                                           # if iter_num is not divisible from any num then print that
        print(iter_num, end = ' ')
