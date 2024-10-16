import re
def count_substring(string, sub_string):
    count = 0
    while True:
        if len(string) == 0:
            break
        temp = string[0:len(sub_string)]
        if temp == sub_string:
            count += 1
        string = string[1:]
    return count
    

if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print(count)