def mergeOverlappingIntervals(intervals):
    intervals.sort()
    pointer = 0
    while pointer < len(intervals)-1:
        first_pair, second_pair = intervals[pointer], intervals[pointer+1]
        if first_pair[1]>=second_pair[0]:
            if first_pair[1] >= second_pair[1]:
                pass
            else:
                intervals[pointer] = [first_pair[0], second_pair[1]]
            del intervals[pointer+1]
        else:
            pointer += 1   
        

    return intervals
		