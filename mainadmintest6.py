import ctypes
import subprocess
import colorama

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def option_test():
    subprocess.call(["C:\\Users\\toode\\Desktop\\Kode Test\\test.bat"], shell=True)

def main():
    if not is_admin():
        input("Venligst åben filen som Admin. Tryk enter for at afslutte...")
        return

    colorama.init()  # Initialize colorama
    print(colorama.Fore.RED + "Velkommen til terminalen" + colorama.Style.RESET_ALL)
    print("_________________________")
    print("1. Test")
    print("2. Test")
    choice = input("Vælge et tal: ")
    if choice == "1":
        option_test()
    elif choice == "2":
        return
    else:
        print("Forkert værdi. Prøv igen.")
        main()

    input("Tryk enter for at afslutte...")

if __name__ == '__main__':
    main()
