import customtkinter

from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super(App, self).__init__()

        self.geometry("460x370")
        self.title = "Password generator"
        self.resizable(False, False)

        self.logo = customtkinter.CTkImage(dark_image=Image.open("logo.png"), size=(460, 150))
        self.logo_label = customtkinter.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

        self.password_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), sticky="nsew")


if __name__ == '__main__':
    app = App()
    app.mainloop()
