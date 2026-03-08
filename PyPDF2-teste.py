import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from PyPDF2 import PdfReader

caminhoPdf = r"C:\Users\Cauan\Documents\python\docs\HP e a pedra filosofal.pdf"
leitor = PdfReader(caminhoPdf)

texto = ""
for pagina in leitor.pages:
    texto += pagina.extract_text()

janela = tk.Tk()
janela.title("Visualizador de PDF")
janela.config(bg="#d9d9d9")  

modo_noturno = False

def aplicar_tema():
    if modo_noturno:
        caixaTxt.config(bg="black", fg="white", insertbackground="white")
    else:
        caixaTxt.config(bg="white", fg="black", insertbackground="black")

class ToggleSwitch(tk.Canvas):
    def __init__(self, master, width=60, height=30, bg_on="#4cd964",
                 bg_off="#e5e5ea", knob_color="white", command=None):
        super().__init__(master, width=width, height=height, highlightthickness=0, bg=master.cget("bg"))
        
        self.width = width
        self.height = height
        self.bg_on = bg_on
        self.bg_off = bg_off
        self.knob_color = knob_color
        self.command = command
        self.on = False

        self.bg_left = self.create_oval(0, 0, height, height, fill=bg_off, outline=bg_off)
        self.bg_mid = self.create_rectangle(height/2, 0, width - height/2, height, fill=bg_off, outline=bg_off)
        self.bg_right = self.create_oval(width - height, 0, width, height, fill=bg_off, outline=bg_off)

        self.knob = self.create_oval(2, 2, height - 2, height - 2, fill=knob_color, outline=knob_color)

        self.bind("<Button-1>", self.toggle)

    def toggle(self, event=None):
        self.on = not self.on
        self.animate()
        if self.command:
            self.command(self.on)

    def animate(self):
        start = 2 if self.on else self.width - self.height + 2
        end = self.width - self.height + 2 if self.on else 2
        step = 2 if end > start else -2

        color = self.bg_on if self.on else self.bg_off
        self.itemconfig(self.bg_left, fill=color)
        self.itemconfig(self.bg_mid, fill=color)
        self.itemconfig(self.bg_right, fill=color)

        for x in range(start, end, step):
            self.coords(self.knob, x, 2, x + self.height - 4, self.height - 2)
            self.update()
            self.after(5)



top_frame = tk.Frame(janela, bg="#d9d9d9")
top_frame.pack(fill="x", pady=10)

label = tk.Label(top_frame, bg="#d9d9d9", font=("Arial", 12))
label.pack(side="left", padx=10)

switch = ToggleSwitch(top_frame, command=lambda s: alternar_modo(s))
switch.pack(side="left")

def alternar_modo(estado):
    global modo_noturno
    modo_noturno = estado
    aplicar_tema()

caixaTxt = ScrolledText(janela, wrap=tk.WORD, width=100, height=40)
caixaTxt.pack(expand=True, fill="both")
caixaTxt.insert(tk.END, texto)
caixaTxt.config(state="disabled")

aplicar_tema()
janela.mainloop()