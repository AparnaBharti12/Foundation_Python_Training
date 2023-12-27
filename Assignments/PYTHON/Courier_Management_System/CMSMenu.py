from CMSCourier import Courier

print("\n\n\t\t\t_____.WELCOME TO THE COURIER MANAGEMENT SYSTEM._____ ")
print("\n\n\nPRESS 1 TO PLACE A COURIER ORDER ")
print("PRESS 2 TO DISPLAY COURIER INFORMATION  ")
print("PRESS 3 TO DISPLAY ORDER STATUS ")
print("PRESS 4 SORT COURIER BASED ON WEIGHT ")
print("PRESS 5 TO TRACK AN COURIER  ")
print("PRESS 6 TO CALCULATE DELIVERY COST ")
print("PRESS 7 TO CANCEL COURIER ORDER ")

c = Courier(106, "anshul Verma", "13, XYZ Colony, kolkata", "riya sharma", "34, ABC Street ,Noida", 2.50,
            "In Transit", "2023 - 12 - 15")
ch = int(input("\n\n\t\t\tenter you choice here  :  "))
if ch==1:
    print("ENTER VALUES ")
    courierID  = int(input("ENTER COURIER ID : "))
    SenderName = input("ENTER SENDER NAME : ")
    SenderAddress = input("ENTER SENDER ADDRESS : ")
    ReceiverName = input("ENTER RECEIVER NAME : ")
    ReceiverAddress = input("ENTER RECEIVER ADDRESS : ")
    Weight  = int(input("ENTER COURIER WEIGHT : "))
    c_new = Courier(courierID,SenderName,SenderAddress,ReceiverName,ReceiverAddress,Weight)
    c_new.placeOrder()
if ch == 2:
    i = int(input("\n\nEnter your courier id "))
    Courier.get_courier_info(i)
if ch == 3:
    ID = int(input("ENTER COURIER ID   :  "))
    c.order_status(ID)
if ch == 4:
    c.Categories_parcel()
if ch==5:
    ID = input("ENTER TRACKING ID   :  ")
    c.Track_order(ID)
if ch==6:
    c.calculate_delivery_Cost()
if ch==7:
    courier_id   = int(input("ENTER COURIER ID "))
    c.cancelOrder(courier_id)