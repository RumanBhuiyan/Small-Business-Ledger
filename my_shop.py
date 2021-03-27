class MyShop : 
    
    def __init__(self) :  
       self.__nameOfProducts=[] 
       self.__availableAmount =[]
       self.__profitEachItem= []
       self.__balance = 0
       self.__buyingPrices={}
       self.__sellingPrices={}
       self.insertProduct("Product Name","Amount","Profit Per Item")
    
    def addProduct(self) :  
        productName=input('Product Name : ')
        buyingPrice=input('Buy Price : ')  
        sellingPrice=input('Sell Price : ')
        availableNumber=input('Available number in the inventory: ')
        profit=input('Profit: ')
        
        if productName in self.__nameOfProducts :  
            productIndex=self.__nameOfProducts.index(productName)
            self.__buyingPrices[self.__nameOfProducts[int(productIndex)]] = buyingPrice
            self.__sellingPrices[self.__nameOfProducts[int(productIndex)]] = sellingPrice
        else  :  
            self.__buyingPrices[productName]=buyingPrice
            self.__sellingPrices[productName]=sellingPrice
            
        self.insertProduct(productName,availableNumber,profit)
    
    def insertProduct(self,name,amount,profit) :  
        if name in self.__nameOfProducts :  
            index=self.__nameOfProducts.index(name)
            self.__availableAmount[index]=int(self.__availableAmount[index])+amount 
        else :
            self.__nameOfProducts.append(name)
            self.__availableAmount.append(amount)
            self.__profitEachItem.append(profit)
            
    def deleteProduct(self) :  
        name=input("Product Name : ")
        if name in self.__nameOfProducts : 
            index=self.__nameOfProducts.index(name)
            self.__nameOfProducts.remove(name)
            self.__availableAmount.remove(self.__availableAmount[index])
            self.__profitEachItem.remove(self.__profitEachItem[index])
        else : 
            print("There is no such Product in My Shop")
        
    def buyProduct(self) :  
        selectProduct=int(input("Select Product : "))
        numberOfProducts=int(input("How many ?: "))
        self.__availableAmount[selectProduct]=int(self.__availableAmount[selectProduct])+numberOfProducts
        price=int(self.__buyingPrices[self.__nameOfProducts[selectProduct]]) 
        self.__balance = int(self.__balance)-numberOfProducts*price 
    
    def sellProduct(self):  
        selectProduct=int(input("Select Product : "))
        numberOfProducts=int(input("How many ? : "))
        if numberOfProducts > int(self.__availableAmount[selectProduct]):  
            print("Insufficient Stock ")
        else : 
            self.__availableAmount[selectProduct] = int(self.__availableAmount[selectProduct])-numberOfProducts
            price = int(self.__sellingPrices[self.__nameOfProducts[selectProduct]])
            self.__balance = int(self.__balance)+numberOfProducts*price
    
    def showProducts(self) : 
       for i in range(len(self.__nameOfProducts)) :  
           print('\t','-'*20,'|','-'*12,'|','-'*20)
           
           print('\t',f'| {self.__nameOfProducts[i]} ',end='')
           print(' '*(15-len(self.__nameOfProducts[i])+2),'|',end='')
           print(f' {self.__availableAmount[i] }',end='')
           print(' '*(12-len(str(self.__availableAmount[i]))), '|', end='')
           print(f' {self.__profitEachItem[i] }', end='')
           print(' '*(17-len(self.__profitEachItem[i])+2), '|')
    
    def showAvailableBalance(self) : 
        print('\t','-'*13,'|','-'*13)
        print('\t','| ',' Balance : |',' '*5,f'{self.__balance} ',' '*3,'|')

