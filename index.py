def swap_case(s):
   
    final = ""
        
    for index in range(len(s)):
        if s[index].isupper():
           final += s[index].lower()
        else:
            final += s[index].upper()
        

    return final

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)