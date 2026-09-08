#Problem 3: Duplicated Substrings. 


def find_dup_str(s, n):
    #range is from start to 2n less than len because 2 substrings are needed
    for i in range(0, (len(s)-(n*2)+1)):
        #slice moves forward and is always n long
        test_string = s[i:i+n]
        if test_string in s[i+n:]:
            return(test_string)
    return("")

def find_max_dup(s):
    #Count backwards, first substring found is fastest 
    for i in range((len(s))//2, 0, -1):
        dup = find_dup_str(s, i)
        if dup != "":
            return(dup)


s = input("Enter string to search: ")
n = int(input("Enter substring length: "))
print(find_dup_str(s,n))

s = input("Enter string to search: ")
print(find_max_dup(s))