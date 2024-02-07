def generate_triangle_pattern(n):
    #external loop runs for n times 
    #it determines the number of rows
    # i == row number
    #(since i starts from 1, we need to add 1 the upper range)
    for i in range(1, n+1):
        #starting_val determines the first value in the first column of each row
        #increments by 2,each iteration/each row, starting from 2 in the first row.
        start_val= (i)*2
        #internal loop runs/needs to run for i times:
            #It runs for the number of times the external loop is running currently 
            #for example, if it's the 2nd iteration for the external(which means in the second row),
            #it will also run for exactly 2 times
            #this is because this determines the number of value(s)/column(s) in each row
        #(since the internal loop starts from 1, we need to add 1 the upper limit)
        for k in range(1, i+1):
            print(str(start_val*k),' ',end='')
        print()

import random as rn        
for x in range(3):
    #for sake of demonstration,the upper limit has been set to 10,code works for any natural number
    n= rn.randint(0,10)
    print("For n:",n)
    generate_triangle_pattern(n)
    print()
