import streamlit as st
import pandas as pd
# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()
def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False
# DB Management for normal users
import sqlite3 
conn = sqlite3.connect('user.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

#DB management for autoricksaw owners
conn2 = sqlite3.connect('auto.db')
c2 = conn2.cursor()
# DB  Functions
def create_usertable2():
    c2.execute('CREATE TABLE IF NOT EXISTS autotable(username TEXT,password TEXT)')


def add_userdata2(username,password):
    c2.execute('INSERT INTO autotable(username,password) VALUES (?,?)',(username,password))
    conn2.commit()

def login_user2(username,password):
    c2.execute('SELECT * FROM autotable WHERE username =? AND password = ?',(username,password))
    data = c2.fetchall()
    return data


def view_all_users2():
    c2.execute('SELECT * FROM autotable')
    data = c2.fetchall()
    return data

#DB management for online Users
conn3 = sqlite3.connect('online.db')
c3 = conn3.cursor()
# DB  Functions
def create_usertable3():
    conn3.execute('CREATE TABLE IF NOT EXISTS onlinetable(username TEXT,password TEXT)')


def add_userdata3(username,password):
    c3.execute('INSERT INTO onlinetable(username,password) VALUES (?,?)',(username,password))
    conn3.commit()

def login_user3(username,password):
    c3.execute('SELECT * FROM onlinetable WHERE username =? AND password = ?',(username,password))
    data = c3.fetchall()
    return data


def view_all_users3():
    c3.execute('SELECT username FROM onlinetable')
    data = c3.fetchall()
    return data

def go_offline(username):
    c3.execute('DELETE FROM onlinetable WHERE username = ?',(username))

def main():
    """Simple Login App"""

    st.title("Simple Login App")
    menu = ["Home","Login As User","Login As Autoricksaw","SignUp","SignUp As Autoricksaw "]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.subheader("Home")
    elif choice == "Login As User":
        st.subheader("Login Section")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login-Logout"):
            create_usertable()
            hashed_pswd = make_hashes(password)
            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:
                col1,col2 = st.columns(2)
                with col1:
                    st.success("Logged In as {}".format(username))
                with col2:
                    login_btn = st.button("Login")
                    if login_btn:
                        login_btn.text = ("Logout")
                task = st.selectbox("Task",["Get Nearby Hubs","Go Online","Go Offline","Profiles"])
                if task == "Get Nearby Hubs":
                    st.subheader("Add Your Post")
                elif task == "Go Online":
                    st.subheader("Your Location Will Be Shared With Nearby Autorickshaw")
                    create_usertable3()
                    add_userdata3(username,password)
                elif task == "Go Offline":
                    st.subheader("Making Your Location Private From Autorickshaw")
                    go_offline(username)
                elif task == "Profiles":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db=pd.DataFrame(user_result,columns=["Username","Password"])
                    st.dataframe(clean_db)

            else:
                st.warning("Incorrect Username/Password")
    elif choice == "Login As Autoricksaw":
        st.subheader("Login Section")
        username = st.sidebar.text_input("Auto-Owner Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login/Logout"):
            create_usertable2()
            hashed_pswd = make_hashes(password)
            result = login_user2(username,check_hashes(password,hashed_pswd))
            if result:
                st.success("Logged In as {}".format(username))
                task = st.selectbox("Task",["See Online Users","Analytics","Other Auto Profiles"])
                if task == "See Online Users":
                    st.subheader("Online Users")
                    user_result = view_all_users3()
                    clean_db=pd.DataFrame(user_result,columns=["Username"])
                    st.dataframe(clean_db)
                elif task == "Analytics":
                    st.subheader("Analytics")
                elif task == "Other Auto Profiles":
                    st.subheader("User Profiles")
                    user_result = view_all_users2()
                    clean_db=pd.DataFrame(user_result,columns=["Username","Password"])
                    st.dataframe(clean_db)
            else:
                st.warning("Incorrect Username/Password")
    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')
        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user,make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")
    elif choice == "SignUp As Autoricksaw ":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')
        if st.button("Signup"):
            create_usertable2()
            add_userdata2(new_user,make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")
main()