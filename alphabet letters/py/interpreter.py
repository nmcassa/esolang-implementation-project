import sys

def interpret(arr):
    
    stack = []
    pointer = 0
    
    for item in arr:

        if item == 'p':
            pointer = 0
        
        if item == 'a':
            pointer += 1
            
        if item == 's':
            pointer -= 1
            
        #??? don't know if this is what he meant
        if item == 'm':
            pointer *= pointer

        #??? again don't know, didn't want floats
        if item == 'd':
            pointer //= pointer

        if item == 'z':
            stack.append(pointer)

        if item == 'c':
            for num in stack:
                print(chr(num), end='')

        

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception('\n\nPlease give .alphaletters file as an second arg')
    else:
        h = open(sys.argv[1], 'r')
        s = h.read()
        h.close()
        interpret(list(s))
