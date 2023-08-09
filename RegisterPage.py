from tkinter import *
from PIL import ImageTk, Image
import subprocess
from tkinter import messagebox
import sqlalchemy
import pymysql


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


class go_to_loginpage_or_Posts:
    def go_to_login():
        window.destroy()
        subprocess.call(["python", "LoginPage.py"])

    def go_to_Posts(conn, name, password, role, first_name, last_name):
        user = name
        userexists = sqlalchemy.text(
            f"SELECT COUNT(*) FROM data_network._user WHERE username = '{name}' "
        )
        transform_userexists = conn.execute(userexists)
        for i in transform_userexists:
            r = (1,)
            if name and password and role and first_name and last_name != "":
                if r != i:
                    query = (
                        meta.tables["_user"]
                        .insert()
                        .values(
                            username=f"{name}",
                            user_password=f"{password}",
                            user_role=f"{role}",
                            user_first_name=f"{first_name}",
                            user_last_name=f"{last_name}",
                        )
                    )
                    conn.execute(query)
                    conn.commit()
                    window.destroy()
                    subprocess.call(["python", "LoginPage.py"])
                    s = name
                else:
                    messagebox.showinfo(
                        title="Error", message="username already exists"
                    )
            else:
                messagebox.showinfo(
                    title="Error", message="you didn't put all requirements"
                )


