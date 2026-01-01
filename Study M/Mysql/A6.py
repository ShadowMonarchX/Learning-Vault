import mysql.connector
from datetime import date
class Inventory_Management:
    
    def __init__(self):
        self.mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@123",
        database="Abhay"
    )
        self.mycursor=self.mydb.cursor()
        while True:
            print("\nWelcome to Sughatika")
            print("Enter 1 for adding a new product")
            print("Enter 2 for adding an order")
            print("Enter 3 for checking stock")
            print("Enter 4 for adding stock")
            print("Enter 5 for checking orders")
            print("Enter 6 for checking pending orders")
            print("Enter 7 for completing an order")
            print("Enter 8 for checking last month's sale")
            print("Enter 9 for production suggestions")
            print("Enter 10 for Exit")
            
            input_value = int(input())
            while input_value < 1 or input_value > 10:
                print("Enter a valid choice")
                input_value = int(input())
            
            if input_value == 1:
                self.register_Product()
            elif input_value == 2:
                self.add_Order()
            elif input_value == 3:
                self.check_Stock()
            elif input_value == 4:
                self.add_Stock()
            elif input_value == 5:
                self.check_Order_Status()
            elif input_value == 6:
                self.check_Pending_Orders()
            elif input_value == 7:
                self.complete_Order()
            # elif input_value == 8:
            #     check_Sales()
            # elif input_value == 9:
            #     suggest_Production()
            # elif input_value == 10:
            #     break
    def register_Product(self):
        print("Enter product's Model number")
        model_no = input().upper()
        if not self.check_Model_No(model_no):
            type_input = input("Enter product type: ").upper()
            while True:
                pieces_input = int(input("Enter ready pieces: "))
                if pieces_input < 0:
                    print("Enter a valid number")
                else:
                    break
                print("Enter a valid number")
            sql_query = "INSERT INTO product (model_no, product_type, stock) VALUES (%s, %s, %s)"
            self.mycursor.execute(sql_query, (model_no, type_input, pieces_input))
            self.mydb.commit()
            print("Product registered successfully")
        else:
            print('That product already exists')
    def add_Order(self):
        model_no = input("Enter model_no: ")
        model_no = model_no.upper()
        if self.check_Model_No(model_no):
            quantity=int(input("Enter quantity"))
            while (quantity<=0):
                print("Enter a valid quantity")
                quantity=int(input("Enter quantity"))
            today=date.today()
            status="PENDING"
            order_id=self.get_Order_Id()
            sql_query = "INSERT INTO orders (order_id, model_no, order_date,order_status,quantity) VALUES (%s, %s, %s,%s,%s)"
            self.mycursor.execute(sql_query, (order_id,model_no,today,status,quantity))
            self.mydb.commit()
            print("Order added successfully")
        else:
            print("The Product doesnot exist.")
    def check_Stock(self):
        print("Enter product's Model number whose stock you want to check")
        model_no = input().upper()
        if self.check_Model_No(model_no):
            self.mycursor.execute("SELECT stock FROM product where model_no= %s",(model_no,))
            myresult = self.mycursor.fetchone()
            print("In Stock : ",myresult[0])
        else:
            print("That product doesnt exists")
    def add_Stock(self):
        print("Enter product's Model number whose stock you want to add")
        model_no = input().upper()
        if self.check_Model_No(model_no):
            quantity=int(input("Enter quantity of production"))
            while(quantity<=0):
                print("Enter valid quantity")
                quantity=int(input("Enter quantity of production"))
            self.mycursor.execute("update product set stock=stock+ %s where model_no= %s",(quantity,model_no))
            myresult = self.mycursor.fetchone()
            self.mydb.commit()
        else:
            print("That product doesn't exists")
    def check_Order_Status(self):
        self.mycursor.execute("SELECT * FROM orders")
        myresult = self.mycursor.fetchall()  
        for x in myresult:
            print("Order ID: ", x[0]," Model_No: ",x[1]," Quantity: ",x[4], " Order Date: ",x[2], " Status: ",x[3])
    def check_Pending_Orders(self):
        self.mycursor.execute("SELECT * FROM orders where order_status='PENDING'")
        myresult = self.mycursor.fetchall()  
        for x in myresult:
            print("Order ID: ", x[0]," Model_No: ",x[1]," Quantity: ",x[4], " Order Date: ",x[2], " Status: ",x[3])
    def complete_Order(self):
        self.mycursor.execute("Select * from orders where order_status='pending'")
        myresult=self.mycursor.fetchall()
        orders=[]
        for x in myresult:
            orders.append(x[0])
            print("Order ID: ", x[0]," Model_No: ",x[1]," Quantity: ",x[4], " Order Date: ",x[2], " Status: ",x[3])
        inp=int(input("Enter order which you want to complete y"))
        print(orders)
        print(inp)
        for id in orders:
            if id==inp:
                self.mycursor.execute("Update orders set order_status='COMPLETED',completed_date= %s where order_id=%s",(date.today(),inp,))
                self.mydb.commit()
        

    def check_Model_No(self,model_no):
        self.mycursor.execute("SELECT model_no FROM product where model_no= %s",(model_no,))
        myresult = self.mycursor.fetchone()
        if myresult:
            return True
        else:
            return False
    def get_Order_Id(self):
        self.mycursor.execute("SELECT MAX(order_id) FROM orders;")
        myresult=self.mycursor.fetchone()
        return (int(myresult[0])+1)     
i=Inventory_Management()