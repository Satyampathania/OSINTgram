import os
import time
import instaloader
from colorama import Fore, Style, init
import requests

# Initialize colorama
init(autoreset=True)

# Function to clear screen based on OS
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the animated startup
def animated_intro():
    intro_frames = [
        f"""
{Fore.GREEN}███████╗██████╗ ██╗     ██╗   ██╗███████╗██████╗ 
{Fore.GREEN}╚══██╔══╝██╔══██╗██║     ██║   ██║██╔════╝██╔══██╗
{Fore.RED}   ██║   ██████╔╝██║     ██║   ██║███████╗██████╔╝
{Fore.YELLOW}   ██║   ██╔══██╗██║     ██║   ██║╚════██║██╔═══╝ 
{Fore.CYAN}   ██║   ██████╔╝██████╗ ╚██████╔╝███████║██║     
{Fore.MAGENTA}   ╚═╝   ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝     
    """,
    ]

    for _ in range(3):  # Display 3 times
        for frame in intro_frames:
            clear_screen()
            print(frame)
            time.sleep(0.3)

# Function to display social links
def display_socials():
    socials = f"""
{Fore.YELLOW}--- ABOUT ME ---
{Fore.CYAN}👋 Hi, I'm Satyam! A passionate Security Researcher and Developer.
{Fore.GREEN}🌐 LinkedIn: {Fore.RESET}https://www.linkedin.com/in/satyam-pathania/
{Fore.BLUE}🐦 X (Twitter): {Fore.RESET}https://x.com/satyam72565815
{Fore.MAGENTA}🎥 YouTube: {Fore.RESET}https://www.youtube.com/@cryptoKnight69

{Fore.YELLOW}--- SUPPORT ME ---
{Fore.GREEN}☕ Buy Me a Coffee: {Fore.RESET}https://buymeacoffee.com/satyampathania
{Fore.CYAN}💰 PayPal: {Fore.RESET}https://www.paypal.com/paypalme/satyampathania69
"""

    print(socials)

# Function to download Instagram profile data
def download_instagram_data(profile_name):
    L = instaloader.Instaloader()

    print(f"{Fore.GREEN}Fetching data for {profile_name}...")

    try:
        # Load profile
        profile = instaloader.Profile.from_username(L.context, profile_name)

        # Show profile information
        print(f"{Fore.CYAN}Profile Info for @{profile_name}:")
        print(f"{Fore.MAGENTA}Name: {profile.full_name}")
        print(f"{Fore.YELLOW}Bio: {profile.biography}")
        print(f"{Fore.GREEN}Followers: {profile.followers}")
        print(f"{Fore.RED}Following: {profile.followees}")
        print(f"{Fore.CYAN}Posts: {profile.mediacount}")

        # Download profile's recent posts
        print(f"{Fore.YELLOW}Downloading latest posts...")
        for post in profile.get_posts():
            L.download_post(post, target=profile_name)

    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}")

# Function to install the tool
def install_osintgram():
    print("\n[INFO] Installing OSINTgram Tool...")

    # Simulate installation with a delay
    time.sleep(1)
    print("[INFO] Fetching tool resources...")

    try:
        # A placeholder for a real request or tool download
        url = "https://github.com/satyampathania/OSINTgram"
        response = requests.get(url)
        
        if response.status_code == 200:
            print("[INFO] Tool fetched successfully!")
        else:
            print("[ERROR] Could not fetch the tool.")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch tool: {e}")
    
    print("\n[INFO] Installation complete!")

# Main function to run the tool
def main():
    animated_intro()  # Display intro animation
    install_osintgram()  # Simulate installation
    display_socials()  # Show social media links

    # Get Instagram profile name from user
    profile_name = input(f"{Fore.GREEN}\nEnter Instagram profile name: ")

    # Download data for the entered profile
    download_instagram_data(profile_name)

if __name__ == "__main__":
    main()
