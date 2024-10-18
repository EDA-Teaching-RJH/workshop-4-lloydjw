def calculation(amountc):
    paid = False
    amountp = 0
    while paid == False:
        coin = int(input("enter coin: "))
        amountp += coin
        if amountp >= amountc:
            print("here is your",option,"and",str(amountp-amountc)+"p for your change")
            paid = True
        else:
            print("you need to pay",(amountc-amountp))

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