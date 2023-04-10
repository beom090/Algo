def solution(my_str, n):
    answer = []
    my_str = list(my_str)
    
    iter = len(my_str) // n
    
    rest = len(my_str) % n
    
    for idx_n in range(iter):
        mylist=[]
        
        for idx_str in range(idx_n * n,(idx_n + 1) * n):
            
            mylist.append(my_str[idx_str])
        answer.append(''.join(mylist))
        
    if rest != 0:
        mylist = my_str[iter * n:]
        answer.append(''.join(mylist))
                          
    return answer