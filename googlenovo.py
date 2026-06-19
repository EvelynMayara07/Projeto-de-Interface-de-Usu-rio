import tkinter as tk
from tkinter import ttk

class SearchApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações principais da janela
        self.title("May")
        self.geometry("800x600")
        self.configure(bg="#ffd6e7")
        self.minsize(400, 300)

        # Container principal centralizado
        main_frame = tk.Frame(self, bg="#ffd6e7")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # ---------- CORAÇÕES DECORATIVOS ----------
        hearts = [
            ("💖", 80, 70),
            ("💗", 700, 100),
            ("💕", 120, 500),
            ("💘", 650, 480),
            ("💞", 20, 300),
            ("💓", 740, 320),
        ]

        for heart, x, y in hearts:
            tk.Label(
                self,
                text=heart,
                font=("Arial", 22),
                bg="#ffd6e7"
            ).place(x=x, y=y)

        # ---------- TÍTULO ----------
        title_frame = tk.Frame(main_frame, bg="#ffd6e7")
        title_frame.pack(pady=(0, 30))

        # Tons de rosa
        colors = [
            "#ff69b4",
            "#ff1493",
            "#ff85c1",
            "#db7093"
        ]

        text = "May"

        for i, char in enumerate(text):
            tk.Label(
                title_frame,
                text=char,
                font=("Arial", 64, "bold"),
                fg=colors[i],
                bg="#ffd6e7"
            ).pack(side="left")

        # ---------- BARRA DE PESQUISA ----------
        search_frame = tk.Frame(
            main_frame,
            bg="#ffffff",
            bd=1,
            relief="solid",
            highlightbackground="#ff8fc4",
            highlightthickness=2
        )

        search_frame.pack(ipadx=10, ipady=5, fill="x")

        # Ícone lupa
        search_icon = tk.Label(
            search_frame,
            text="🔍",
            bg="#ffffff",
            font=("Segoe UI Emoji", 14),
            fg="#ff4fa3"
        )

        search_icon.pack(side="left", padx=(10, 5))

        # Entrada de texto
        self.placeholder_text = "Pesquise algo fofo..."
        self.search_var = tk.StringVar()

        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Arial", 14),
            width=50,
            bd=0,
            bg="#ffffff",
            fg="grey",
            highlightthickness=0
        )

        self.search_entry.pack(side="left", padx=5, pady=5)
        self.search_entry.insert(0, self.placeholder_text)

        # Ícone microfone
        mic_icon = tk.Label(
            search_frame,
            text="🎀",
            bg="#ffffff",
            font=("Segoe UI Emoji", 14)
        )

        mic_icon.pack(side="right", padx=(5, 10))

        # Eventos
        self.search_entry.bind("<FocusIn>", self.on_entry_click)
        self.search_entry.bind("<FocusOut>", self.on_focus_out)
        self.search_entry.bind("<Return>", self.perform_search)

        # ---------- BOTÕES ----------
        buttons_frame = tk.Frame(main_frame, bg="#ffd6e7")
        buttons_frame.pack(pady=30)

        search_button = tk.Button(
            buttons_frame,
            text="Pesquisa May",
            font=("Arial", 11, "bold"),
            bg="#ff69b4",
            fg="#ffffff",
            relief="flat",
            activebackground="#ff1493",
            padx=18,
            pady=8,
            cursor="hand2",
            command=self.perform_search
        )

        search_button.pack(side="left", padx=10)

        feeling_lucky_button = tk.Button(
            buttons_frame,
            text="Estou com sorte 💖",
            font=("Arial", 11, "bold"),
            bg="#ff69b4",
            fg="#ffffff",
            relief="flat",
            activebackground="#ff1493",
            padx=18,
            pady=8,
            cursor="hand2"
        )

        feeling_lucky_button.pack(side="left", padx=10)

    def on_entry_click(self, event):

        if self.search_entry.get() == self.placeholder_text:
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg="black")

    def on_focus_out(self, event):

        if self.search_entry.get() == "":
            self.search_entry.insert(0, self.placeholder_text)
            self.search_entry.config(fg="grey")

    def perform_search(self, event=None):

        query = self.search_entry.get()

        if query and query != self.placeholder_text:
            print(f"Pesquisando por: {query}")

if __name__ == "__main__":
    app = SearchApp()
    app.mainloop()