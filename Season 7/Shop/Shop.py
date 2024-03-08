import qrcode
PRODUCTS = []
basket_of_goods = []


def read_from_database():
    f = open("season 7\database.txt", "r")
    for line in f:
        a = line.split("\n")
        b = a[0]
        result = b.split(",")
        my_dict = {"code": result[0], "name": result[1],
                   "price": result[2], "count": result[3]}

        PRODUCTS.append(my_dict)

    f.close()


def write_to_database():
    f = open("season 7/database.txt", "w")

    for product in PRODUCTS:

        txt = product["code"] + "," + product["name"] + "," + product["price"] + "," + product["count"] + "\n"
        f.write (txt)
    f.close()


def show_menu():
    print("-1 Add")
    print("-2 Edit")
    print("-3 Remove")
    print("-4 Search")
    print("-5 Show List")
    print("-6 Buy")
    print("-7 QrCode")
    print("-8 Exit")


def add():
    code = input("enter code: ")
    name = input("enter name: ")
    price = input("enter price: ")
    count = input("enter count: ")
    new_product = {'code': code, 'name': name, 'price': price, 'count': count}
    PRODUCTS.append(new_product)
    print("Item added successfully")
    write_to_database()
    showlist()


def edit():
    showlist()
    c_input = input("type your code: ")
    print("-1 Name")
    print("-2 Price")
    print("-3 Count")
    u_input = input("type your keyword: ")

    if u_input == "1":
        n_input = input("Enter your new name: ")
        for product in PRODUCTS:
            if product["code"] == c_input:
                product["name"] = n_input
                showlist()
                print("Information updated successfully")
    if u_input == "2":
        p_input = input("Enter your new Price: ")
        for product in PRODUCTS:
            if product["code"] == c_input:
                product["price"] = p_input
                showlist()
                print("Information updated successfully")
    if u_input == "3":
        c_input = input("Enter your new Count: ")
        for product in PRODUCTS:
            if product["code"] == c_input:
                product["count"] = c_input
                showlist()
                print("Information updated successfully")
                write_to_database()


def remove():
    remov_input = input("Enter your code: ")
    for product in PRODUCTS:
        if remov_input == product["code"]:
            PRODUCTS.remove(product)
            print("Removed successfully")
            write_to_database()
            showlist()


def search():
    user_input = input("type your keyword: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"], "\t\t", product["name"],
                  "\t\t", product["price"])
            break
    else:
        print("not found")


def showlist():
    print("code\t\t\tname\t\t\tprice")
    for product in PRODUCTS:
        print(product["code"], "\t\t\t", product["name"],
              "\t\t\t", product["price"], "\t\t\t", product["count"])


def buy():
    print (" print 'Done' when you finish shopping ")
    Factor = []
    final_cost = 0
    
    while True :    
        user_choice = input(" Please enter the product's code : ")
        
        if user_choice == "Done" :
            print ("name\t\tcount\t\tfee\t\tcost")
            for product in Factor :
                print ( product["name"] , "\t\t" , product["tedad"] , "\t\t" , product["price"] , "\t\t" , product["cost"])
                final_cost = final_cost + int( product["cost"] )
            
            print (" final cost : ", final_cost)
            break

        else :
            for product in PRODUCTS :
                if product["code"] == user_choice :
                    print (" We have this product ")
                    number = int ( input (" How many do you want : "))
                    count = int ( product["count"] )
                    if number <= count :
                        print ("OK! What else ?")
                        store = count - number
                        product["count"] = str ( store )                                    
                        price = int ( product["price"] )
                        cost = number * price
                        new_purchase = {"name" : product["name"] , "tedad" : number , "price" : product["price"] , "cost" : cost }
                        Factor.append ( new_purchase )

                    else :
                        print (" We don't have this many ")

                    break
            
            else :
                print (" There is not any product with this code number ")


def qr_code():
    c_input = input("Enter your code: ")
    for product in PRODUCTS:
        if c_input == product["code"]:

            qr_s = (product["code"], product["name"],
                    product["price"])
            img = qrcode.make(qr_s)
            img.save("yourqrcode.png")


print("Wellcome Seppehrj Store")
print("Loading...")
read_from_database()
print("Data loaded.")
while True:
    show_menu()
    choise = int(input("Enter your choice: "))

    if choise == 1:
        add()
    elif choise == 2:
        edit()
    elif choise == 3:
        remove()
    elif choise == 4:
        search()
    elif choise == 5:
        showlist()
    elif choise == 6:
        buy()
    elif choise == 7:
        qr_code()
    elif choise == 8:
        write_to_database()
        exit(0)
    else:
        print("Wrong number")

