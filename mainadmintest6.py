import ctypes
import subprocess
import colorama
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def option_filer():
        base_path = os.path.dirname(os.path.abspath(__file__))
        bat_path = os.path.join(base_path, "filer.bat")
        subprocess.call([bat_path], shell=True, cwd=base_path)
        input("Success! Tryk Enter for at gå tilbage.")
        main()


def option_net():
    base_path = os.path.dirname(os.path.abspath(__file__))
    bat_path = os.path.join(base_path, "net.bat")
    subprocess.call([bat_path], shell=True, cwd=base_path)
    input("Success! Tryk Enter for at gå tilbage.")
    main()

def option_indstillinger():
    base_path = os.path.dirname(os.path.abspath(__file__))
    bat_path = os.path.join(base_path, "indstillinger.bat")
    subprocess.call([bat_path], shell=True, cwd=base_path)
    input("Success! Tryk Enter for at gå tilbage.")
    main()

def main():
    if not is_admin():
        input("Venligst åben filen som Admin. Tryk enter for at afslutte...")
        return

    colorama.init()  # Initialize colorama
    print(colorama.Fore.RED + "Velkommen til terminalen" + colorama.Style.RESET_ALL)
    print("_________________________")
    print("1. Ryd op på filer")
    print("2. Ryd op på netværk")
    print("3. Anvend ydeevneindstillinger")
    print("4. Afslut programmet")
    choice = input("Vælge et tal: ")
    if choice == "1":
        option_filer()

    elif choice == "2":
        option_net()

    elif choice == "3":
        option_indstillinger()

    elif choice == "4":
        input("Tryk enter for at afslutte.")

    else:
        print("Forkert værdi. Prøv igen.")
        main()


if __name__ == '__main__':
    main()
