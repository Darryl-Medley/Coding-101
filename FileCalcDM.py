# Simple calculation program to demonstrate use of Python text files
# Written on 04/24/2014 by Darryl Medley for Coding 101 on the TWiT network

# This program reads a text file called equation_list.txt that is in the same folder
# as the .py program file. The file must contain one expression per line and be in
# Polish (aka prefix) notation: Operator, Operand1, Operand2. For example:
# +, 12.5, 24.3
# -, 23, 17
# Note: Real Polish notation has spaces, not commas between the values. I used
#       commas to make it easier to read.

print "Polish (prefix) Notation Equation File Processor"
fname = "./equation_list.txt"
try:
    eqlstFile = open(fname, "r")  # open the text file
except:
    print "Error: File",fname,"does not exist"
else:
    # The first thing we do is read the file into a Python list. Each line in
    # the file is an element in the list. .splitlines() removes the \n newline
    # character from the end of each line.
    eqList = eqlstFile.read().splitlines()   # read file and strip newline characters
    eqlstFile.close()   # We're done with the file now that the lines are in a list

    # Process each equation in the list
    for eqLine in eqList:
        if eqLine.strip() != "":   # skip blank lines
            # Parse the equation into operator and operands by creating a little list using split()
            opList = eqLine.split(',')
            ErrMsg = ""
            if len(opList) < 3:
                ErrMsg = "Missing Operator or Operand"
            elif opList[0].strip() not in "+-*/%":
                ErrMsg = "Operator is not +, -, *, / or %"
            else:
                try:
                    oprnd1 = float(opList[1])
                    oprnd2 = float(opList[2])
                except:
                    ErrMsg = "One of the operands is not a number"
                else:
                    opr8tr = opList[0].strip()
                    if (opr8tr in "/%") and (oprnd2 == 0.0):
                        ErrMsg = "Division by Zero is illegal"

            if ErrMsg == "":   # No errors were found with the equation line
                # Calculate and print the result. Here we cheat and use Python's
                # eval() function that interprets a string as an expression.
                # Note that we rearrange the elements into infix notation.
                print eqLine,"=",eval(opList[1]+" "+opr8tr+" "+opList[2])
            else:
                print eqLine,"= Error:",ErrMsg
                
print 
raw_input("(press Enter to close)")

