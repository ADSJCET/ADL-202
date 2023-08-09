def replace(strng, substr, rplstr): 
    if substr not in strng:
        return strng

    low_index = strng.find(substr) # get lowest index of substring
    high_index = low_index + len(substr) # evaluate the highest index of substring

    return replace(strng[:low_index]+ rplstr + strng[high_index:], 


print(replace("Hello World Hello World", "llo", "@@"))
# He@@ World He@@ World
