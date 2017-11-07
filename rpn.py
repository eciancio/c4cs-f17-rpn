import colorama
import operator

ops = {
        '+': operator.add,
        '-': operator.sub,
        '^': operator.pow
    }

def calculate(string):
    stack = list()
    for token in string.split():
        try:
            stack.append(int(token))

        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = ops[token]
            result = function(arg1,arg2)
            stack.append(result)

    return stack.pop()
    

def no_calculations(string):
    print(string)

def main():
    while True:
        answer = calculate(input("rpn calc> "))
        if (answer < 0) : 
            print(colorama.Fore.RED + str(answer))
            print(colorama.Style.RESET_ALL)

        else: 
            print answer


        
        
        

if __name__=='__main__':
    main()
