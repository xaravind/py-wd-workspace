try:
    with open(r"C:\Users\VishwasKSingh\Workspace\ey-wd-workspace\test2.txt","a") as fh:
        fh.write("I am vishwas k singh")

    # print("The content of the file is: ", line)
    print("\nthe conent of the file has ended")
except FileNotFoundError:
    print("File you are trying to open does not exist")
except FileExistsError:
    print("File that you are tring to write already exists")
else:
    print("This is an else block for try-except")
finally:
    print("Will always be executed")

