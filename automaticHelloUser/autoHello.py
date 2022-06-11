import subprocess


file = open("helloTest.py", "w")
file.close()

file = open("helloTest.py", "a")
file.write("def helloUser():\n")
file.write("\tname = input('What is your name? ')\n")
file.write("\tprint(f'Hello, {name}')\n\n")

file.write("if __name__ == '__main__':\n")
file.write("\thelloUser()\n")


file.close()

#if __name__ == '__main__':
#    # Script2.py executed as script
#    # do something
#    func1()

subprocess.run("helloTest.py", shell=True)

print("Does this run before subprocess finishes?")
