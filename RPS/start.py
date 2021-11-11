import time, os

#reads starting message from file
def main():
    #reads 'welcome' file
    handle = open('D:\PythonCodes\\RPS\\welcome.txt', 'r')
    os.system('cls')
    msg = handle.read()
    handle.close()
    start_time = time.time()
    while time.time() - start_time < 5:
        print(f'\n{msg}\n')
        time.sleep(0.75)
        os.system('cls')
        time.sleep(0.25)
    print(f'\n{msg}\n')
    #reads creator from file
    handle = open('D:\PythonCodes\\RPS\\about.txt', 'r')
    msg2 = handle.read()
    print(f'{msg2}')