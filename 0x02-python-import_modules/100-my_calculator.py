#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    operator = [+,*,/,-]
    if len(sys.argv) == 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        for i in range(1, len(sys.argv)):
            if sys.argv[i] in operator:
                if sys.argv[i] == "+":
                    sum = ""
                    sum = int(sys.argv[1]) + int(sys.argv[3])
                    
            else:
                print("jj")

