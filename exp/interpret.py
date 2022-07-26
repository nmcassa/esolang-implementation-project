import sys

def check_syntax(line):
    allowed_chars = ["{", "}", "@", "~", "I", "|", "\n", "^"]
    allowed_spaces = [" ", "<", ">", "x", "X", "/", "+", "-"]
    
    #empty lines are allowed
    if len(line) == 0:
        return False
    
    i = 0

    while i < len(line):
        if line[i] not in allowed_chars and line[i] not in allowed_spaces:
            raise Exception("Syntax Error")
        if line[i] == " ":
            if line[i-1] not in allowed_spaces and line[i+1] not in allowed_spaces:
                raise Exception("Syntax Error")
        if line[i] == "<" and line[i+1] == ">":
            raise Exception("Syntax Error")
        i += 1
        
    if line[0] != "{":
        raise Exception("Syntax Error")
    
    is_int = True if line[1] == "{" else False

    return is_int

def parser(lines):
    
    new_lines = []
    
    for line in lines:
        
        is_int = check_syntax(line)

        new_line = [is_int]

        ops = ["I", "X", "x", "+", "-", "/", "@", "~"]

        inside = False
        inside_line = False
        
        for item in line:

            if item in ops:
                new_line.append(item)
            
            if item == "<":
                inside = True
                
            if inside:
                if item == ">":
                    inside = False
                    
                if item == "|" and not inside_line:
                    inside_line = True
                    val = 0
                    continue
                        
                if inside_line:
                    if item == "^":
                        val += 1
                        
                    if item == "|":
                        inside_line = False
                        new_line.append(val)
                        continue
                    
        new_lines.append(new_line)
    return new_lines

def check_sides(line, index):
    if type(line[index-1] == int) and type(line[index+1] == int):
        return True
    return False

def interpret(lines):

    ops = ["x", "X", "/", "+", "-"]
    hand = -1

    for line in lines:
        
        is_int = line[0]
        line.remove(line[0])
        index = 0

        for item in line:
            if item == "I":
                line[line.index(item)] = input()

        while index < len(line):
            item = line[index]
            if item == "@":
                if line[index + 1] == "~":
                    hand = line[0]
                    break
            if item == '~':
                line[index] = hand
            if item in ops:
                if check_sides(line, index):
                    if item == "+":
                        if is_int:
                            temp = int(line[index-1]) + int(line[index+1])
                        else:
                            temp = line[index-1] + line[index+1]
                        line.remove(line[index+1])
                        line.remove(line[index])
                        line[index-1] = temp
                        index = 0
                    if item == "x" or item == "X":
                        temp = int(line[index-1]) * int(line[index+1])
                        line.remove(line[index+1])
                        line.remove(line[index])
                        line[index-1] = temp
                        index = 0
                    if item == "-":
                        if is_int:
                            temp = int(line[index-1]) - int(line[index+1])
                        else:
                            temp = line[index-1] - line[index+1]
                        line.remove(line[index+1])
                        line.remove(line[index])
                        line[index-1] = temp
                        index = 0
                    if item == "/":
                        temp = int(line[index-1]) / int(line[index+1])
                        line.remove(line[index+1])
                        line.remove(line[index])
                        line[index-1] = temp
                        index = 0
                        
            index += 1
        if is_int:
            print(int(line[0]))
        else:
            print(chr(int(line[0])))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception('\n\nNeeds second arg')
    else:
        h = open(sys.argv[1], 'r')
        s = h.read()
        h.close()
        parsed = parser(s.splitlines())
        interpret(parsed)
