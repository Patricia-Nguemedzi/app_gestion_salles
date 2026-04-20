import customtkinter as ctk
from services.services_salle import ServiceSalle
from tkinter import ttk
from models.salle import Salle

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des Salles - STEF & JD COLLECTION Style")
        self.geometry("900x650")
        self.service_salle = ServiceSalle()
        self.setup_ui()

    def setup_ui(self):
        pass

    def setup_ui(self):
        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.pack(pady=20, padx=20, fill="x")

        ctk.CTkLabel(self.frame_form, text="Code:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_code = ctk.CTkEntry(self.frame_form)
        self.entry_code.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.frame_form, text="Description:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_desc = ctk.CTkEntry(self.frame_form)
        self.entry_desc.grid(row=0, column=3, padx=5, pady=5)

        ctk.CTkLabel(self.frame_form, text="Catégorie:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_cat = ctk.CTkEntry(self.frame_form)
        self.entry_cat.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.frame_form, text="Capacité:").grid(row=1, column=2, padx=5, pady=5)
        self.entry_cap = ctk.CTkEntry(self.frame_form)
        self.entry_cap.grid(row=1, column=3, padx=5, pady=5)

        self.frame_btns = ctk.CTkFrame(self)
        self.frame_btns.pack(pady=10, padx=20, fill="x")

        self.btn_add = ctk.CTkButton(self.frame_btns, text="Ajouter", command=self.action_ajouter)
        self.btn_add.pack(side="left", padx=10, pady=10)

        self.btn_update = ctk.CTkButton(self.frame_btns, text="Modifier", command=self.action_modifier)
        self.btn_update.pack(side="left", padx=10, pady=10)

        self.btn_delete = ctk.CTkButton(self.frame_btns, text="Supprimer", fg_color="red", command=self.action_supprimer)
        self.btn_delete.pack(side="left", padx=10, pady=10)

        self.tree = ttk.Treeview(self, columns=("code", "desc", "cat", "cap"), show="headings")
        self.tree.heading("code", text="Code")
        self.tree.heading("desc", text="Description")
        self.tree.heading("cat", text="Catégorie")
        self.tree.heading("cap", text="Capacité")
        self.tree.pack(pady=20, padx=20, fill="both", expand=True)

    def action_ajouter(self):
        s = Salle(self.entry_code.get(), self.entry_desc.get(),
                  self.entry_cat.get(), int(self.entry_cap.get()))
        succes, msg = self.service_salle.ajouter_salle(s)
        print(msg)
        self.charger_donnees()

    def action_modifier(self):
        code = self.entry_code.get()
        desc = self.entry_desc.get()
        cat = self.entry_cat.get()
        try:
            cap = int(self.entry_cap.get())
        except ValueError:
            cap = 0

        salle_modifiee = Salle(code, desc, cat, cap)

        succes, msg = self.service_salle.modifier_salle(salle_modifiee)

        if succes:
            print(f"Succès : {msg}")
            self.charger_donnees()  # On rafraîchit le tableau
        else:
            print(f"Erreur : {msg}")

    def charger_donnees(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        salles = self.service_salle.recuperer_salles()
        for s in salles:
            self.tree.insert("", "end", values=(s.codes, s.descriptions, s.categorie, s.capacite))