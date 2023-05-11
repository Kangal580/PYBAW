import subprocess

def option_test():
    subprocess.call(["C:\\Users\\toode\\Desktop\\Kode Test\\test.bat"], shell=True)

def main():
    print("\033[31mVelkommen til panelen\033[0m")
    print("_________________________")
    print("1. Test")
    print("2. Test")
    choice = input("Vælge et tal: ")
    if choice == "1":
        option_test()
    if choice == "2":
        exit

    else:
        print("Forkert værdig. Prøv igen.")
        main()

if __name__ == '__main__':
    main()