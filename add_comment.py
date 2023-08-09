from tkinter import *
from PIL import ImageTk, Image
import subprocess
import ttkbootstrap as ttk
import tkinter.ttk as tk
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

logined_user = ""
with open("user.txt", "r") as rb:
    logined_user = rb.readline()


post_id = ""
with open("post.txt", "r") as rd:
    post_id = rd.readline()


class go_to_Profilepage:
    def go_to_profile():
        window.destroy()
        subprocess.call(["python", "ProfilePage.py"])

    def go_to_posts():
        window.destroy()
        subprocess.call(["python", "CommentsPage.py"])


class CommentsPage:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0, 0)
        self.window.state("zoomed")
        self.window.title("add comment")
        self.window.configure(bg="#080310")
        # header
        self.headerframe = Frame(self.window, height=120, bg="#02080F")
        self.headerframe.pack(fill="x")
        self.profile_image = Image.open("hyy.png")
        photo = ImageTk.PhotoImage(self.profile_image)
        self.profile_image_Button = Button(
            self.headerframe,
            image=photo,
            bg="#02080F",
            border=0,
            activebackground="#02080F",
            command=go_to_Profilepage.go_to_profile,
        )
        self.profile_image_Button.image = photo
        self.profile_image_Button.place(x=20, y=10)

        self.profile_name = Label(
            self.headerframe,
            text=f"{logined_user}",
            fg="white",
            bg="#02080F",
            font=("yu gothic ui", 17, "bold"),
        )
        self.profile_name.place(x=180, y=45)
        self.back = Image.open("back.png")
        photo = ImageTk.PhotoImage(self.back)
        self.back_button = Button(
            self.headerframe,
            image=photo,
            bg="#02080F",
            border=0,
            activebackground="#02080F",
            command=go_to_Profilepage.go_to_posts,
        )
        self.back_button.image = photo
        self.back_button.place(relx=0.9, y=35)

        self.frame = Frame(self.window, height=350, width=550, bg="#040405")
        self.frame.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.comment_content = Label(
            self.frame,
            text="Comment content",
            bg="#040405",
            fg="white",
            font=("yu gothic ui", 13, "bold"),
        )
        self.comment_content.place(relx=0.2, rely=0.15)

        self.comment_content_entry = Text(
            self.frame,
            highlightthickness=0,
            relief=FLAT,
            bg="#fff",
            fg="black",
            font=("yu gothic ui ", 13, "bold"),
            insertbackground="black",
            width=30,
            height=10,
        )
        self.comment_content_entry.place(relx=0.21, rely=0.3)

        def insert_into_comments():
            CommentsPage.comment_maker(self.comment_content_entry.get(1.0, END))
            window.destroy()
            subprocess.call(["python", "CommentsPage.py"])

        self.add_image = Image.open("small-add-button.png")
        photo = ImageTk.PhotoImage(self.add_image)
        self.add_image_Button = Button(
            self.frame,
            image=photo,
            bg="#040405",
            border=0,
            activebackground="#040405",
            command=insert_into_comments,
        )

        self.add_image_Button.image = photo
        self.add_image_Button.place(relx=0.8, rely=0.75)

    def comment_maker(
        commentcontent,
    ):
        if commentcontent != "":
            query = (
                meta.tables["_comment"]
                .insert()
                .values(
                    comment_content=f"{commentcontent}",
                    id_of_post=f"{post_id}",
                    comment_username=f"{logined_user}",
                )
            )
            connection.execute(query)
            connection.commit()


window = Tk()


def page():
    CommentsPage(window)
    window.mainloop()


if __name__ == "__main__":
    page()
