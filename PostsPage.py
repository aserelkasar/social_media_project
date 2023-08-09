from tkinter import *
from PIL import ImageTk, Image
import subprocess
import ttkbootstrap as ttk
import tkinter.ttk as tk
import sqlalchemy
import pymysql

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

logined_user = ""
with open("user.txt", "r") as rb:
    logined_user = rb.readline()


class go_to_Profilepage_or_addpost:
    def go_to_profile():
        window.destroy()
        subprocess.call(["python", "ProfilePage.py"])

    def go_to_addpost():
        window.destroy()
        subprocess.call(["python", "add_post.py"])

    def go_to_comments(post_id):
        with open("post.txt", "w") as ps:
            ps.write(f"{post_id}")
        window.destroy()
        subprocess.call(["python", "CommentsPage.py"])

    def go_to_login():
        window.destroy()
        subprocess.call(["python", "LoginPage.py"])


class PostsPage:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0, 0)
        self.window.state("zoomed")
        self.window.title("Posts Page")
        self.window.configure(bg="#040405")
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
            command=go_to_Profilepage_or_addpost.go_to_profile,
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

        self.frame = Frame(self.window, width=550, bg="#040405")
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.frame_canvas = Frame(self.frame, bg="#fff")
        self.frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky="nw")
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)

        # Add a canvas in that frame
        self.canvas = Canvas(
            self.frame_canvas, bd=0, highlightthickness=0, relief="ridge", width=550
        )
        self.canvas.grid(row=0, column=0, sticky="news")
        self.canvas.config(bg="#fff")
        self.vsb = Scrollbar(
            self.frame_canvas,
            orient="vertical",
            command=self.canvas.yview,
            bg="#fff",
        )
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.vsb.set)

        # Create a frame to contain the buttons
        self.frame_buttons = Frame(self.canvas, bg="#fff", width=550)
        self.canvas.create_window((0, 0), window=self.frame_buttons, anchor="nw")

        self.frame_buttons.update_idletasks()

        self.frame_canvas.config(width=550, height=200)

        # Set the canvas scrolling region
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.posts_selected = sqlalchemy.text("SELECT * FROM data_network._post ")
        self.transform_posts_selected = connection.execute(self.posts_selected)

        m = 0
        c = []
        for i in self.transform_posts_selected:
            m += 1
            c.append(i)

        for dd in range(m):
            PostsPage.post_maker(
                self.frame_buttons,
                dd,
                self.canvas,
                c[dd][3],
                c[dd][2],
                c[dd][1],
                c[dd][0],
            )
        self.frame_buttons.update_idletasks()

        # Set the canvas scrolling region
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.add_image = Image.open("add-button.png")
        photo = ImageTk.PhotoImage(self.add_image)
        self.add_image_Button = Button(
            self.window,
            image=photo,
            bg="#040405",
            border=0,
            activebackground="#040405",
            command=go_to_Profilepage_or_addpost.go_to_addpost,
        )
        self.add_image_Button.image = photo
        self.add_image_Button.place(relx=0.9, rely=0.85)

    def post_maker(window, y, canvas, name, postcontent, postname, id):
        post_frame = Frame(window, width=500, height=180, bg="#424242")
        post_frame.grid(row=y, column=2, sticky="news", pady=30, padx=20)
        small_profile_img = Image.open("small_profile_img.png")
        photo = ImageTk.PhotoImage(small_profile_img)
        small_profile_img_button = Button(
            post_frame,
            image=photo,
            bg="#424242",
            border=0,
            activebackground="#424242",
        )
        small_profile_img_button.image = photo
        small_profile_img_button.place(relx=0.02, y=7)

        post_username = Label(
            post_frame,
            text=f"{name}",
            fg="white",
            bg="#424242",
            font=("yu gothic ui", 17, "bold"),
        )
        post_username.place(relx=0.15, y=10)
        circles_frame = Frame(post_frame, bg="#424242")
        circles_frame.place(relx=0.8, y=7, width=90, height=100)
        post_name = Label(
            post_frame,
            text=f"{postname}",
            fg="white",
            bg="#424242",
            font=("yu gothic ui", 17, "bold"),
        )

        post_name.place(
            relx=0.5,
            y=10,
            anchor=N,
        )
        main_frame = Frame(post_frame, bg="#424242")
        main_frame.place(
            relx=0.5,
            rely=0.78,
            anchor=CENTER,
        )
        post_content_canvas = Canvas(
            main_frame,
            bd=0,
            highlightthickness=0,
            relief="ridge",
            height=70,
            width=480,
            bg="#424242",
        )
        post_content_canvas.grid(
            row=0,
            column=0,
        )
        vsb = Scrollbar(
            main_frame,
            orient="vertical",
            command=post_content_canvas.yview,
            bg="#424242",
        )
        post_content_canvas.configure(yscrollcommand=vsb.set)
        post_content_frame = Frame(post_content_canvas, bg="#424242")
        post_content_canvas.create_window(
            (0, 0), window=post_content_frame, anchor="nw"
        )

        post_content = Label(
            post_content_frame,
            text=f"{postcontent}",
            fg="white",
            bg="#424242",
            font=("yu gothic ui", 14, "bold"),
        )
        post_content.place(
            relx=0.01,
            rely=0.05,
            anchor=NW,
        )
        post_content.text = ""
        vsb.grid(row=0, column=1, sticky="ns")
        post_content_frame.update_idletasks()
        post_content_frame.config(width=550, height=post_content.winfo_height())

        post_content_canvas.config(scrollregion=post_content_canvas.bbox("all"))

        def show_or_hide_frame():
            role = sqlalchemy.text(
                f"SELECT user_role FROM data_network._user WHERE username = '{logined_user}' "
            )
            transform_role = connection.execute(role)
            for i in transform_role:
                g = i
            l = (0,)
            frame = Frame(circles_frame, bg="#fff", width=90, height=55)
            d = bool(frame.winfo_exists())

            frame.place(rely=0.4, relx=0)

            def delete_frame():
                post_frame.grid_forget()
                post_content_frame.update_idletasks()
                canvas.config(scrollregion=canvas.bbox("all"))
                comment_delete = sqlalchemy.text(
                    f"DELETE FROM data_network._comment WHERE id_of_post = '{id}' "
                )
                transform_comment_delete = connection.execute(comment_delete)
                post_delete = sqlalchemy.text(
                    f"DELETE FROM data_network._post WHERE post_id = '{id}' "
                )
                transform_post_delete = connection.execute(post_delete)
                connection.commit()

            def comment():
                with open("post.txt", "w") as ps:
                    ps.write(f"{id}")

            delete = Button(
                frame,
                bg="#fff",
                border=0,
                text="delete",
                foreground="black",
                activebackground="#fff",
                command=delete_frame,
                font=("yu gothic ui", 15, "bold"),
            )
            if g != l:
                delete.place(relx=0.5, rely=0.15, anchor=CENTER)
            elif name == logined_user:
                delete.place(relx=0.5, rely=0.15, anchor=CENTER)
            comment_button = Button(
                frame,
                bg="#fff",
                border=0,
                text="comment",
                foreground="black",
                activebackground="#fff",
                command=lambda: go_to_Profilepage_or_addpost.go_to_comments(id),
                font=("yu gothic ui", 15, "bold"),
            )
            if g == l and logined_user != name:
                comment_button.place(relx=0.5, rely=0.5, anchor=CENTER)
            else:
                comment_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        circles = Image.open("circles.png")
        photo = ImageTk.PhotoImage(circles)
        circles_button = Button(
            circles_frame,
            image=photo,
            bg="#424242",
            border=0,
            activebackground="#424242",
            command=show_or_hide_frame,
            width=90,
            height=46,
        )
        circles_button.image = photo
        circles_button.place(relx=0, rely=-0.05)


def page():
    PostsPage(window)
    window.mainloop()


if __name__ == "__main__":
    page()
