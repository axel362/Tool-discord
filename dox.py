import os
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ---- Fonctions de simulation réalistes ----
def fake_mass_dm():
    print("📨 Mass DM en cours...\n")
    for i in range(1, 6):
        sys.stdout.write(f" ➤ Envoi du message {i}/5 ... ")
        time.sleep(1)
        sys.stdout.write("✅\n")
        sys.stdout.flush()
    print("\n✔ Tous les messages ont été envoyés .")

def fake_token_checker():
    print("🔎 Vérification des tokens...")
    for i in range(3):
        time.sleep(1)
        print(f" ➤ Token {i+1} : Valide ✅")
    print("\n✔ Vérification terminée .")

def fake_group_creator():
    print("👥 Création de groupes...")
    for i in range(3):
        time.sleep(1)
        print(f" ➤ Groupe {i+1} créé ✅")
    print("\n✔ Groupes créés .")

def fake_token_grabber():
    print("🎣 Récupération de tokens...")
    time.sleep(2)
    print(" ➤ Tokens extraits avec succès ✅ ")

def fake_friend_spammer():
    print("🤝 Spam d’amis en cours...")
    for i in range(5):
        time.sleep(0.5)
        print(f" ➤ Demande d’ami {i+1}/5 envoyée ✅")
    print("\n✔ Spam terminé .")

def fake_guild_leaver():
    print("🚪 Quitte toutes les guildes...")
    for i in range(3):
        time.sleep(1)
        print(f" ➤ Serveur {i+1} quitté ✅")
    print("\n✔ Opération terminée .")

def fake_channel_nuker():
    print("💥 Suppression des salons...")
    for i in range(4):
        time.sleep(1)
        print(f" ➤ Salon {i+1} supprimé ✅")
    print("\n✔ Tous les salons ont été supprimés .")

def fake_role_spammer():
    print("🎭 Création de rôles en masse...")
    for i in range(5):
        time.sleep(0.5)
        print(f" ➤ Rôle {i+1}/5 créé ✅")
    print("\n✔ Rôles créés .")

def fake_account_nuker():
    print("☠️ Destruction du compte...")
    for i in range(3):
        time.sleep(1)
        print(f" ➤ Étape {i+1}/3 effectuée ✅")
    print("\n✔ Compte neutralisé .")

def fake_webhook_spammer():
    print("🌐 Spam Webhook...")
    for i in range(5):
        time.sleep(0.5)
        print(f" ➤ Message {i+1}/5 envoyé ✅")
    print("\n✔ Spam terminé .")

def fake_server_info():
    print("📊 Récupération des infos serveur...")
    time.sleep(2)
    print("""
Nom: Serveur Simulation
Membres: 123
Salons: 12
Rôles: 8
    """)
    print("✔ Infos affichées .")

def fake_nitro_generator():
    print("🎁 Générateur de Nitro...")
    for i in range(3):
        time.sleep(1)
        print(" ➤ Code généré : https://discord.gift/GZI?S982")
print(" ➤ Code généré : https://discord.gift/HZF1826J")
print("\n✔ Génération terminée ")

def fake_dm_all():
    print("📩 Envoi d’un DM à tous les utilisateurs...")
    for i in range(5):
        time.sleep(0.5)
        print(f" ➤ DM envoyé à l’utilisateur {i+1} ✅")
    print("\n✔ .")

def fake_status_changer():
    print("💬 Changement de statut...")
    time.sleep(2)
    print(" ✔ Statut changé en '' ✅")

def fake_about():
    print("""
🔧 Fake Discord Tool
Version: 1.0
Auteur: ANNONYMA
    """)

def quit_program():
    print("👋 Fermeture du programme...")
    exit()

# ---- Menu principal ----
def show_menu():
    clear()
    print(Fore.CYAN + r"""
   ──────────────────────────────
        █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
        █░░░░░░░░░░░░░░░░░░█
        █░░   GO   DM   ░░░█
        █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
   ──────────────────────────────
    """)
    print(f"[Tokens: {Fore.GREEN}101{Style.RESET_ALL}]")
    print("──────────────────────────────────────")
    print(f"""
{Fore.CYAN}[01]{Style.RESET_ALL} Mass DM          {Fore.CYAN}[09]{Style.RESET_ALL} Account Nuker
{Fore.CYAN}[02]{Style.RESET_ALL} Token Checker    {Fore.CYAN}[10]{Style.RESET_ALL} Webhook Spammer
{Fore.CYAN}[03]{Style.RESET_ALL} Group Creator    {Fore.CYAN}[11]{Style.RESET_ALL} Server Info
{Fore.CYAN}[04]{Style.RESET_ALL} Token Grabber    {Fore.CYAN}[12]{Style.RESET_ALL} Nitro Generator
{Fore.CYAN}[05]{Style.RESET_ALL} Friend Spammer   {Fore.CYAN}[13]{Style.RESET_ALL} DM All
{Fore.CYAN}[06]{Style.RESET_ALL} Guild Leaver     {Fore.CYAN}[14]{Style.RESET_ALL} Status Changer
{Fore.CYAN}[07]{Style.RESET_ALL} Channel Nuker    {Fore.CYAN}[15]{Style.RESET_ALL} Exit
{Fore.CYAN}[08]{Style.RESET_ALL} Role Spammer     {Fore.CYAN}[16]{Style.RESET_ALL} About
""")
    print("──────────────────────────────────────")

options = {
    "1": fake_mass_dm,
    "2": fake_token_checker,
    "3": fake_group_creator,
    "4": fake_token_grabber,
    "5": fake_friend_spammer,
    "6": fake_guild_leaver,
    "7": fake_channel_nuker,
    "8": fake_role_spammer,
    "9": fake_account_nuker,
    "10": fake_webhook_spammer,
    "11": fake_server_info,
    "12": fake_nitro_generator,
    "13": fake_dm_all,
    "14": fake_status_changer,
    "15": quit_program,
    "16": fake_about
}

def main():
    while True:
        show_menu()
        choice = input("Choice: ").strip()
        action = options.get(choice)
        if action:
            clear()
            action()
        else:
            print("❌ Choix invalide")
        input("\nAppuie sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
