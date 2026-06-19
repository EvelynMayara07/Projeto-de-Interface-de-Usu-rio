import tkinter as tk
from tkinter import ttk, messagebox

class AppConsultaMedica(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("Cadastro de Consulta Médica")
        self.geometry("900x650")
        self.configure(bg="#FFE4EC")  # Rosa claro
        self.resizable(False, False)

        # Paleta de Cores Rosa
        self.bg_color = "#FFE4EC"
        self.fg_color = "#4A0033"
        self.accent_color = "#FF4F9A"
        self.input_bg = "#FFF0F5"
        self.border_color = "#FFB6C1"
        self.text_muted = "#A64D79"

        # Estilo do Combobox
        style = ttk.Style()
        style.theme_use('clam')

        style.configure(
            "TCombobox",
            fieldbackground=self.input_bg,
            background=self.bg_color,
            foreground=self.fg_color,
            bordercolor=self.border_color,
            arrowcolor=self.accent_color,
            padding=5
        )

        self.create_widgets()

    def create_widgets(self):

        # ---------- CABEÇALHO ----------
        header_frame = tk.Frame(self, bg=self.bg_color)
        header_frame.pack(fill="x", pady=(40, 20))

        title = tk.Label(
            header_frame,
            text="S I S T E M A   M É D I C O",
            font=("Segoe UI", 11, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title.pack()

        subtitle = tk.Label(
            header_frame,
            text="CADASTRO DE CONSULTA",
            font=("Segoe UI", 30, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        subtitle.pack()

        separator = tk.Frame(
            header_frame,
            bg=self.accent_color,
            height=3,
            width=120
        )
        separator.pack(pady=(10, 0))

        # ---------- FORMULÁRIO ----------
        form_frame = tk.Frame(self, bg=self.bg_color)
        form_frame.pack(expand=True, fill="both", padx=120)

        def create_input(parent, label_text, row, col, width=30):

            lbl = tk.Label(
                parent,
                text=label_text,
                font=("Segoe UI", 10, "bold"),
                bg=self.bg_color,
                fg=self.text_muted
            )

            lbl.grid(row=row, column=col, sticky="w", pady=(15, 0), padx=15)

            entry = tk.Entry(
                parent,
                font=("Segoe UI", 13),
                bg=self.input_bg,
                fg=self.fg_color,
                insertbackground=self.accent_color,
                relief="flat",
                width=width,
                highlightthickness=1,
                highlightbackground=self.border_color,
                highlightcolor=self.accent_color
            )

            entry.grid(
                row=row + 1,
                column=col,
                sticky="we",
                pady=(5, 5),
                padx=15,
                ipady=8
            )

            return entry

        self.ent_nome = create_input(form_frame, "NOME DO PACIENTE", 0, 0, 35)
        self.ent_cpf = create_input(form_frame, "CPF", 0, 1, 25)

        self.ent_email = create_input(form_frame, "E-MAIL", 2, 0, 35)
        self.ent_telefone = create_input(form_frame, "TELEFONE", 2, 1, 25)

        self.ent_data = create_input(form_frame, "DATA DA CONSULTA", 4, 0, 20)
        self.ent_horario = create_input(form_frame, "HORÁRIO", 4, 1, 15)

        # Especialidade
        lbl_tipo = tk.Label(
            form_frame,
            text="ESPECIALIDADE",
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_color,
            fg=self.text_muted
        )

        lbl_tipo.grid(row=6, column=0, sticky="w", pady=(15, 0), padx=15)

        self.combo_tipo = ttk.Combobox(
            form_frame,
            values=[
                "Clínico Geral",
                "Pediatria",
                "Cardiologia",
                "Dermatologia",
                "Ginecologia"
            ],
            font=("Segoe UI", 12),
            state="readonly"
        )

        self.combo_tipo.grid(
            row=7,
            column=0,
            sticky="we",
            pady=(5, 5),
            padx=15
        )

        self.combo_tipo.set("Clínico Geral")

        # Cores do menu dropdown
        self.option_add('*TCombobox*Listbox.font', ("Segoe UI", 12))
        self.option_add('*TCombobox*Listbox.background', self.input_bg)
        self.option_add('*TCombobox*Listbox.foreground', self.fg_color)
        self.option_add('*TCombobox*Listbox.selectBackground', self.accent_color)
        self.option_add('*TCombobox*Listbox.selectForeground', "#FFFFFF")

        # Grid
        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=1)

        # ---------- BOTÃO ----------
        btn_frame = tk.Frame(self, bg=self.bg_color)
        btn_frame.pack(fill="x", pady=(20, 40))

        def on_enter(e):
            self.btn_cadastrar.config(bg="#FF85B3")

        def on_leave(e):
            self.btn_cadastrar.config(bg=self.accent_color)

        self.btn_cadastrar = tk.Button(
            btn_frame,
            text="AGENDAR CONSULTA",
            font=("Segoe UI", 12, "bold"),
            bg=self.accent_color,
            fg="#FFFFFF",
            activebackground="#FF85B3",
            activeforeground="#FFFFFF",
            relief="flat",
            cursor="hand2",
            command=self.cadastrar
        )

        self.btn_cadastrar.pack(ipady=12, ipadx=50)

        self.btn_cadastrar.bind("<Enter>", on_enter)
        self.btn_cadastrar.bind("<Leave>", on_leave)

        # Status
        self.status_lbl = tk.Label(
            self,
            text="",
            font=("Segoe UI", 11),
            bg=self.bg_color,
            fg=self.accent_color
        )

        self.status_lbl.pack(pady=(10, 0))

    def cadastrar(self):

        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        especialidade = self.combo_tipo.get()

        if not nome or not cpf:
            messagebox.showwarning(
                "Atenção",
                "Os campos Nome e CPF são obrigatórios!",
                parent=self
            )
            return

        self.status_lbl.config(
            text="Agendando consulta...",
            fg=self.fg_color
        )

        self.update()
        self.after(500)

        self.status_lbl.config(
            text=f"✓ Consulta de {especialidade} agendada para {nome.split()[0]}!",
            fg=self.accent_color
        )

        # Limpar campos
        self.ent_nome.delete(0, tk.END)
        self.ent_cpf.delete(0, tk.END)
        self.ent_email.delete(0, tk.END)
        self.ent_telefone.delete(0, tk.END)
        self.ent_data.delete(0, tk.END)
        self.ent_horario.delete(0, tk.END)

        self.combo_tipo.set("Clínico Geral")

        self.ent_nome.focus()


if __name__ == "__main__":
    app = AppConsultaMedica()
    app.mainloop()