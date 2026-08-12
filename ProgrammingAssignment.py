import os
stock_1 = 100
stock_2 = 100
stock_3 = 100
stock_4 = 100 
stock_5 = 100
menu = 0

#payment
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

#total price restock
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0

#----------------------------------------------------------------------------------------------------------------
#define function

def homepage () :
    print ("================================================")
    print ("                                _ _           ")
    print ("  _ __ ___   ___  _ __   __ _  | (_)___  __ _ ")
    print (" | '_ ` _ \ / _ \| '_ \ / _` | | | / __|/ _` |")
    print (" | | | | | | (_) | | | | (_| | | | \__ \ (_| |")
    print (" |_| |_| |_|\___/|_| |_|\__,_| |_|_|___/\__,_|")
    print (" \t\tPHARMACY") 
    print ("================================================")
    print (" ")
    print ("Welcome to Monalisa Pharmacy !")
    print ("")
    print ("1. Inventory")
    print ("2. Sales")
    print ("3. Restock item")
    print ("4. Sales Report")
    print ("5. Exit")
    print ("")

def inventory_sales ():  
    print ("==================================================================")
    print ("|        Items          |        Stock         | Price per stock |")
    print ("==================================================================")
    print ("|    1. Mask            |       %5d          |        15       |"%stock_1)
    print ("|    2. Panadol         |       %5d          |         8       |"%stock_2)
    print ("|    3. Plaster         |       %5d          |         5       |"%stock_3)
    print ("|    4. Sanitary pad    |       %5d          |        20       |"%stock_4)
    print ("|    5. Milk powder     |       %5d          |        50       |"%stock_5)
    print ("==================================================================")
    
def payment_method ():
    input ("Please choose payment method (C-Cash,V-Visa Card,Q-QR Payment)>> ")

def restock_menu ():
    print ("                              Restock Menu:                      ")
    print ("=================================================================")
    print ("|      Items           |        Stock         |  Restock Price  |")
    print ("=================================================================")
    print ("|    1. Mask           |       %5d          |        12       |"%stock_1)
    print ("|    2. Panadol        |       %5d          |         5       |"%stock_2)
    print ("|    3. Plaster        |       %5d          |         4       |"%stock_3)
    print ("|    4. Sanitary pad   |       %5d          |        17       |"%stock_4)
    print ("|    5. Milk powder    |       %5d          |        15       |"%stock_5)
    print ("=================================================================")
        
def report ():
    print ("=====================================================================")
    print ("|        Items          |        Stock         |Price(Sales/Restock)|")
    print ("=====================================================================")
    print ("|    1. Mask            |       %5d          |        15/12       |"%stock_1)
    print ("|    2. Panadol         |       %5d          |         8/5        |"%stock_2)
    print ("|    3. Plaster         |       %5d          |         5/4        |"%stock_3)
    print ("|    4. Sanitary pad    |       %5d          |        20/17       |"%stock_4)
    print ("|    5. Milk powder     |       %5d          |        50/15       |"%stock_5)
    print ("=====================================================================\n")
    ttl = p1 + p2 + p3 + p4 + p5 # total sales
    rst = r1 + r2 + r3 + r4 + r5 # total restock values
    cf  = ttl - rst # cash flow
    print ("Total Sales for today is",ttl,"golds")
    print ("Total Restock Value for today is",rst,"golds")
    print ("Total Cash flow for today is",cf,"golds\n")

    
#----------------------------------------------------------------------------------------------------------------
#main-menu
    
print ("\t\t\t\t================================================")
print ("\t\t\t\t                                _ _           ")
print ("\t\t\t\t  _ __ ___   ___  _ __   __ _  | (_)___  __ _ ")
print ("\t\t\t\t | '_ ` _ \ / _ \| '_ \ / _` | | | / __|/ _` |")
print ("\t\t\t\t | | | | | | (_) | | | | (_| | | | \__ \ (_| |")
print ("\t\t\t\t |_| |_| |_|\___/|_| |_|\__,_| |_|_|___/\__,_|")
print ("\t\t\t\t================================================")
print ("\t\t\t\t\t ________________________")
print ("\t\t\t\t\t||                      ||")
print ("\t\t\t\t\t||                      ||")
print ("\t\t\t\t\t||     .--------.       ||")
print ("\t\t\t\t\t||    /  _.._    `\     ||")
print ("\t\t\t\t\t||   / /`    `-.   ; . .||")
print ("\t\t\t\t\t||   | |__  __  \   |   ||")
print ("\t\t\t\t\t||.-.| | e`/e`  |   |   ||")
print ("\t\t\t\t\t||   | |  |     |   |'--||")
print ("\t\t\t\t\t||   | |  '-    |   |   ||")
print ("\t\t\t\t\t||   |  \ --'  /|   |   ||")
print ("\t\t\t\t\t||   |   `;---'\|   |   ||")
print ("\t\t\t\t\t||   |    |     |   |   ||")
print ("\t\t\t\t\t||   |  .-'     |   |   ||")
print ("\t\t\t\t\t||'--|/`        |   |--.||")
print ("\t\t\t\t\t||   ;    .     ;  _.\  ||")
print ("\t\t\t\t\t||    `-.;_    /.-'     ||")
print ("\t\t\t\t\t||         ````         ||")
print ("\t\t\t\t\t||______________________||")
print ("")
input ("\t\t\t\t\tID       : ")
input ("\t\t\t\t\tPassword : ")


#----------------------------------------------------------------------------------------------------------------
#title

