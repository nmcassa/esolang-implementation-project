import sys

def interpret(line):

    i = 0
    
    while i < len(line):
        item = line[i]

        #I don't know how you would use this input
        #We could have the oi output the input
        #Then we'd have to add an escape char
        if item == "i":
            input()
            
        if item == "o":
            print(line[i+1], end='')
            i += 1
            
        i += 1

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception('\n\nNeeds second arg')
    else:
        h = open(sys.argv[1], 'r')
        s = h.read()
        h.close()
        interpret(s)
