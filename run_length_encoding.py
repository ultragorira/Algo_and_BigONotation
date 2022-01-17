def encoding(string):

        
    cnt = 1
    encoding = []

    for i in range(1, len(string)):
        curr_char = string[i]
        prev_char = string[i - 1]

        if curr_char != prev_char or cnt==9:
            encoding.append(str(cnt)+prev_char)
            cnt = 0
        cnt +=1

    encoding.append(str(cnt)+string[-1])

    
    print(''.join(encoding))




encoding('aA')

