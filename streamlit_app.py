import streamlit as st
import seaborn as sns
from streamlit_authenticator import Authenticate

from streamlit_option_menu import option_menu


# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
    st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")
    with st.sidebar:
        selection = option_menu(
            menu_title="Mon menu",
            options = ["Accueil", "Photos"],
            menu_icon  = "arrows-move"
        )
        authenticator.logout("Déconnexion")
        
    if selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil !")
        st.image("https://img.static-af.com/otf/images/meta/IDname/CRITERIA-BEACH-1")
    elif selection == "Photos":
        st.write("Bienvenue sur mon album photo")
        st.image("https://i.pinimg.com/originals/3f/60/0d/3f600dd8237be2a4ea2a574142e5edb6.jpg")
        

if st.session_state["authentication_status"]:
    accueil()
    
    # Le bouton de déconnexion
    

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
