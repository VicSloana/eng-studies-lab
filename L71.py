#Anna, Victoria
##
##def too_long(x):
##    result = len(x) 
##    if result >= 1400:
##        print("Too long to be sent")
##    else:
##        print("Sent")
##
##too_long("happy")
##too_long("hbdfibdsfnshbsjnfidgifudi")
##
##import unicodedata 
##
##print(unicodedata.name("%"))
##


def count_letters(word):
    total = 0
    for x in word:
        if x == "o":
            total = total + 1
    print(total)

count_letters("bobo bobo") 

