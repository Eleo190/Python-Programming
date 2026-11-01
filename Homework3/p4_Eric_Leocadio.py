#PROBLEM 4
from testif import testif
#cant use 'from' as a parameter name, using 'start' instead
def ed_read(filename:str, start=0, to=-1) -> str:
    '''returns the contents of the file "filename", starting from "start", ending at "to"
    Preconditions: "to" must be shorter than the length of the file'''
    with open(filename, 'r') as infile:
        file_txt = infile.read()
    #full read
    if to == -1:
        return file_txt[start:]
    #partial read
    elif to <= len(file_txt):
        return file_txt[start:to]
    #out of bounds
    elif to > len(file_txt):
        raise IndexError("Arg 'to' exceeds length of file")

def ed_find(filename:str, search_str:str) -> list:
    '''Counts the amount of times "search_str" occurs in the file "filename" and returns the indices of the start of each occurence of the substring'''
    with open(filename, 'r') as readfile:
        file_txt = readfile.read()
        indices = []
        found = file_txt.find(search_str)
        #iterates until no more occurences found
        while found != -1:
            indices.append(found)
            found = file_txt.find(search_str,found+len(search_str))
        return indices

def ed_replace(filename:str, search_str:str, replace_with:str, occurence=-1) -> int:
    """Replaces the occurence of 'search_str' set by 'occurence' with 'replace_with' in 'filename' if 'occurence' = -1, all instances will be replaced
    returns the amount of times that the substring was replaces"""
    with open(filename, 'r') as infile:
        file_txt = infile.read()
    indices = ed_find(filename, search_str)
    if occurence ==-1:
        file_txt = file_txt.replace(search_str, replace_with)
        with open(filename, 'w') as outfile:
            outfile.write(file_txt)
        return len(indices)
    else:
        if occurence >= len(indices):
            return 0
        else:
            file_txt = file_txt[0:indices[occurence]] + file_txt[indices[occurence]:].replace(search_str, replace_with, 1)
            with open(filename, 'w') as outfile:
                outfile.write(file_txt)
                return 1

def ed_append(filename:str, string:str) ->int:
    """writes 'string' to 'filename', appending if the file already exists
    returns the number of characters written to 'filename'"""
    with open(filename, 'a') as outfile:
        return outfile.write(string)

def test_ed_replace():
    '''unit test for ed_find using testif module'''
    test_file = 'test_replace.txt'
    with open(test_file, 'w') as file:
        file.write('123454231')

    #Test multiple replacements
    testif(ed_replace(test_file, '23', 'newlines', -1)==2, "Test ed_replace multiple", "ed_replace success", "ed_replace, failed")
    #Test one replacement
    with open(test_file, 'w') as file:
        file.write('123454231')
    testif(ed_replace(test_file, '123', 'newlines')==1, "Test ed_replace single", "ed_replace success", "ed_replace, failed")
    #test no replacement
    with open(test_file, 'w') as file:
        file.write('123454231')
    testif(ed_replace(test_file, '12333', 'newlines',3)==1, "Test ed_replace none", "ed_replace success", "ed_replace, failed")
    
    
def test_ed_find():
    '''unit test for ed_find using testif module'''
    test_file = 'test_replace.txt'
    with open(test_file, 'w') as file:
        file.write('123454231')
    #Test substring present
    testif(ed_find(test_file, '23')==[1,6], 'test ed_find present', 'ed_find success', 'ed_find failure')
    #Test substring absent
    testif(ed_find(test_file, 'words')==[], 'test ed_find absent', 'ed_find success', 'ed_find failure')

def main():
    print("Testing:")

    test_ed_find()
    test_ed_replace()

    demo_file = "demo.txt"
    #clearing file
    with open(demo_file, 'w'):
        pass

    #appending and reading file
    ed_append(demo_file, "12345")
    print("file: " + ed_read(demo_file))
    ed_append(demo_file, "12345")
    print("file: " + ed_read(demo_file))

    #partial read
    print("first four characters: " + ed_read(demo_file, 0, 4))

    #finding
    print("Indexes of '12': " + str(ed_find(demo_file, '12')))

    #replace
    ed_replace(demo_file, '12345', 'abcde', 0)
    print("swap first occurence with letters: " + ed_read(demo_file))


if __name__ == "__main__":
    main()