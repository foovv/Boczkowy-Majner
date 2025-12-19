import customtkinter as ctk



def run(start_cb, stop_cb):
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()        
    app.geometry("500x500")
    app.title("BoczkowyMajner")
    label = ctk.CTkLabel(app, text="BoczkowyMajner 2000")
    label.pack(pady=20)
    labelBlocks = ctk.CTkLabel(app, text="Na ile blokow stowniarka:")
    labelBlocks.pack(pady=5)
    entry = ctk.CTkEntry(app)
    entry.pack(pady=10)
    labelCommands = ctk.CTkLabel(app, text="Komendy które mam pisac: ")
    labelCommands.pack(pady=5)

    # Commands
    entryCommandOne = ctk.CTkEntry(app)
    entryCommandOne.pack(pady=10)

    entryCommandTwo = ctk.CTkEntry(app)
    entryCommandTwo.pack(pady=10)

    entryCommandThree = ctk.CTkEntry(app)
    entryCommandThree.pack(pady=10)

    entryCommandFour = ctk.CTkEntry(app)
    entryCommandFour.pack(pady=10)



    def on_start():
        try:
            x = [
                entryCommandOne.get(),
                entryCommandTwo.get(),
                entryCommandThree.get(),
                entryCommandFour.get()
            ]


            b = int(entry.get())
            start_cb(b, x)
            print(x)
        except ValueError:
            print("podaj liczbe")

    btn_start = ctk.CTkButton(app, text="Start", command=on_start)
    btn_start.pack(pady=5)

    btn_stop = ctk.CTkButton(app, text="Stop", command=stop_cb)
    btn_stop.pack(pady=5)

    
    app.mainloop()    


