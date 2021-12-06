# Python Logger by JamesJoynsonEllis

# [Requires tkinter_tools.py, tkinter, datetime]
# (NB: Modules(tkinter_tools.py) are made by JamesJoynsonEllis on GitHub, it is recommended to get the most recent version from the repository online

def logger_tkinter():
    from datetime import datetime
    import tkinter
    import tkinter.filedialog as fd
    import tkinter_tools as tt

    root = tkinter.Tk()
    root.title("Python Logger by JamesJoynsonEllis")

    filetypes = (
        ('Text Files', '*.txt'),
        ('All Files', '*.*')
    )

    # Widgets
    fp_label = tkinter.Label(root, text="File Path: ")
    fp_entry = tkinter.Entry()
    log_label = tkinter.Label(root, text="LOG: ")
    log_entry = tkinter.Entry(root)

    def open_file_path():
        if len(fp_entry.get()) > 0:
            fp_entry.delete(0, -1)
        fp_entry.insert(0, fd.askopenfilename(initialdir="/", title="Select a log file", filetypes=filetypes))

    def submit_log():
        file_path = fp_entry.get()
        log = log_entry.get()
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.today().strftime("%d/%m/%Y")
        log = "<" + current_date + " " + current_time + "> " + log
        file = open(file_path, "a")
        file.write(log)

    # Buttons
    get_fp_button = tkinter.Button(root, text="Get File", command=open_file_path)
    submit_log_button = tkinter.Button(root, text="Submit log", command=submit_log)

    # Grid
    tt.blank_lines_vertical(0, 3, root=root)
    tt.blank_lines_horizontal(0, 6, root=root)

    fp_label.grid(row=1, column=1)
    fp_entry.grid(row=2, column=1)
    get_fp_button.grid(row=2, column=2)
    log_label.grid(row=1, column=4)
    log_entry.grid(row=2, column=4)
    submit_log_button.grid(row=2, column=5)

    tkinter.mainloop()

logger_tkinter()

# This code is not to be directly used without crediting the author
