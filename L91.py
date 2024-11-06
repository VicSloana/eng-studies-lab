# mylist = ["uno", "dos", "tres", "cuatro"]

def total_length(mylist):
    total = 0 
    for x in mylist:
        total = total + len(x)
    return total

print(total_length(["uno", "dos", "tres", "cuatro"]))


        
