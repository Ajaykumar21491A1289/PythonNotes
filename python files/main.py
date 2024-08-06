import streamlit as st
import sqlite3
from passlib.hash import pbkdf2_sha256

# Function to create a user table in the database
def create_user_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Create a user table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Function to add a new user to the database
def add_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:
        # Hash the password before storing it
        hashed_password = pbkdf2_sha256.hash(password)

        # Insert user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))

        conn.commit()
        st.sidebar.success("Registration successful!")
    except sqlite3.IntegrityError:
        # This exception is raised if the username already exists
        st.sidebar.error("Username already exists. Please choose a different username.")
    finally:
        conn.close()
# Function to check if the username and password match a record in the database
def verify_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Retrieve the hashed password for the given username
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()

    conn.close()

    # If the username exists, verify the password
    if result:
        return pbkdf2_sha256.verify(password, result[0])

    return False


def fun():
    import streamlit as st
    import sqlite3 as sq
    connection = sq.connect("mydatabase.db")
    cursor = connection.cursor()
    st.title("ANNAPURNA DELUX LODGE")
    cursor.execute('''CREATE TABLE IF NOT EXISTS HM 
    (adharid INTEGER PRIMARY KEY,name TEXT,roomtype text,total integer,amountpaid integer,amount2 integer,room_no integer,total_persons integer,mobile INTEGER,address TEXT)''')

    def add_user(adharid, name, roomtype, total, amountpaid, amount2, room_no, total_persons, mobile, address):
        cursor.execute(
            "INSERT INTO HM(adharid,name,roomtype,total,amountpaid,amount2,room_no,total_persons,mobile,address) VALUES (?,?,?,?,?,?,?,?,?,?)",
            (adharid, name, roomtype, total, amountpaid, amount2, room_no, total_persons, mobile, address))
        connection.commit()

    def view_data():
        cursor.execute("SELECT * FROM HM")
        data = cursor.fetchall()
        return data

    st.write("Enter the customer Details")
    adharid = st.text_input("Enter Adhar number of the Customer")
    name = st.text_input("Enter Name of the Customer")
    roomtype = st.text_input("Enter the Room Type")
    room_no = st.text_input("Enter the room number")
    total = st.text_input("Enter the Total Amount")
    amountpaid = st.text_input("Enter the Advance Amount")
    amount2 = st.text_input("Enter Balance Amount")
    total_persons = st.text_input("Enter the Count Customers")
    mobile = st.text_input("Enter mobile number of customer")
    address = st.text_input("Enter The Address  of customer")
    if st.button("Check in"):
        add_user(adharid, name, roomtype, total, amountpaid, amount2, room_no, total_persons, mobile, address)
    if st.button("show the Data"):
        st.table(view_data())
# Streamlit UI
def main():
    st.title("Login Page")

    create_user_table()

    # Sidebar for registration
    st.sidebar.title("Register")
    new_username = st.sidebar.text_input("Username")
    new_password = st.sidebar.text_input("Password", type="password")
    register_button = st.sidebar.button("Register")

    # Register new user
    if register_button:
        add_user(new_username, new_password)
        st.sidebar.success("Registration successful!")

    # Main login form
    st.write("## Login")
    username = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")

    login_button = st.button("Login")

    # Check login credentials
    if login_button:
        if verify_user(username, password):
            st.success("Login successful!")
            fun()
        else:
            st.error("Login failed. Please check your credentials.")

if __name__ == "__main__":
    main()