class RegisterPage:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0, 0)
        self.window.state("zoomed")
        self.window.title("Register Page")

        # background image
        self.bg_frame = Image.open("background.png")  # sourc
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.First_fram = Label(self.window, image=photo)
        self.First_fram.image = photo  # setup
        self.First_fram.pack(fill="both", expand=True)  # photo fill window

        # Login Frame
        self.lgn_frame = Frame(self.window, bg="#040405", width=950, height=600)
        self.lgn_frame.place(x=200, y=70)
        self.heading = Label(
            self.lgn_frame,
            text="WELCOME",
            font=("yu gothic ui", 25, "bold"),
            bg="#040405",
            fg="white",
            bd=5,
            relief=FLAT,
        )
        self.heading.place(x=80, y=30, width=300, height=30)

        # Left Side Image
        self.side_image = Image.open("vector.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # Sign In Image
        self.sign_in_image = Image.open("hyy.png")
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=30)

        # creat new acount label
        self.sign_in_label = Label(
            self.lgn_frame,
            text="Creat new acount",
            bg="#040405",
            fg="white",
            font=("yu gothic ui", 17, "bold"),
        )
        self.sign_in_label.place(x=610, y=130)

        # First name
        self.First_name_label = Label(
            self.lgn_frame,
            text="First name",
            bg="#040405",
            fg="#4f4e4d",
            font=("yu gothic ui", 13, "bold"),
        )
        self.First_name_label.place(x=550, y=170)

        self.First_name_entry = Entry(
            self.lgn_frame,
            highlightthickness=0,
            relief=FLAT,
            bg="#040405",
            fg="#6b6a69",
            font=("yu gothic ui ", 12, "bold"),
            insertbackground="#6b6a69",
        )
        self.First_name_entry.place(x=580, y=200, width=270)

        self.First_name_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.First_name_line.place(x=550, y=221)

        # Last_name
        self.Last_name_label = Label(
            self.lgn_frame,
            text="Last name",
            bg="#040405",
            fg="#4f4e4d",
            font=("yu gothic ui", 13, "bold"),
        )
        self.Last_name_label.place(x=550, y=230)

        self.Last_name_entry = Entry(
            self.lgn_frame,
            highlightthickness=0,
            relief=FLAT,
            bg="#040405",
            fg="#6b6a69",
            font=("yu gothic ui ", 12, "bold"),
            insertbackground="#6b6a69",
        )
        self.Last_name_entry.place(x=580, y=260, width=270)

        self.Last_name_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.Last_name_line.place(x=550, y=281)

        # username
        self.username_label = Label(
            self.lgn_frame,
            text="Username",
            bg="#040405",
            fg="#4f4e4d",
            font=("yu gothic ui", 13, "bold"),
        )
        self.username_label.place(x=550, y=290)

        self.username_entry = Entry(
            self.lgn_frame,
            highlightthickness=0,
            relief=FLAT,
            bg="#040405",
            fg="#6b6a69",
            font=("yu gothic ui ", 12, "bold"),
            insertbackground="#6b6a69",
        )
        self.username_entry.place(x=580, y=320, width=270)

        self.username_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.username_line.place(x=550, y=341)

        # password
        self.password_label = Label(
            self.lgn_frame,
            text="Password",
            bg="#040405",
            fg="#4f4e4d",
            font=("yu gothic ui", 13, "bold"),
        )
        self.password_label.place(x=550, y=350)

        self.password_entry = Entry(
            self.lgn_frame,
            highlightthickness=0,
            relief=FLAT,
            bg="#040405",
            fg="#6b6a69",
            font=("yu gothic ui", 12, "bold"),
            show="*",
            insertbackground="#6b6a69",
        )
        self.password_entry.place(x=580, y=380, width=244)

        self.password_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.password_line.place(x=550, y=401)

        # show/hide password
        self.show_image = ImageTk.PhotoImage(file="show.png")

        self.hide_image = ImageTk.PhotoImage(file="hide.png")

        self.show_button = Button(
            self.lgn_frame,
            image=self.show_image,
            command=self.show,
            relief=FLAT,
            activebackground="white",
            borderwidth=0,
            background="white",
            cursor="hand2",
        )
        self.show_button.place(x=860, y=380)

        self.Role_label_rg = Label(
            self.lgn_frame,
            text="Role:",
            font=("yu gothic ui", 12, "bold"),
            bg="#040405",
            fg="#4f4e4d",
        )
        self.Role_label_rg.place(x=550, y=417)

        self.Role = StringVar()

        self.admin_radiobutton = Radiobutton(
            self.lgn_frame,
            text="admin",
            font=("yu gothic ui", 14, "bold"),
            variable=self.Role,
            value="1",
            bg="#040405",
            fg="#4f4e4d",
            activebackground="black",
            activeforeground="white",
        )
        self.admin_radiobutton.place(x=600, y=410)

        self.user_radiobutton = Radiobutton(
            self.lgn_frame,
            text="user",
            font=("yu gothic ui", 14, "bold"),
            variable=self.Role,
            value="0",
            bg="#040405",
            fg="#4f4e4d",
            activebackground="black",
            activeforeground="white",
        )
        self.user_radiobutton.place(x=700, y=410)

        # creat_button
        self.creat_button = Image.open("btn1.png")
        photo = ImageTk.PhotoImage(self.creat_button)
        self.creat_button_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.creat_button_label.image = photo
        self.creat_button_label.place(x=550, y=450)
        self.login = Button(
            self.creat_button_label,
            text="CREAT",
            font=("yu gothic ui", 13, "bold"),
            width=25,
            bd=0,
            bg="#3047ff",
            cursor="hand2",
            activebackground="#3047ff",
            fg="white",
            command=lambda: go_to_loginpage_or_Posts.go_to_Posts(
                connection,
                self.username_entry.get(),
                self.password_entry.get(),
                self.Role.get(),
                self.First_name_entry.get(),
                self.Last_name_entry.get(),
            ),
        )
        self.login.place(x=20, y=10)

        # Sign i
        self.sign_label = Label(
            self.lgn_frame,
            text="Have an account ?",
            font=("yu gothic ui", 11, "bold"),
            relief=FLAT,
            borderwidth=0,
            background="#040405",
            fg="white",
        )
        self.sign_label.place(x=570, y=540)

        self.signup_img = ImageTk.PhotoImage(file="log.png")
        self.signup_button_label = Button(
            self.lgn_frame,
            image=self.signup_img,
            bg="#98a65d",
            cursor="hand2",
            borderwidth=0,
            background="#040405",
            activebackground="#040405",
            command=go_to_loginpage_or_Posts.go_to_login,
        )
        self.signup_button_label.place(x=695, y=535, width=111, height=35)

    def show(self):
        self.hide_button = Button(
            self.lgn_frame,
            image=self.hide_image,
            command=self.hide,
            relief=FLAT,
            activebackground="white",
            borderwidth=0,
            background="white",
            cursor="hand2",
        )
        self.hide_button.place(x=860, y=380)
        self.password_entry.config(show="")

    def hide(self):
        self.show_button = Button(
            self.lgn_frame,
            image=self.show_image,
            command=self.show,
            relief=FLAT,
            activebackground="white",
            borderwidth=0,
            background="white",
            cursor="hand2",
        )
        self.show_button.place(x=860, y=380)
        self.password_entry.config(show="*")


def page():
    RegisterPage(window)
    window.mainloop()


if __name__ == "__main__":
    page()
