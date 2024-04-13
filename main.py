import mysql.connector
from mysql.connector import Error

def connect_to_database(username, password):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='travel_itinerary',
            user=username,
            password=password
        )
        if connection.is_connected():
            print("Connection established.")
            return connection
    except Error as e:
        print("Incorrect credentials or error: ", e)
        return None

def call_addtraveller(connection, email, mobile, fname, lname, gen, dob, unit, street, street_no, city, state, zip):
    try:
        cursor = connection.cursor()
        cursor.callproc('AddTraveller', [email, mobile, fname, lname, gen, dob, unit, street, street_no, city, state, zip])
        connection.commit()
        print("Traveller added successfully.")
    except Error as e:
        print("Failed to add traveller: ", e)
    finally:
        cursor.close()

def call_gettravellerbyemail(connection, email, password):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetTravellerByEmail', [email])
        valid = False
        for result in cursor.stored_results():
            traveller = result.fetchone()
            if traveller:
                if traveller[1] == password:
                    print("Login successful!")
                    print("Traveller Details:")
                    columns = [desc[0] for desc in cursor.description]
                    for col, val in zip(columns, traveller):
                        print(f"{col}: {val}")
                    valid = True
                else:
                    print("Incorrect password.")
        if not valid:
            print("Login failed. Incorrect email or password.")
    except Error as e:
        print("Failed to retrieve traveller: ", e)
    finally:
        cursor.close()

def main():
    username = 'root'
    password = 'Anvitha@2024'
    connection = connect_to_database(username, password)
    if connection:
        try:
            call_addtraveller(connection, 'example@email.com', '0123456789', 'John', 'Doe', 'Male', '1980-01-01', 101, 'Some St', 123, 'Some City', 'Some State', '12345')
            call_gettravellerbyemail(connection, 'example@email.com', '0123456789')
        finally:
            if connection.is_connected():
                connection.close()
                print("Disconnected from the database.")

if __name__ == "__main__":
    main()
