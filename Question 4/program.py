def generate_triangle_pattern(n):
    #external loop runs for i times (which is == n times)
    #It determines the number of rows
    for i in range(1, n+1):
        #starting_val determines the first value in the first column of each row
        start_val= (i)*2
        #internal loop runs/needs to run for i times
            #due to difference between external and internal loop starting values we need to add 1 to upper range
            #since the internal loop starts from 1, we need to anothr 1 
        for k in range(1, i+1):
            print(str(start_val*k),' ',end='')
        print()
        
generate_triangle_pattern(5)