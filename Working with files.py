data = "Data"

def write():
    with open("data.txt", "w")as file:
        file.write(data + "\n")
        file.close()
write()

def append():
    with open("data.txt", "a")as file:
        file.write(data + "\n")
        file.close()
append()

def read():
    with open("data.txt", "r")as file:
        file.close()

read()   
