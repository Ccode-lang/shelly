import os
running = True

while running:
    cwd = os.getcwd()
    input_ = raw_input("shelly#")
    inp = input_.split(" ")
    if inp[0] == "cd":
        os.chdir(inp[1])
    elif "=" in input_:
        exec(input_)
    elif inp[0] == "echo":
        try:
            exec("os.system(inp[0] + ' ' " + '+' + inp[1] + ")")
        except:
            os.system(inp)
    elif input_ == "exit":
        running = False
    elif "if" in input_:
        print("error: if is not supported in shelly")
    else:
        if os.system(input_ + " >/dev/null 2>&1") == 0:
            os.system(input_)
        else:
            print("shelly: error: syntax is wrong")