from tkinter import *
from tkinter import ttk
import dbbackend

class MusicDatabase:

    def __init__(self, root):
        self.root = root
        self.root.title("Music Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="#0077CC")  

        self.title = StringVar()
        self.artist = StringVar()
        self.genre = StringVar()
        self.release_year = StringVar()
        self.duration = StringVar()
        self.selected_record_id = None  

        dbbackend.create_music_table()

        self.create_widgets()

    def create_widgets(self):
    


        def add_music():
            dbbackend.add_music_record(self.title.get(), self.artist.get(), self.genre.get(),
                                        self.release_year.get(), self.duration.get())
            self.display_music()

        def on_select(event):
            selected_item = self.treeview.focus()
            if selected_item:
                self.selected_record_id = int(self.treeview.item(selected_item)['text'])

        def display_music():
            records = dbbackend.view_data()
            self.treeview.delete(*self.treeview.get_children())
            for record in records:
                self.treeview.insert("", "end", text=record[0], values=(record[1], record[2], record[3], record[4], record[5]))

        Label(self.root, text="Title:", bg="#0077CC", fg="#FFFFFF", font=('Arial', 16, 'bold')).grid(row=0, column=0, padx=10, pady=10)
        Entry(self.root, textvariable=self.title, font=('Arial', 16)).grid(row=0, column=1)
        Label(self.root, text="Artist:", bg="#0077CC", fg="#FFFFFF", font=('Arial', 16, 'bold')).grid(row=1, column=0, padx=10, pady=10)
        Entry(self.root, textvariable=self.artist, font=('Arial', 16)).grid(row=1, column=1)
        Label(self.root, text="Genre:", bg="#0077CC", fg="#FFFFFF", font=('Arial', 16, 'bold')).grid(row=2, column=0, padx=10, pady=10)
        Entry(self.root, textvariable=self.genre, font=('Arial', 16)).grid(row=2, column=1)
        Label(self.root, text="Release Year:", bg="#0077CC", fg="#FFFFFF", font=('Arial', 16, 'bold')).grid(row=3, column=0, padx=10, pady=10)
        Entry(self.root, textvariable=self.release_year, font=('Arial', 16)).grid(row=3, column=1)
        Label(self.root, text="Duration:", bg="#0077CC", fg="#FFFFFF", font=('Arial', 16, 'bold')).grid(row=4, column=0, padx=10, pady=10)
        Entry(self.root, textvariable=self.duration, font=('Arial', 16)).grid(row=4, column=1)

        tree_frame = Frame(self.root, bg="#0077CC")
        tree_frame.grid(row=6, column=0, columnspan=2, padx=20, pady=20)

        self.treeview = ttk.Treeview(tree_frame, columns=("Title", "Artist", "Genre", "Release Year", "Duration"), show="headings", height=20)
        self.treeview.grid(row=0, column=0)
        self.treeview.heading("Title", text="Title")
        self.treeview.heading("Artist", text="Artist")
        self.treeview.heading("Genre", text="Genre")
        self.treeview.heading("Release Year", text="Release Year")
        self.treeview.heading("Duration", text="Duration")
        self.treeview.bind('<ButtonRelease-1>', on_select)

        add_button = Button(self.root, text="Add New", font=('Arial Black', 16), bg="#FFFFFF", fg="#0077CC", command=add_music)
        add_button.grid(row=0, column=2, padx=20, pady=10)

        display_button = Button(self.root, text="Display", font=('Arial Black', 16), bg="#FFFFFF", fg="#0077CC", command=display_music)
        display_button.grid(row=1, column=2, padx=20, pady=10)

        self.canvas = Canvas(self.root, width=200, height=200, bg="#0077CC")
        self.canvas.grid(row=6, column=2, padx=20, pady=20)

        self.create_music_animation()

    def create_music_animation(self):
        self.music_note = self.canvas.create_text(100, 100, text="♫", font=('Arial', 48), fill="white")

        def move_music_note():
            x, y = self.canvas.coords(self.music_note)
            dx, dy = 4, 0  
            self.canvas.move(self.music_note, dx, dy)
            self.root.after(30, move_music_note)

            if x > self.canvas.winfo_width():
                self.canvas.move(self.music_note, -self.canvas.winfo_width(), 0)

        move_music_note()

if __name__ == '__main__':
    root = Tk()
    application = MusicDatabase(root)
    root.mainloop()
