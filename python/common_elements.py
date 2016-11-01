#common_elements.py
#Author: Rachel Cavin
#Purpose: Find the common elements of two integer arrays

class Common_Elements:

    def find_common_elements(self, array1, array2):
        mydict = {}
        answer = []
        for item in array1:
            mydict[item] = 1
        for item in array2:
            if item in mydict:
                mydict[item] += 1
            else:
                mydict[item] = 1
        for item, value in mydict.viewitems():
            if value > 1:
                answer.append(item)
        return answer;
