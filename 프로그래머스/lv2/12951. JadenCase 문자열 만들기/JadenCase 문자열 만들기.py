def solution(s:str)->str:
    return ' '.join([i[0].upper() + i[1:].lower() if i!= '' and i[0].isalpha else i.lower() for i in s.split(" ")])