import customtkinter as ctk
from services.services_salle import ServiceSalle
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