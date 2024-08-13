bnk_balanace = 0
def main():
    print("1.Deposit")
    print("2.WithDraw")
    print("3.Show Balance")
    print("4.Exit")
    get = int(input("Select a Option:"))
    if get == 1:
        deposit()
        main()
    elif get == 2:
        withdraw()
        main()
    elif get == 3:
        show_balance()
        main()
    elif get == 4:
        exit()
    else:
        print("Invalid Input")
        main()

def deposit():
    global bnk_balanace
    get = int(input("Enter Amount:"))
    bnk_balanace += get

def show_balance():
    print(f"Balance:{bnk_balanace}")
    print("***********************")

def withdraw():
    global bnk_balanace
    get = int(input("Enter Amount:"))
    if get<= bnk_balanace:
        bnk_balanace -= get
    elif get >= bnk_balanace:
        print("Insufficient Balance")
    else:
        print("Invalid Input")
    
if __name__ == ('__main__'):
    main()