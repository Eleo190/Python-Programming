#PROBLEM 1
def line_number(read_file, write_file):
    '''This function takes two files. It reads read_file and writes every line in read_file prefixed
    by its line number into write_file'''
    try:
        with open(read_file, "r") as infile, open(write_file, "w") as outfile:
            #takes every line in the infile and enumerates it starting at index 1. then, iterates over the newly made tuple of tuples, printing the number then line contents to the outfile
            for num, func in enumerate(infile, 1):
                print(f"{num}. {func.rstrip()}", file=outfile)
    except IOError as err:
        print(f"An error occurred while trying to read or write the files: {err}")
        raise

def parse_functions(read_file):
    '''This function takes a file and reads it line by line. It returns a tuple of tuples, where each tuple contains the function name and its parameters.'''
    try:
        with open(read_file, "r") as infile:
            functions = []
            lines = infile.readlines()
            #use numline here to seperate from line in inner loop. numline represents the lines in outer loop are numbered
            for lineid, numline in enumerate(lines, 1):
                if numline.startswith("def") == True:
                    #splice "def " from the string, split from open parenthesis to get name, then splice off at index for closed parenthesis to get params
                    def_line = numline[4:]
                    func_name, arg_list = def_line.split("(")
                    arg_list = arg_list[:arg_list.find(")")]
                    #add definition line at declaration, checking for comment inline
                    if numline.find("#") != -1:
                        func_code = numline[:numline.find("#")].rstrip() + "\n"
                    else: func_code = numline
                    for line in lines[lineid:]:
                        #check if each line is blank and if its a comment, if neither then checks if line starts with whitespace to make sure its part of the same function
                        if line.isspace() == False and line.strip().startswith("#") == False:
                            if line.startswith((' ', '\t')) == True:
                                if line.find("#") != -1:
                                    func_code += line[:line.find("#")].rstrip() + "\n"
                                else:
                                    func_code += line
                            else: 
                                break
                    functions.append((lineid, func_name.strip(), arg_list.strip(), func_code))
            functions.sort(key=lambda item:item[1])
            functions = tuple(functions)
            return functions
    except IOError as err:
        print(f"An error occured reading {read_file}: {err}")
        raise
def main():
    line_number("Homework2/p1_Leocadio_Eric.py", "Homework2/test.txt")
    print(parse_functions("Homework2/p1_Leocadio_Eric.py"))
if __name__ == "__main__":
    main()
    print("ERIC LEOCADIO, Z23712790")

