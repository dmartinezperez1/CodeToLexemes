
#Open file and will close file when it exits 'with' block
with open('test.txt', 'r') as reader:
    f = reader.read()
    
    #Print out the text to be analyzed
    print("This file contains the following:")
    print(f)
    
    #initalize empty string to store text
    sub = ""
    
    #iterate through text.
    for i in range(0, len(f)):
        #Set conditions for the lexemes, a-z lower and upper case. and alpanumeric
        if((f[i] <= 'z')and(f[i]>='a') or
         (f[i]<= 'Z') and (f[i]>='A') or
          (f[i]<='9') and (f[i]>='0')):
            #if index of f is within conditions, append to string
            sub += f[i]
            
        else:
            #else print string of elements that have been added thus far.
            print(sub)
            #print out the character that did not meet the if conditions. should be a special character or white space.
            print(f[i])
            #Empty the string, start with a fresh new string
            sub = ""


   

    
