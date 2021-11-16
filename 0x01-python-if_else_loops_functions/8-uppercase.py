def uppercase(str):
    for i in len(str):
        if str[i] >= ord('a') and str[i] <= ord('z'):
            ord(str[i]) += 32
    print(str)        
