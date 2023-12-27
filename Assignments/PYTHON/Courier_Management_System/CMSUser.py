from DatabaseConnection import create_connection


class User:
    def __init__(self, id, name, email, password, contact_number, address):
        self.user_id = id
        self.name = name
        self.email = email
        self.password = password
        self.contact_number = contact_number
        self.address = address

    def validate_user(self):
        try:
            res = any(ch.isdigit() for ch in self.name)
            if res:
                raise Exception("Invalid Name Exception ")
            elif not self.name.istitle():
                raise Exception("Invalid Name Exception ")
            elif len(self.contact_number < 10):
                raise Exception("Invalid Name Exception ")
            else:
                print("User Information validated SuccessFully")
        except Exception as e:
            print(f"Exception Details  : {e}")

    def address_validator(self):
        str = ""
        val = self.address.split()
        for i in val:
            if i.isnumeric():
                str += "Zip Code " + i + " "
            else:
                str += i.title() + " "
        print(str)
    def generate_password(self):
        return self.name.title()+"@1234"
    def  Duplicate_address(self):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        cur.execute("select address from user where address=%s",self.address)
        val = cur.fetchall()
        if len(val)==0:
            print("NO DUPLICATE ADDRESS FOUND ")
        else:
            print(" DUPLICATE ADDRESS FOUND ")


# u = User(1, "aparna", "aparna@gmail.com", "aparna@1234", 123456, "parasia road  chhindwara 45655")
# u.address_validator()
