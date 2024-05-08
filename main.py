import tkinter as tk


class StudentManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Student Management System')
        self.geometry('250x400')
        self.create_widgets()
        # self.database = Database()

    def create_widgets(self):
        lbl_id = tk.Label(self, text="Meli Code")
        lbl_id.grid(row=0, column=0, padx=10, pady=10)

        lbl_first_name = tk.Label(self, text='Firstname:')
        lbl_first_name.grid(row=1, column=0, padx=10, pady=10)

        lbl_last_name = tk.Label(self, text='Last name:')
        lbl_last_name.grid(row=2, column=0, padx=10, pady=10)

        lbl_age = tk.Label(self, text="Age:")
        lbl_age.grid(row=3, column=0, padx=10, pady=10)

        lbl_email = tk.Label(self, text="Email:")
        lbl_email.grid(row=4, column=0, padx=10, pady=10)

        self.entry_id = tk.Entry(self)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        self.entry_first_name = tk.Entry(self)
        self.entry_first_name.grid(row=1, column=1, padx=10, pady=10)

        self.entry_last_name = tk.Entry(self)
        self.entry_last_name.grid(row=2, column=1, padx=10, pady=10)

        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=3, column=1, padx=10, pady=10)

        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=4, column=1, padx=10, pady=10)




if __name__ == '__main__':
            app = StudentManagementApp()
            app.mainloop()
