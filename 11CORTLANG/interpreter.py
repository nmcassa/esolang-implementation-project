import sys
import math

def parser(lines):
    new_lines = []

    for line in lines:

        new_line = []
        
        new_line.append(line[0])

        count = 0
        pos = 1
        i = len(line)-1
        l = 0

        while i > 0:
            if line[i] == '1':
                count += pos
            pos *= 2
            i -= 1
            l += 1

        new_line.append(count)

        if new_line[0] == '1':
            new_line.append(l)
            if l > 3 and line[1:4] == '010':
                i = len(line)-1
                count = 0
                pos = 1
                while i > 3:
                    if line[i] == '1':
                        count += pos
                    pos *= 2
                    i -= 1
                new_line.append(count)
                    
        new_lines.append(new_line)

    return new_lines

stack = []

def interpret(lines):
    i = 0

    while i < len(lines):
        line = lines[i]
        if line[0] == '0':
            stack.append(line[1])
            
        else:
            if line[2] == 1:
                if line[1] == 1:
                    stack.pop(len(stack)-1)
                    
            if line[2] == 2:
                if line[1] == 0:
                    print(chr(math.ceil(stack[len(stack)-1])), end='')
                    
                if line[1] == 1:
                    stack[len(stack)-1] += stack[len(stack)-2]
                    stack.remove(stack[len(stack)-2])
                    
                if line[1] == 2:
                    stack[len(stack)-1] -= stack[len(stack)-2]
                    stack.remove(stack[len(stack)-2])
                    
                if line[1] == 3:
                    stack[len(stack)-1] *= stack[len(stack)-2]
                    stack.remove(stack[len(stack)-2])
                    
            if line[2] == 3:
                if line[1] == 0:
                    stack[len(stack)-1] /= stack[len(stack)-2]
                    stack.remove(stack[len(stack)-2])
                    
                if line[1] == 1:
                    stack.append(input())

            if len(line) == 4:
                i -= line[3]
                    
        i += 1           

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception('\n\nNeeds second arg')
    else:
        h = open(sys.argv[1], 'r')
        s = h.read()
        h.close()
        parsed = parser(s.splitlines())
        interpret(parsed)
