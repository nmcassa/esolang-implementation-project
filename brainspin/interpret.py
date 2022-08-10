import sys

def remove_from_list(arr):
    allowed = ['+', '-', '.', ',', '[', ']', '*']

    i = 0

    while i < len(arr):
        if arr[i] not in allowed:
            del arr[i]
        else:
            i += 1

    return arr

def interpret(arr):
    stack = [0, 0, 0]
    pointer = 0
    i = 0

    while i < len(arr):
        item = arr[i]

        if item == '+':
            stack[pointer] += 1
            
        if item == '-':
            stack[pointer] -= 1
            
        if item == '.':
            print(chr(stack[pointer]), end='')
            
        if item == ',':
            stack[pointer] = int(input())
            
        if item == '[':
            matching = 0
            if stack[pointer] == 0:
                while i < len(arr):
                    if arr[i] == '[':
                        matching += 1
                    elif arr[i] == ']':
                        if matching != 0:
                            matching -= 1
                        else:
                            break
                    i += 1
                i += 1
                
        if item == ']':
            if stack[pointer] != 0:
                while i >= 0:
                    if arr[i] == ']':
                        matching += 1
                    elif arr[i] == '[':
                        if matching != 0:
                            matching -= 1
                        else:
                            break
                    i -= 1
                i -= 1

        if item == '*':
            pass

        pointer = 0 if pointer == 2 else pointer + 1
        i += 1


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception('\n\nPlease give file in second arg')
    else:
        h = open(sys.argv[1], 'r')
        s = h.read()
        h.close()
        code = remove_from_list(list(s))
        interpret(code)
