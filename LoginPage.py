from tkinter import *
from PIL import ImageTk, Image
import subprocess
import sqlalchemy
import pymysql
from tkinter import messagebox

window = Tk()

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


class go_to_registerpage_or_posts:
    def go_to_register():
        window.destroy()
        subprocess.call(["python", "RegisterPage.py"])

    def go_to_Posts(conn, name, password):
        with open("user.txt", "w") as wr:
            wr.write(f"{name}")
        userexists = sqlalchemy.text(
            f"SELECT COUNT(*) FROM data_network._user WHERE username = '{name}' "
        )
        transform_userexists = conn.execute(userexists)
        passwordexists = sqlalchemy.text(
            f"SELECT COUNT(*) FROM data_network._user WHERE user_password = '{password}' "
        )
        transform_passwordexists = conn.execute(passwordexists)
        for i in transform_userexists:
            r = (1,)
            z = (0,)
            if name and password != "":
                if i == r:
                    for k in transform_passwordexists:
                        if k != z:
                            window.destroy()
                            subprocess.call(["python", "PostsPage.py"])
                        else:
                            message = messagebox.askquestion(
                                title="Error",
                                message=f"password is incorrect , did you forgot password ",
                            )
                            if message == "yes":
                                passwordforgot = sqlalchemy.text(
                                    f"SELECT user_password FROM data_network._user WHERE username= '{name}' "
                                )
                                transform_passwordforgot = conn.execute(passwordforgot)
                                for i in transform_passwordforgot:
                                    pas = i
                                messagebox.showinfo(
                                    title="password",
                                    message=f"your password is : {pas}",
                                )

                else:
                    messagebox.showinfo(title="Error", message="username is incorrect")
            else:
                messagebox.showinfo(
                    title="Error", message="you didn't put all requirements"
                )


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0, 0)
        self.window.state("zoomed")
        self.window.title("Login Page")

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
        self.sign_in_image_label.place(x=620, y=130)

        # Sign In label
        self.sign_in_label = Label(
            self.lgn_frame,
            text="Sign In",
            bg="#040405",
            fg="white",
            font=("yu gothic ui", 17, "bold"),
        )
        self.sign_in_label.place(x=650, y=240)

        # username
        self.username_label = Label(
            self.lgn_frame,
            text="Username",
            bg="#040405",
            fg="#4f4e4d",
            font=("yu gothic ui", 13, "bold"),
        )
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(
            self.lgn_frame,
            highlightthickness=0,
            relief=FLAT,
            bg="#040405",
            fg="#6b6a69",
            font=("yu gothic ui ", 12, "bold"),
            insertbackground="#6b6a69",
        )
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.username_line.place(x=550, y=359)
        # Username icon
        self.username_icon = Image.open("username_icon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # login button
        self.lgn_button = Image.open("btn1.png")
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(
            self.lgn_button_label,
            text="LOGIN",
            font=("yu gothic ui", 13, "bold"),
            width=25,
            bd=0,
            bg="#3047ff",
            cursor="hand2",
            activebackground="#3047ff",
            fg="white",
            command=lambda: go_to_registerpage_or_posts.go_to_Posts(
                connection, self.username_entry.get(), self.password_entry.get()
            ),
        )
        self.login.place(x=20, y=10)

        # Sign Up
        self.sign_label = Label(
            self.lgn_frame,
            text="No account yet?",
            font=("yu gothic ui", 11, "bold"),
            relief=FLAT,
            borderwidth=0,
            background="#040405",
            fg="white",
        )
        self.sign_label.place(x=575, y=540)

        self.signup_img = ImageTk.PhotoImage(file="register.png")
        self.signup_button_label = Button(
            self.lgn_frame,
            image=self.signup_img,
            bg="#98a65d",
            cursor="hand2",
            borderwidth=0,
            background="#040405",
            activebackground="#040405",
            command=go_to_registerpage_or_posts.go_to_register,
        )
        self.signup_button_label.place(x=695, y=535, width=111, height=35)

        # password
        self.password_label = Label(
            self.lgn_frame,
            text="Password",
            bg="#040405",
            fg="#4f4e4d",
            font=("yu gothic ui", 13, "bold"),
        )
        self.password_label.place(x=550, y=380)

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
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0
        )
        self.password_line.place(x=550, y=440)
        # Password icon
        self.password_icon = Image.open("password_icon.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg="#040405")
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
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
        self.show_button.place(x=860, y=420)

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
        self.hide_button.place(x=860, y=420)
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
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show="*")


def page():
    LoginPage(window)
    window.mainloop()


if __name__ == "__main__":
    page()
