from collections import deque

sequence = deque([el for el in input()])   # create deque from the input
seq_copy = sequence.copy()   #create a copy , so that we can modify while looping through the main deque( sequence)

open_brackets = "{,(,["
closing_brackets = "},),]"

for el in sequence:         # loop through the deque by element
    if el in open_brackets:    # check if th element is in the open brackets
        el_index = open_brackets.index(el)   # get the index of the element in teh Open Brackets string
        seq_copy.popleft()                   # remove it from the copied deque
        close_el = closing_brackets[el_index]  # closing bracket = same index in Closing Brackect as the element(open bracket)
        if seq_copy[0] == close_el:          # we have removed the first Open bracket and check if the next one is the same closing one
            seq_copy.popleft()              # remove it from the copied deque
        elif seq_copy[-1] == close_el:      #if the following is not the bracket we search, check if it is the latest
            seq_copy.pop()                  # remove it then
        else:                              # if none of the above is True, break and then will break the loop and exit
            break
    else:                 # if the element is not in the open brackets skip it
        continue
if seq_copy:
    print("NO")
else:
    print("YES")


"""
test the following inputs:
{[()]} - YES.
(){}[] - YES.
{[(])} - NO.
{{[[(())]]}} YES.

"""
