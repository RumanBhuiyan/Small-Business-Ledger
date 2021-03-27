from my_shop import MyShop

myShop = MyShop()

isFirst=True
while True :  
    if isFirst :
        print('Select from 1 to 6 to perform action on store or "q" to exit :')
        print('1. Add a Product') 
        print('2. Delete a Product')
        print('3. Buy a Product')
        print('4. Sell a Product')
        print('5. See the list of products')
        print('6. See available Balance')
        isFirst=False
    
    selection=input("Your Selection : ")
    if selection == 'q' : 
        break
    
    if selection == '1' :
         myShop.addProduct()
    elif selection == '2':  
         myShop.deleteProduct()
    elif selection == '3' : 
         myShop.buyProduct()
    elif selection == '4' : 
         myShop.sellProduct()
    elif selection == '5' : 
         myShop.showProducts()
    else :  
         myShop.showAvailableBalance()
