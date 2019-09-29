from time import sleep

a = 'python123#'
b = input("password")
if a == b:
    st = "your computer is open"
    print(st)
    sleep(10.0)

else:
        cb = "oops!!!! try again"
        print(cb)
        sleep(10.0)