import mysql.connector


def get_connection():
    # Read the properties from the file
    with open(r'C:\Users\LENOVO\PycharmProjects\helloWorld\util\config.properties', 'r') as file:
        lines = file.readlines()
        properties = {}
        for line in lines:
            if '=' in line:
             key, value = line.strip().split('=',1)
             properties[key.strip()] = value.strip()

    # Create the connection string
    connection_string = f"mysql://{properties['username']}:{properties['password']}@{properties['hostname']}:{properties['port']}/{properties['dbname']}"

    try:
        connection = mysql.connector.connect(host=properties['hostname'],
                                             database=properties['dbname'],
                                             user=properties['username'],
                                             password=properties['password'])
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None
