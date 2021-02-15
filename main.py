import os


def main():

    mode = input("Выбери режим.\n1 - запустить users.py\n2 - запустить find_athelete.py\n")
    if mode == "1":
        os.system('python users.py')
    elif mode == "2":
        os.system('python find_athelete.py')
    else:
        print("Некорректный режим:(")

if __name__ == "__main__":
    main()