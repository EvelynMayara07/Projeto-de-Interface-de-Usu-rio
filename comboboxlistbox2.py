"""
Sistema de Receitas com Combobox e Listbox
Adaptado do exemplo didático de Tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ── Banco de Receitas ───────────────────────────────────────────────
receitas = {
    "🍰 Sobremesa": {
        "Brigadeiro": {
            "ingredientes": "1 lata de leite condensado\n2 colheres de chocolate em pó\n1 colher de manteiga",
            "preparo": "Misture tudo na panela e mexa até desgrudar do fundo."
        },
        "Pudim": {
            "ingredientes": "1 lata de leite condensado\n3 ovos\n2 medidas de leite",
            "preparo": "Bata tudo no liquidificador e asse em banho-maria."
        },
        "Mousse de Chocolate": {
            "ingredientes": "200g de chocolate\n1 caixa de creme de leite",
            "preparo": "Misture os ingredientes e leve à geladeira."
        }
    },

    "🍽️ Almoço": {
        "Lasanha": {
            "ingredientes": "Massa, molho, queijo e presunto",
            "preparo": "Monte as camadas e asse por 40 minutos."
        },
        "Estrogonofe": {
            "ingredientes": "Frango, creme de leite e molho de tomate",
            "preparo": "Refogue o frango e misture os demais ingredientes."
        },
        "Feijoada": {
            "ingredientes": "Feijão preto e carnes variadas",
            "preparo": "Cozinhe tudo junto até ficar macio."
        }
    },

    "🌙 Janta": {
        "Sopa de Legumes": {
            "ingredientes": "Batata, cenoura e chuchu",
            "preparo": "Cozinhe os legumes e bata parte deles."
        },
        "Omelete": {
            "ingredientes": "Ovos, queijo e temperos",
            "preparo": "Misture tudo e frite em uma frigideira."
        },
        "Macarrão": {
            "ingredientes": "Macarrão e molho",
            "preparo": "Cozinhe o macarrão e adicione o molho."
        }
    },

    "🍳 Café da Manhã": {
        "Panquecas": {
            "ingredientes": "Farinha, leite e ovos",
            "preparo": "Misture os ingredientes e cozinhe em frigideira."
        },
        "Pão de Queijo": {
            "ingredientes": "Polvilho, queijo e ovos",
            "preparo": "Misture, modele e asse."
        },
        "Vitamina de Frutas": {
            "ingredientes": "Banana, leite e aveia",
            "preparo": "Bata tudo no liquidificador."
        }
    },

    "🥪 Lanche da Tarde": {
        "Sanduíche Natural": {
            "ingredientes": "Pão, alface, tomate e frango",
            "preparo": "Monte os ingredientes entre as fatias de pão."
        },
        "Bolo de Cenoura": {
            "ingredientes": "Cenoura, farinha, ovos e açúcar",
            "preparo": "Bata os ingredientes e asse."
        },
        "Cookies": {
            "ingredientes": "Farinha, manteiga e gotas de chocolate",
            "preparo": "Misture tudo e asse por 15 minutos."
        }
    }
}

# ── Janela ──────────────────────────────────────────────────────────
janela = tk.Tk()
janela.title("🍴 Sistema de Receitas")
janela.geometry("500x550")
janela.configure(bg="#FCE4EC")
janela.resizable(False, False)

# ── Título ──────────────────────────────────────────────────────────
tk.Label(
    janela,
    text="🍴 Sistema de Receitas",
    font=("Arial", 16, "bold"),
    bg="#5DADE2",
    fg="white",
    pady=12
).pack(fill="x")

# ── Mensagem de Boas-vindas ─────────────────────────────────────────
tk.Label(
    janela,
    text="Bem-vindo! Escolha um tipo de comida e uma receita.",
    font=("Arial", 10),
    bg="#FCE4EC",
    fg="#6C3483"
).pack(pady=10)

# ── Combobox ────────────────────────────────────────────────────────
tk.Label(
    janela,
    text="1. Escolha um tipo de comida:",
    font=("Arial", 11, "bold"),
    bg="#FCE4EC",
    fg="#6C3483"
).pack(pady=(10, 4))

var_categoria = tk.StringVar()

combo = ttk.Combobox(
    janela,
    textvariable=var_categoria,
    values=list(receitas.keys()),
    state="readonly",
    width=28,
    font=("Arial", 11)
)

combo.set("Selecione...")
combo.pack()

# ── Listbox ─────────────────────────────────────────────────────────
tk.Label(
    janela,
    text="2. Escolha uma receita:",
    font=("Arial", 11, "bold"),
    bg="#FCE4EC",
    fg="#6C3483"
).pack(pady=(18, 4))

listbox = tk.Listbox(
    janela,
    height=8,
    width=35,
    font=("Arial", 11),
    bg="white",
    selectbackground="#5DADE2",
    selectforeground="white"
)

listbox.pack()

# ── Atualizar receitas ──────────────────────────────────────────────
def atualizar_receitas(event=None):
    categoria = var_categoria.get()

    listbox.delete(0, tk.END)

    if categoria in receitas:
        for receita in receitas[categoria]:
            listbox.insert(tk.END, receita)

combo.bind("<<ComboboxSelected>>", atualizar_receitas)

# ── Mostrar Receita ────────────────────────────────────────────────
def mostrar():
    categoria = var_categoria.get()

    if categoria == "Selecione...":
        messagebox.showwarning(
            "Atenção",
            "Escolha um tipo de comida!"
        )
        return

    selecionado = listbox.curselection()

    if not selecionado:
        messagebox.showwarning(
            "Atenção",
            "Escolha uma receita!"
        )
        return

    nome_receita = listbox.get(selecionado[0])

    dados = receitas[categoria][nome_receita]

    messagebox.showinfo(
        f"🍴 {nome_receita}",
        f"Categoria: {categoria}\n\n"
        f"📋 Ingredientes:\n{dados['ingredientes']}\n\n"
        f"👨‍🍳 Modo de preparo:\n{dados['preparo']}"
    )

# ── Botão ───────────────────────────────────────────────────────────
tk.Button(
    janela,
    text="🍽️ Ver Receita",
    command=mostrar,
    bg="#EC407A",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    relief="flat",
    cursor="hand2"
).pack(pady=20)

# ── Informações ─────────────────────────────────────────────────────
frame_info = tk.Frame(
    janela,
    bg="#D6EAF8",
    padx=15,
    pady=10
)

frame_info.pack(fill="x", padx=20)

tk.Label(
    frame_info,
    text="Como usar:",
    font=("Arial", 10, "bold"),
    bg="#D6EAF8",
    fg="#21618C"
).pack(anchor="w")

tk.Label(
    frame_info,
    text="• Escolha uma categoria no Combobox.",
    bg="#D6EAF8",
    fg="#21618C"
).pack(anchor="w")

tk.Label(
    frame_info,
    text="• Selecione uma receita na Listbox.",
    bg="#D6EAF8",
    fg="#21618C"
).pack(anchor="w")

tk.Label(
    frame_info,
    text="• Clique em 'Ver Receita' para visualizar.",
    bg="#D6EAF8",
    fg="#21618C"
).pack(anchor="w")

# ── Rodapé ──────────────────────────────────────────────────────────
tk.Label(
    janela,
    text="🍰 Receitas para todas as ocasiões 🍽️",
    font=("Arial", 9, "italic"),
    bg="#FCE4EC",
    fg="#7D3C98"
).pack(side="bottom", pady=8)

janela.mainloop()