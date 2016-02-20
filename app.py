from ttk import Frame, Label, Button, Entry
import Tkinter
import adder
import threading

class AdderApp(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Adder App")
        #self.master.geometry("200x150")

        self.instructions = Label(self, text="Enter the value to add to:")
        self.instructions.pack(pady=5)

        self.number = Entry(self)
        self.number.focus_set()
        self.number.pack(pady=5)

        self.total = Tkinter.StringVar()
        self.time = Tkinter.StringVar()

        self.total_frame = Frame(self)
        self.total_frame.pack(pady=0)
        Label(self.total_frame, text="Total:").pack(side=Tkinter.LEFT, padx=5)
        Label(self.total_frame, textvariable=self.total).pack(side=Tkinter.LEFT)
        self.time_frame = Frame(self)
        self.time_frame.pack(pady=0)
        Label(self.time_frame, text="Time:").pack(side=Tkinter.LEFT)
        Label(self.time_frame, textvariable=self.time).pack(side=Tkinter.LEFT)
        self.complete_msg = Tkinter.StringVar()
        Label(self, textvariable=self.complete_msg).pack(pady=2)

        self.buttons = Frame(self)
        self.buttons.pack(side=Tkinter.BOTTOM, pady=2)
        self.quit_btn = Button(self.buttons, text="Quit", command=self.quit)
        self.quit_btn.pack(side=Tkinter.LEFT)
        self.quit_btn.bind("<Return>", (lambda e, b=self.quit_btn: b.invoke()))
        self.run_btn = Button(self.buttons, text="Run", command=self.run, default=Tkinter.ACTIVE)
        self.run_btn.pack(side=Tkinter.LEFT)
        
        self.pack(fill=Tkinter.X)
        self.master.bind("<Return>", (lambda e, b=self.run_btn: b.invoke()))

    def run_btn_invoke(self, e):
        print("starting run with button enter")
        self.run_btn.invoke()

    def run(self):
        self.complete_msg.set("")

        self.add_run = adder.Adder()
        self.t = threading.Thread(target=self.add_run.run_to, args=(int(self.number.get()),))
        self.t.start()

        self.update_status()

    def update_status(self):
        self.total.set(self.add_run.total)
        try:
            self.time.set(self.add_run.elapsed_seconds())
        except Exception:
            pass

        if self.add_run.complete:
            self.complete_msg.set("Run Complete")
            self.quit_btn.focus_set()

        self.after(50, self.update_status)

if __name__ == "__main__":
    AdderApp().mainloop()