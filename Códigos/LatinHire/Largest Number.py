# Max variable intialized as zero
Max = 0 
# Matrix with predefined integer values
matrix = [[1,2,3,4,5,6,7,8],
        [9,10,11,12,13,14,15,16],
        [17,18,19,20,21,22,23,24],
        [25,26,27,5000,29,30,31,32],
        [33,34,35,36,37,38,39,40],
        [41,42,43,44,45,46,47,48]]
# for loops to search for the greater value
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        # Ask if the selected value in the matrix
        # is greater than the value stored in Max.
        if matrix[i][j] > Max:
            # Update the Max variable if  true.
            Max = matrix[i][j]
# Print the greatest number  
print(Max)