while menu != "5":
    os.system ('cls')
    homepage ()

    menu = input ("Please select the service you want : ")


#----------------------------------------------------------------------------------------------------------------
#1. Inventory
    
    if menu == "1":
        os.system ('cls')
        print ("Items Checking... ... ...")
        inventory_sales ()
        input ("Press enter to exit >> ")


#----------------------------------------------------------------------------------------------------------------
#2. Sales
        
    elif menu == "2":
        buy = -1
        while buy == -1:
            os.system ('cls')
            print ("Welcome to the store , You may buy anything you like :D")
            print ("If buy more than 30 will have 10% discount !")
            inventory_sales ()
            
            buy = input("Choose the item you want to buy (0 to leave)>> ")
            buy_list = ["1","2","3","4","5"]
            if buy in buy_list:
                quantity = int(input("Enter quantity that you want to buy : "))
                
                if buy == "1":
                    if 0 <= quantity <= stock_1:
                        stock_1 = stock_1 - quantity
                        p1 = quantity * 15
                        if quantity >= 30:
                            p1 = quantity * 15 * 0.9
                        os.system ('cls') #to print new inventory
                        inventory_sales ()
                        print ("Total payment >> %.2f" %p1)
                        payment_method ()
                    else:
                        print ("Our stock is only %d" %stock_1)
                        input ("Press Enter to Continue")

                elif buy == "2":
                    if 0 <= quantity <= stock_2:
                        stock_2 = stock_2 - quantity
                        p2 = quantity * 8
                        if quantity >= 30:
                            p2 = quantity * 8 * 0.9
                        os.system ('cls') #to print new inventory
                        inventory_sales ()
                        print ("Total payment >> %.2f" %p2)
                        payment_method ()
                    else:
                        print ("Our stock is only %d" %stock_2)
                        input ("Press Enter to Continue")

                elif buy == "3":
                    if 0 <= quantity <= stock_3:
                        stock_3 = stock_3 - quantity
                        p3 = quantity * 5
                        if quantity >= 30:
                            p3 = quantity * 5 * 0.9
                        os.system ('cls') #to print new inventory
                        inventory_sales ()
                        print ("Total payment >> %.2f" %p3)
                        payment_method ()
                    else:
                        print ("Our stock is only %d" %stock_3)
                        input ("Press Enter to Continue")

                elif buy == "4":
                    if 0 <= quantity <= stock_4:
                        stock_4 = stock_4 - quantity
                        p4 = quantity * 20
                        if quantity >= 30:
                            p4 = quantity * 20 * 0.9
                        os.system ('cls') #to print new inventory
                        inventory_sales ()
                        print ("Total payment >> %.2f" %p4)
                        payment_method ()
                    else:
                        print ("Our stock is only %d" %stock_4)
                        input ("Press Enter to Continue")

                elif buy == "5":
                    if 0 <= quantity <= stock_5:
                        stock_5 = stock_5 - quantity
                        p5 = quantity * 50
                        if quantity >= 30:
                            p5 = quantity * 50 * 0.9
                        os.system ('cls') #to print new inventory
                        inventory_sales ()
                        print ("Total payment >> %.2f" %p5)
                        payment_method ()
                    else:
                        print ("Our stock is only %d" %stock_5)
                        input ("Press Enter to Continue")
                buy = -1
                
            elif buy == "0" :
                    input("Press Enter again to leave")
                
            else:
                print ("Item not defined")
                input ("Please try again")
                buy = -1


#----------------------------------------------------------------------------------------------------------------
#3. Restock item

    elif menu == "3":
        itemrestock = -1
        while itemrestock == -1:
            os.system('cls')
            print ("Time to restock !")
            print ("")
            restock_menu ()
            itemrestock = input("Please select item that you want to restock (0 to leave)   >> ")
            itemrestock_list = ["1","2","3","4","5"]        
            if itemrestock in itemrestock_list:
                num = int(input("Please key in number of item you want to restock >> "))
                if itemrestock == "1":
                    stock_1 += num
                    r1 = num * 12 + r1                  
                elif itemrestock == "2":
                    stock_2 += num
                    r2 = num * 5 + r2
                elif itemrestock == "3":
                    stock_3 += num
                    r3 = num * 4 + r3
                elif itemrestock == "4":
                    stock_4 += num
                    r4 = num * 17 + r4
                elif itemrestock == "5":
                    stock_5 += num
                    r5 = num * 15 + r5
                rst = r1 + r2 + r3 + r4 + r5
                print ("Total Restock Value is",rst,"golds.")
                input ("Press enter to continue >> ")
                os.system ('cls') #to print updated inventory
                print ("Updated inventory >>")
                inventory_sales ()
                input ("Press Enter to Continue")
                itemrestock=-1
                
            elif itemrestock == "0":
                input ("Press Enter again to leave")
                
            else:
                print ("Invalid item")
                input ("Sorry,Please try again")
                itemrestock=-1 #try again to restock item
        

#----------------------------------------------------------------------------------------------------------------        
#4 Sales report
                
    elif menu == "4":
        os.system('cls')
        report ()
        input ("Press enter to leave")
        
                
#----------------------------------------------------------------------------------------------------------------
#5 Exit
        
    elif menu == "5":
        os.system('cls')
        input ("Thank you !Hope to see you next time! (enter to leave)")


#----------------------------------------------------------------------------------------------------------------
#Invalid function        

    else:
        print ("Invalid function")
        print ("Please key in 1-5")
        input ("Press enter to retry ")

#----------------------------------------------------------------------------------------------------------------
#END
