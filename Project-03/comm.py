#!/usr/bin/python
import random, sys, locale, string
from optparse import OptionParser


class comm:
    def __init__(self, my_file1, my_file2, option_1, option_2, option_3, option_4):
        try:

            if my_file1[0] == '-':
                self.lines_file1 = sys.stdin.readlines()

                f = open (my_file2, 'r')
                f2 = f.read()
                self.lines_file2 = f2.split('\n')
                f.close()
            elif my_file2[0] == '-':
                f = open (my_file1, 'r')
                f2 = f.read()
                self.lines_file1 = f2.split('\n')
                f.close()
                self.lines_file2 = sys.stdin.readlines()
            elif my_file1[0] != '-' and my_file2[0] != '-':

                f = open(my_file1, 'r')

                f2 = f.read()

                self.lines_file1 = f2.split('\n')
                f.close()
               
                f = open (my_file2, 'r')
                f2 = f.read()  
                self.lines_file2 = f2.split('\n')
                f.close()
                                                
            else:
                parser.error ("There was a problem opening the files and/or reading in the input")         
            

            self.col1 = [] 
            self.col2 = []
            self.col3 = []
            
            
            if option_1 == False and option_2 == False and option_3 == False:
                self.remove_col = "unn"           
            elif option_1 == True and option_2 == False and option_3 == False:
                self.remove_col = "col1"
            elif option_2 == True and option_1 == False and option_3 == False:
                self.remove_col = "col2"
            elif option_3 == True and option_2 == False and option_1 == False:
                self.remove_col = "col3"
            elif option_1 == True and option_2 == True and option_3 == False:
                self.remove_col = "only three"
            elif option_2 == True and option_3 == True and option_1 == False:
                self.remove_col = "only one"
            elif option_3 == True and option_1 == True and option_2 == False:
                self.remove_col = "only two"
            else:
                self.remove_col = "none"

        except:
            parser.error ("There was a problem opening the files and/or reading in the input")


    def sort_check (self):

        max_len_file1 = len(self.lines_file1) - 1
        max_len_file2 = len (self.lines_file2) - 1
        flag = True

        if max_len_file1 > 1:
            counter = 0
            while counter < max_len_file1 -1:
                if  self.lines_file1[counter] > self.lines_file1[counter+1]:
                    flag = False
                    break
                counter = counter + 1

        if max_len_file2 > 1:
            counter = 0
            while counter < max_len_file2 -1:
                if self.lines_file2[counter] > self.lines_file2[counter+1]:
                    flag = False
                    break
                counter = counter + 1

        return flag
    def unsort_check(self):
        max_len = len (self.lines_file1)
        if len(self.lines_file2) > max_len:
            max_len = len (self.lines_file2)
        while len (self.lines_file1) < max_len:
            self.lines_file1.append ("\t")
        while len(self.lines_file2) < max_len:
            self.lines_file2.append ("\t")
        i = 0
        while i < max_len:
            if self.lines_file1[i] == self.lines_file2[i]:
                self.col1.append ("\t")
                self.col2.append (self.lines_file1[i])
                self.col3.append ("\t")
            else:
                print "these aren't the same"

                if self.lines_file1[i] < self.lines_file2[i]:
                    print "file 1 is smaller"
                    self.col1.append(self.lines_file1[i])
                    self.col2.append("\t")
                    self.col3.append("\t")

                    self.col1.append("\t")
                    self.col2.append("\t")
                    self.col3.append(self.lines_file2[i])
                else:
                    print "file 2 is smaller"
                    self.col1.append("\t")
                    self.col2.append("\t")
                    self.col3.append(self.lines_file2[i])

                    self.col1.append(self.lines_file1[i])
                    self.col2.append("\t")
                    self.col3.append("\t")
            i = i + 1

    def sorted_compare(self):
        counter1 = len (self.lines_file1) - 1
        counter2 = len (self.lines_file2) - 1
        if counter1 < counter2:
            index = counter1
        else:
            index = counter2
        iterator = 0
        while iterator <= index:
            if self.lines_file1[iterator]== self.lines_file2[iterator]:
                self.col1.append ("\t")
                self.col3.append ("\t")
                self.col2.append (self.lines_file1[iterator])
            else:
                if self.lines_file1[iterator] < self.lines_file2[iterator]:

                    self.col1.append (self.lines_file1[iterator])
                    self.col2.append ("\t")
                    self.col3.append ("\t")

                    self.col1.append ("\t")
                    self.col3.append (self.lines_file2[iterator])
                    self.col2.append ("\t")
                else:
                    self.col1.append ("\t")
                    self.col2.append ("\t")
                    self.col3.append (self.lines_file2[iterator])

                    self.col1.append (self.lines_file1[iterator])
                    self.col3.append ("\t")
                    self.col2.append ("\t")
            iterator = iterator + 1


    def make_matrix(self):
        len_col1 = len(self.col1)
        len_col2 = len(self.col2)
        len_col3 = len(self.col3)
        if self.remove_col == "col1":
            for i in range(len(self.col3)):
                if self.col3[i] == ("\t") and self.col2[i] == ("\t"):
                    self.col3[i] = "remove me"
                    self.col2[i] = "remove me"

            for i in range(len(self.col3)-1):
                if self.col3[i] != "remove me" and self.col2[i] != "remove me":
                    print (self.col3[i] + self.col2[i])
        elif self.remove_col == "col2":
            for i in range(len(self.col1)):
                if self.col1[i] == ("\t") and self.col2[i] == ("\t"):
                    self.col1[i] = "remove me"
                    self.col2[i] = "remove me"
            for i in range(len(self.col1)-1):
                if self.col3[i] != "remove me" and self.col2[i] != "remove me":
                    print (self.col1[i] + self.col2[i])
        elif self.remove_col == "col3":
            for i in range(len(self.col1)):
                if self.col1[i] == ("\t") and self.col3[i] == ("\t"):
                    self.col1[i] = "remove me"
                    self.col3[i] = "remove me"

            for i in range(len(self.col3)-1):
                if self.col3[i] != "remove me" and self.col2[i] != "remove me":
                    print (self.col1[i] +  self.col3[i])
        elif self.remove_col == "only three":
            i = 0
            while i < len(self.col2)-1:
                if self.col2[i] != "\t":
                    print self.col2[i]
                i = i + 1
        elif self.remove_col == "only two":
            i = 0
            while i < len(self.col3)-1:
                if self.col3[i] != "\t":
                    print self.col3[i]
                i = i + 1
        elif self.remove_col == "only one":
            i = 0
            while i < len(self.col1)-1:
                if self.col1[i] != "\t":
                    print self.col1[i]
                i = i + 1
        else:
            if len(self.col1) > len(self.col2):
                max_len = len(self.col1)
            else:
                max_len = len(self.col2)
            if max_len < len(self.col3):
                max_len = len(self.col3)
            while len(self.col1) < max_len:
                self.col1.append ("\t")
            while len(self.col2) < max_len:
                self.col1.append ("\t")
            while len(self.col3) < max_len:
                self.col3.append ("\t")
            for i in range(len(self.col1)):
                if self.col1[i] == "\t" and self.col2[i] == "\t" and self.col3[i] == "\t":
                    self.col1[i] = "remove me"
                    self.col3[i] = "remove me"
            i = 0

            while i < max_len -2:
               if self.col1[i] != "remove me" and self.col3[i] != "remove me" and self.col2[i] != "remove me":
                   print (self.col1[i] +  self.col2[i] + self.col3[i])
               i = i + 1



