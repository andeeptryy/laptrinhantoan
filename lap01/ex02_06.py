input_str= input("Nhap X,Y: ")
dimensions= [int(x) for x in input_str.split(",")]
rouNum= dimensions[0]
colNum= dimensions[1]
multilist= [[0 for col in range(colNum)] for row in range(rouNum)]
for row in range(rouNum): 
    for col in range(colNum): 
        multilist[row][col]= row*col
print(multilist)