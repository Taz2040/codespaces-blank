def box_num_to_color(n,m):
    #since arm length will be equal, it will be limited 
    #by either the lower number of row or columns
    #if both are equal, it doesn't matter, which is considered the length
    if n>m:
        length=m
    else:
        length=n
    #the lengths that is considered, is the total vertical/horizontal length
    #   the length of each arm will length divided by 2,rounded down
    #the total number of boxes are the (number of arms)*(arm length), plus the one box in the center
    #(there are 8 arms)
    box_num=((length//2)*8)+1
    print("Boxes that need to be colored:",box_num)
    
n=int(input("The Number of rows:"))
m=int(input("The Number of column:"))
box_num_to_color(n,m)

