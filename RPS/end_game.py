import time, os

#read the ending message from file
def main():
    #read the 'thank you' from file
    handle = open('D:\\PythonCodes\\RPS\\end.txt', 'r')
    os.system('cls')
    msg = handle.read()
    handle.close()
    start_time = time.time()
    while time.time() - start_time < 2:
        print(f'\n{msg}\n')
        time.sleep(0.75)
        os.system('cls')
        time.sleep(0.25)
    print(f'\n{msg}\n')
    #read the 'creator' from file
    handle = open('D:\PythonCodes\\RPS\\about.txt', 'r')
    msg2 = handle.read()
    print(f'{msg2}')