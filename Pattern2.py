ln1 = input("Line1:")
ln2 = input ("Line2:")

n1=len(ln1)
n2=len(ln2)
result = n1 == n2

i=0
processed_chars = ""
while i < n1 and result:
    #Take i-character from input-line-1 and input-line-2
    ln1_char = #get i-character from ln1
    ln2_char = #get i-character from ln2

    #Check, that "processed_chars" contains neither of characters above (so, non of these characters have already been processed inside this loop)
    is_ln1_char_processed = #check processed_chars does not contain character[i] from line 1
    is_ln2_char_processed = #check processed_chars does not contain character[i] from line 2

    if not(is_ln1_char_processed) and not(is_ln2_char_processed):
        print("Both characters not processed yet, let's check them")
        #Because we'are going to process i-characters from both input strings - add them to the string which contains already processed characters
        processed_chars += #...

        #Lists to store indexes (positions) of i-character in input line1 and input line2.
        #When you declare lists, it would make sense to add "i" as first index in the list by default (because here we ARE processing i-character, so need to store its index in this list)
        ln1_char_indexes = #...
        ln2_char_indexes = #...

        #Have inner-loop to search for i-character in the remaining part of input-line1 and input-line 2
        j = i + 1
        while j < n1:
            #if j-character from line 1 equals to i-character from line 1, save it's index (which equals to "j") into the list of character indexes for input-line1
            #if j-character from line 2 equals to i-character from line 1, save it's index (which equals to "j") into the list of character indexes for input-line2
            j += 1

        print("List of indexes of line1 character", ln1_char, ":", ln1_char_indexes)
        print("List of indexes of line2 character", ln2_char, ":", ln2_char_indexes)
        print("Compare indexes of chars", ln1_char, "and", ln2_char, "inside their strings")

        #result = <result of comparing lists of indexes of i-character in line 1 and line 2 (ln1_char_indexes  vs. ln2_char_indexes)
        result = #...

    elif is_ln1_char_processed and not(is_ln2_char_processed):
        #print("Only character from 1st line already processed. Comparison fails")
        result = #Think what result should be equal to, if i-character already was processed before, but j-character was not processed yet?
    elif not(is_ln1_char_processed) and is_ln2_char_processed:
        #print("Only character from 2nd line already processed. Comparison fails")
        result = #Think what result should be equal to, if i-character has not been processed before, but j-character has already been processed?
    else:
        print("Both characters already processed, which is OK. Do nothing at this iteration")
     

    i += 1

print(result)