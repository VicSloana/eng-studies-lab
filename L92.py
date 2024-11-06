#L92
def abracadabra(string):
    index = len(string)
    while index >= 0:
        print(string[:index])
        index -=1

abracadabra("victoria")
