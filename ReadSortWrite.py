# Read-Sort-Write file program
# Written on 05/01/2014 by Darryl Medley for Coding 101 on the TWiT network

# This program reads a text file called name_list.txt that is in the same folder
# as the .py program file. The file must contain one name record per line with
# the format: Name, Age, Zipcode
# Sample Test File (save as name_list.txt):
# Padre, 30, 9000
# Shannon, 21, 9100
# Darryl, 50, 9200

# if the Save option is selected, the file is written to name_list_sorted.txt

from operator import itemgetter   # itemgetter lets us sort by any field in the list

# Generic List print routine
def printList(nmList):
    for rec in nmList:
        print ','.join(rec)   # ','.join converts each sub-list into a comma-delimited string
    return 

# Begin main program    
print "Coding 101 Read-Sort-Write Demo Program\n"
fname = "./name_list.txt"
try:
    with open(fname, "r") as nameListFile:  # open the text file to read
        # Read the file into a Python list. Each line in the file becomes a
        # string element in the list. .splitlines() removes the \n (newline)
        # character from the end of each line and filter skips blank lines
        infoList = filter(lambda r : r != '',nameListFile.read().splitlines())
except:
    print "Error: File",fname,"does not exist"
else:
    print "Unsorted File Contents:"
    # Convert each comma-delimited string in the list into a sub-list so we can sort on
    # any field and remove any leading and trailing blanks (whitespace)
    infoList = [[fld.strip() for fld in s.split(",")] for s in infoList]

    printList(infoList)   # call our list print function defined above

    listSorted = False    # List has not been sorted yet
    menuStr = "1-Sort by Name, 2-Sort by Age, 3-Sort by Zip: "

    # Main loop
    while True:
        print "\nMain Menu (press Enter to exit):"
        optn = raw_input(menuStr)
        if optn == "":
            break
        
        if optn[0] in "123":
            # Sort the list by the selected field

            if optn[0] == '2':
                # convert the Age field to an integer so it will sort correctly
                infoList = [[fld[0], int(fld[1]), fld[2]] for fld in infoList]                    
            
            infoList.sort(key=itemgetter(int(optn[0])-1))
            
            if optn[0] == '2':
                # convert the Age field back to a string so it will print correctly
                infoList = [[fld[0], str(fld[1]), fld[2]] for fld in infoList]                    
            
            print "\nSorted by", ["Name:","Age:","Zipcode:"][int(optn[0])-1]
            printList(infoList)   # call our list print function defined above
            listSorted = True    
            menuStr = "1-Sort by Name, 2-Sort by Age, 3-Sort by Zip, S-Save sorted list: "
        elif optn[0].upper() == "S":   # convert to upper-case so both lower-case and upper-case will work
            # Save option selected
            if not listSorted:
                print "Only a sorted list can be saved"
            else:
                with open('./name_list_sorted.txt', 'w') as sortedListFile:
                    # write out each line with a newline (\n) at the end
                    # ','.join is used to create a single comma-delimited string for each record
                    for infoRec in infoList:
                        sortedListFile.write('{0}\n'.format(','.join(infoRec)))
                print "List saved to file name_list_sorted.txt"
                break
        else:
            print "Invalid selection"
    # end while loop
# end try / except / else
