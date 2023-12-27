from DatabaseConnection import create_connection
from CMSException import TrackingNumberNotFoundException,InvalidEmployeeIdException
import random
from ICourierUserService import ICourierUserService
#  CourierID,SenderName,SenderAddress,ReceiverName,ReceiverAddress|
#  Weight,Statu,TrackingNumber,DeliveryDate
class Courier(ICourierUserService):
    courier_track = random.randint(1000,2000)
    def __init__(self, CourierID, SenderName, SenderAddress, ReceiverName, RecieverAddress, Weight,Status="In Transit",Deliverydate="2023-12-12"):
        self.CourierID = CourierID
        self.SenderName = SenderName
        self.SenderAddress = SenderAddress
        self.ReceiverName = ReceiverName
        self.RecieverAddress = RecieverAddress
        self.Weight = Weight
        self.Status = Status
        self.Deliverydate = Deliverydate
        Courier.courier_track=Courier.courier_track+1
    @staticmethod
    def get_courier_info(courier_id):
        connection = create_connection()
        cur = connection.cursor()
        q1 = "select * from courier where CourierID=%s;"
        q2   = (courier_id,)
        cur.execute(q1,q2)
        val = cur.fetchall()
        for  i in val:
          print(f" COURIER ID  :  {i[0]}")
          print(f" SENDER NAME  :  {i[1]}")
          print(f" SENDER ADDRESS :  {i[2]}")
          print(f" RECEIVER NAME  :  {i[3]}")
          print(f" RECEIVER ADDRESS :  {i[4]}")
          print(f" WEIGHT  :  {i[5]}")
          print(f" STATUS  :  {i[6]}")
          print(f" TRACKING NUMBER  :  {i[7]}")
          print(f" DELIVERY DATE  :  {i[8]}")

        connection.close()

    def order_status(self, courier_id):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        try:
            cur.execute("select CourierID  from courier ")
            q1  = cur.fetchall()
            if (courier_id,) not in q1:
                raise Exception("Invalid Courier ID inserted ")
            cur.execute("select  status from courier where CourierID  = %s",(courier_id,))
            info = cur.fetchone()
            print(f"Order Status  :  {info[0]}")
        except Exception as e:
            print(f"Exception Details  : {e}")
        finally:
            connection.close()

    def Categories_parcel(self):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        try:
            cur.execute("select weight,CourierID from courier")
            info = cur.fetchall()
            for i in info:
              if i[0] <= 1.80:
                 print(f"Courier : {i[1]} is Light Weight ")
              elif i[0] <= 2.80 and i[0] > 1.80:
                 print(f"Courier : {i[1]} is Medium Weight ")
              else:
                 print(f"Courier : {i[1]} is Heavy Weight ")
        except Exception as e:
            print(f"Exception Details  : {e}")
        finally:
            connection.close()

    def Track_order(self, TrackingNumber):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        try:
            cur.execute("select TrackingNumber from courier")
            tracking_number = cur.fetchall()
            if (TrackingNumber,) not in tracking_number:
                raise TrackingNumberNotFoundException("Invalid tracking number inserted ")
            cur.execute("select CourierID, Status from courier where TrackingNumber = %s", (TrackingNumber,))
            val = cur.fetchone()
            print(F"\n\n\t\tCOURIER {val[0]} IS {val[1]}")
        except Exception as e:
            print(f"Exception Details  : {e}")
        finally:
            connection.close()

    def calculate_delivery_Cost(self):
        try:
            connection = create_connection()
            cur = connection.cursor(buffered=True)
            courier_id = int(input("ENTER COURIER ID "))
            q1 = "select CourierID from courier"
            cur.execute(q1)
            info = cur.fetchall()
            if (courier_id,) not in info:
                raise Exception("Invalid Courier ID inserted ")
            distance = int(input("ENTER APPROX DISTANCE BETWEEN SENDER AND RECEIVER IN KM"))
            cur.execute("select weight from  courier where CourierID  = %s", (courier_id,))
            weight = cur.fetchone()
            print(f" TOTAL COST OF COURIER ID {courier_id} IS {weight[0] * distance}")
        except Exception as e:
            print(f"Exception Details  : {e}")
    def placeOrder(self):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        q1 = """insert into Courier(CourierID,SenderName,SenderAddress,ReceiverName,ReceiverAddress,
             Weight,Status,TrackingNumber,DeliveryDate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
        q2  = (self.CourierID,self.SenderName,self.SenderAddress,self.ReceiverName,self.RecieverAddress,self.Weight,self.Status,self.courier_track,self.Deliverydate)
        cur.execute(q1,q2)
        connection.commit()
        print("Order Placed !!for furthur details got  to our main menu ")
    def cancelOrder(self,courier_id):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        cur.execute("delete from payment where CourierID   = %s",(courier_id,))
        cur.execute("delete from courier where CourierID   = %s",(courier_id,))
        print("ORDER CANCELED SUCCESSFULLY !!! ")


