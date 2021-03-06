#O (n) space and time
def spiralTraverse(array):

    start_row, start_col = 0, 0
    end_row, end_col = len(array)-1, len(array[0])-1
    output = []
    
    while start_row <= end_row and start_col <= end_col:

        for col in range(start_col, end_col +1): 
            output.append(array[start_row][col])
        for row in range(start_row+1, end_row +1):
            output.append(array[row][end_col]) 
        for col in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break
            output.append(array[end_row][col])
        for row in reversed(range(start_row+1,end_row)):
            if start_col == end_col:
                break
            output.append(array[row][start_col])
        
        end_row-=1
        end_col-=1
        start_row += 1
        start_col +=1

        
    return output