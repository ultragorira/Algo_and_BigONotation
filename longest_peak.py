#O(n) Time O(1) Space
def longestPeak(array):
    if len(array) < 3:
        return 0
    longest_peak = 0
    i = 1
    
    while i < len(array)-1:
        isPeak = array[i-1]<array[i] and array[i]>array[i+1]
        if not isPeak:
            i+=1
            continue
        leftidx = i-2
        while leftidx >=0 and array[leftidx] < array[leftidx+1]:
            leftidx-=1
        rightidx = i+2
        while rightidx <len(array) and array[rightidx] < array[rightidx-1]:
            rightidx +=1
        curr = rightidx - leftidx -1
        longest_peak = max(longest_peak, curr)
        i = rightidx #restart from the right of the peak. We only recheck twice values on left
        
    return longest_peak