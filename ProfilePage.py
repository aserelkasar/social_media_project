from tkinter import *
from PIL import ImageTk, Image
import sqlalchemy
import pymysql
import subprocess

name = ""
with open("user.txt", "r") as rb:
    name = rb.readline()

DATABASE_TYPE = "mysql+pymysql"
USERNAME = "root"
PASSWORD = "aseraser00"
HOST = "localhost"
PORT = "3306"
DATABASE_NAME = "data_network"

DB_URI = f"{DATABASE_TYPE}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"

engine = sqlalchemy.create_engine(DB_URI)
connection = engine.connect()
meta = sqlalchemy.MetaData()
meta.reflect(engine)
window = Tk()


class ProfilePage:
    def __init__(self, conn, window, name):
        self.window = window
        self.window.resizable(0, 0)
        self.window.state("zoomed")
        self.window.title("profile")
        user_get = sqlalchemy.text(
            f"SELECT * FROM data_network._user WHERE username = '{name}' "
        )
        transform_user_get = conn.execute(user_get)
        user_password = ""
        first_name = ""
        last_name = ""
        for i in transform_user_get:
            user_password = i[1]
            first_name = i[3]
            last_name = i[4]
        self.bg_frame = Image.open("background.png")  # sourc
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.First_fram = Label(self.window, image=photo)
        self.First_fram.image = photo  # setup
        self.First_fram.pack(fill="both", expand=True)
        # Frame
        self.lgn_frame = Frame(self.First_fram, bg="#040405", width=500, height=600)
        self.lgn_frame.pack(expand=True)
        # Sign In Image
        self.image = Image.open("hyy.png")
        photo = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.image_label.image = photo
        self.image_label.place(
            relx=0.5, rely=0.25, anchor=CENTER, width=100, height=100
        )

        # First name
        self.First_name_label = Label(
            self.lgn_frame,
            text=f"First name : {first_name}",
            bg="#040405",
            fg="white",
            font=("yu gothic ui", 13, "bold"),
        )
        self.First_name_label.place(relx=0.30, rely=0.40, anchor=W)

        # Last_name
        self.Last_name_label = Label(
            self.lgn_frame,
            text=f"Last name : {last_name}",
            bg="#040405",
            fg="white",
            font=("yu gothic ui", 13, "bold"),
        )
        self.Last_name_label.place(relx=0.30, rely=0.50, anchor=W)

        # username
        self.username_label = Label(
            self.lgn_frame,
            text=f"Username : {name}",
            bg="#040405",
            fg="white",
            font=("yu gothic ui", 13, "bold"),
        )
        self.username_label.place(relx=0.30, rely=0.60, anchor=W)

        # password
        self.password_label = Label(
            self.lgn_frame,
            text=f"Password : {user_password}",
            bg="#040405",
            fg="white",
            font=("yu gothic ui", 13, "bold"),
        )

        self.password_label.place(relx=0.30, rely=0.70, anchor=W)

        def go_to_login():
            window.destroy()
            subprocess.call(["python", "LoginPage.py"])

        self.image2 = Image.open("check-out.png")
        photo2 = ImageTk.PhotoImage(self.image2)
        self.image_button = Button(
            self.lgn_frame,
            image=photo2,
            bg="#040405",
            activebackground="#040405",
            bd=0,
            command=go_to_login,
        )
        self.image_button.image = photo2
        self.image_button.place(
            relx=0.9, rely=0.9, anchor=CENTER, width=100, height=100
        )
        if self.image_button == "3 lines.png":
            print(self.First_fram)


def page():
    ProfilePage(connection, window, name)
    window.mainloop()


if __name__ == "__main__":
    page()
