def calculation(amountc):
    paid = False
    amountp = 0
    while paid == False:
        coin = int(input("enter coin: "))
        if coin == 50 or coin == 20 or coin == 10 or coin == 5:
            amountp += coin
            if amountp >= amountc:
                print("here is your",option,"and",str(amountp-amountc)+"p for your change")
                paid = True
            else:
                print("you need to pay",(amountc-amountp))#
        else:
            print("we only except 50p,20p,10p,5p")

print("menu:\n1.coffee - 75p\n2.hot chocolate - 60p\n3.tea - 70p")
while True:
    option = input("what would you like to drink: ").lower()
    if option == "coffee":
        calculation(75)
        break
    elif option == "hot chocolate":
        calculation(60)
        break
    elif option == "tea":
        calculation(70)
        break
    else:
        print("no option for this drink")