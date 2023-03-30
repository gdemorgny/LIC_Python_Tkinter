# coding: utf-8
import tkinter as tk

#name="Gilbert"
age = "44"
def ecrire_nom():
    if var.get():
        label_nom.config(text=f"Nom : {value.get()}")

def ecrire_age():
    label_age.config(text=f"Age : {value.get()}")


fenetre = tk.Tk()

label_nom = tk.Label(fenetre, text="Nom : ")
label_nom.pack()
label_age = tk.Label(fenetre, text="Age : ")
label_age.pack()

# bouton d'écriture
bouton_write_nom=tk.Button(fenetre, text="Ecrire Nom", command=ecrire_nom, width=15)
bouton_write_nom.pack()
# bouton d'écriture
bouton_write_age=tk.Button(fenetre, text="Ecrire Age", command=ecrire_age, width=15)
bouton_write_age.pack()

# entrée
value = tk.StringVar()
value.set("text à écrire")
entree = tk.Entry(fenetre, textvariable=value, width=60)
entree.pack()
# checkbutton
var = tk.BooleanVar()
checkbox = tk.Checkbutton(fenetre, text="Nouveau?", variable=var)
checkbox.pack()


fenetre.mainloop()