from tkinter import *
from tkinter.ttk import *
from time import strftime

# Configurer la fenêtre principale
root = Tk()
root.title("Horloge avec le langage Python")
root.configure(background="black")

# Fonction pour mettre à jour l'heure
def update_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)

# Créer le label pour afficher l'heure
label = Label(root, font=("ds-digital", 80), background="black", foreground="lime")
label.pack(anchor="center")

# Lancer la mise à jour de l'heure
update_time()

# Boucle principale de l'application
root.mainloop()
