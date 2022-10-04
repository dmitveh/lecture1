file =open("result.txt","w")
for x in range (1,101):
    if x%5==0 and x%3==0:
        print("HelloWorld")
        file.write("HelloWorld")
        file.write("\r")
    elif x%3==0:
        print("Hello")
        file.write("Hello")
        file.write("\r")
    elif x%5==0:
        print("World")
        file.write("World")
        file.write("\r")
    else:
        print(x)
        file.write(str(x))
        file.write("\r")