def  main():
    locale.setlocale(locale.LC_ALL, 'C')
    version_msg = "%prog 1.0"
    usage_msg = """%prog [OPTION]... FILE1 FILE2
    Output the comparison results between FILE1 and FILE2 in three columns."""
    parser = OptionParser(version=version_msg,
                          usage=usage_msg)
    parser.add_option("-1", "--nofile1",
                      action="store_false", dest="only_file_1", default=True,
                      help="suppress column 1 (lines unique to FILE1)")
    parser.add_option("-2", "--nofile2",
                      action="store_false", dest="only_file_2", default=True,
                      help="suppress column 2 (lines unique to FILE2)")
    parser.add_option("-3", "--nocommon",
                      action="store_false", dest="both", default=True, help=
                      "suppress column 3 (lines that appear in both files)")
    parser.add_option("-u", "--unsorted",
                      action="store_true", dest = "files_unsorted",
                      default=False, help="work with unsorted files")
    options, args = parser.parse_args(sys.argv[1:])

    if len(args) != 2:
        parser.error("you need exactly 2 arguements")

    try:
        option_1 = not bool(options.only_file_1)
        option_2 = not bool(options.only_file_2)
        option_3 = not bool(options.both)
        option_4 = not bool(options.files_unsorted)

    except:
        parser.error ("There was a problem accessing the destination of the files")
    file1 = args[0]
    file2 = args[1]
    try:

        constructor_files = comm (file1, file2, option_1, option_2, option_3, option_4)

    except:
        parser.error ("couldn't create a constructor")

    try:

        if option_4 == False:

            constructor_files.unsort_check()
        else:

            sorted_check = constructor_files.sort_check()

            if sorted_check == True:
                constructor_files.sorted_compare()
            else:
                print ("The 2 sources of data do not have not yet been sorted")

        constructor_files.make_matrix()
    except:
        parser.error ("There was an issue with comparing the files")
if __name__ == "__main__":
    main()






