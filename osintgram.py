import pyfiglet
from colorama import Fore, Style

# ASCII Art for OSINTgram
def display_ascii_art():
    ascii_art = pyfiglet.figlet_format("OSINTgram")
    print(Fore.CYAN + ascii_art + Style.RESET_ALL)

# Mocked Instagram Data (Replace with API calls or scraping logic)
mock_data = {
    "profile": {
        "username": "satyam.pathania",
        "followers": 895,
        "followings": 120,
        "bio": "eyes are loud 👀",
        "posts": 42,
    },
    "posts": [
        {"id": 1, "caption": "Climb the mountain not to plant a flag 🌄", "likes": 120, "comments": 15},
        {"id": 2, "caption": "All about the vibe 🔆", "likes": 200, "comments": 25},
        {"id": 3, "caption": "Ethical Hacking 💻", "likes": 180, "comments": 18},
    ],
    "emails": ["testuser1@mail.com", "testuser2@mail.com"],
    "phone_numbers": ["+1234567890", "+0987654321"],
    "hashtags": ["#vibes", "#hacking", "#cybersecurity"],
    "tagged_users": ["@john_doe", "@jane_doe"],
    "commenters": ["@commenter1", "@commenter2"],
}

# Feature Implementations
def addrs():
    print("Fetching all registered addresses by target photos...")
    print("Registered Addresses: Not available in mock data. (Implement scraping here)")

def captions():
    print("Fetching user's photo captions...")
    for post in mock_data["posts"]:
        print(f"Post {post['id']}: {post['caption']}")

def comments():
    print("Fetching total comments on target's posts...")
    total_comments = sum(post["comments"] for post in mock_data["posts"])
    print(f"Total Comments: {total_comments}")

def followers():
    print("Fetching target's followers...")
    print(f"Followers Count: {mock_data['profile']['followers']}")

def followings():
    print("Fetching users followed by the target...")
    print(f"Following Count: {mock_data['profile']['followings']}")

def fwersemail():
    print("Fetching email addresses of target's followers...")
    print("Emails:", ", ".join(mock_data["emails"]))

def fwingsemail():
    print("Fetching email addresses of users followed by the target...")
    print("Emails: Placeholder data (Replace with logic)")

def fwersnumber():
    print("Fetching phone numbers of target's followers...")
    print("Phone Numbers:", ", ".join(mock_data["phone_numbers"]))

def fwingsnumber():
    print("Fetching phone numbers of users followed by the target...")
    print("Phone Numbers: Placeholder data (Replace with logic)")

def hashtags():
    print("Fetching hashtags used by the target...")
    print("Hashtags:", ", ".join(mock_data["hashtags"]))

def info():
    print("Fetching target info...")
    profile = mock_data["profile"]
    print(f"Username: {profile['username']}")
    print(f"Bio: {profile['bio']}")
    print(f"Followers: {profile['followers']}")
    print(f"Following: {profile['followings']}")
    print(f"Posts: {profile['posts']}")

def likes():
    print("Fetching total likes of target's posts...")
    total_likes = sum(post["likes"] for post in mock_data["posts"])
    print(f"Total Likes: {total_likes}")

def mediatype():
    print("Fetching post types (photo or video)...")
    print("Post Types: Placeholder data (Replace with logic)")

def photodes():
    print("Fetching descriptions of target's photos...")
    print("Descriptions: Placeholder data (Replace with logic)")

def photos():
    print("Downloading user's photos...")
    print("Photos: Downloading placeholder (Implement scraping logic here)")

def propic():
    print("Downloading user's profile picture...")
    print("Profile Picture: Placeholder data (Implement scraping logic here)")

def stories():
    print("Downloading user's stories...")
    print("Stories: Placeholder data (Implement scraping logic here)")

def tagged():
    print("Fetching list of users tagged by the target...")
    print("Tagged Users:", ", ".join(mock_data["tagged_users"]))

def wcommented():
    print("Fetching list of users who commented on target's photos...")
    print("Commenters:", ", ".join(mock_data["commenters"]))

def wtagged():
    print("Fetching list of users who tagged the target...")
    print("Tagged by: Placeholder data (Implement scraping logic here)")

# Features Menu
def display_menu():
    print("\nSelect an operation:")
    print("1. Get all registered addresses by target photos (addrs)")
    print("2. Get user's photos captions (captions)")
    print("3. Get total comments of target's posts (comments)")
    print("4. Get target followers (followers)")
    print("5. Get users followed by target (followings)")
    print("6. Get email of target followers (fwersemail)")
    print("7. Get email of users followed by target (fwingsemail)")
    print("8. Get phone numbers of target followers (fwersnumber)")
    print("9. Get phone numbers of users followed by target (fwingsnumber)")
    print("10. Get hashtags used by target (hashtags)")
    print("11. Get target info (info)")
    print("12. Get total likes of target's posts (likes)")
    print("13. Get user's post types (photo or video) (mediatype)")
    print("14. Get descriptions of target's photos (photodes)")
    print("15. Download user's photos (photos)")
    print("16. Download user's profile picture (propic)")
    print("17. Download user's stories (stories)")
    print("18. Get list of users tagged by target (tagged)")
    print("19. Get list of users who commented on target's photos (wcommented)")
    print("20. Get list of users who tagged target (wtagged)")
    print("21. Exit")
    return input("\nEnter your choice (1-21): ")

# Main Program
if __name__ == "__main__":
    display_ascii_art()
    print("Welcome to OSINTgram - An Instagram OSINT Tool\n")

    while True:
        user_choice = display_menu()
        if user_choice == '1':
            addrs()
        elif user_choice == '2':
            captions()
        elif user_choice == '3':
            comments()
        elif user_choice == '4':
            followers()
        elif user_choice == '5':
            followings()
        elif user_choice == '6':
            fwersemail()
        elif user_choice == '7':
            fwingsemail()
        elif user_choice == '8':
            fwersnumber()
        elif user_choice == '9':
            fwingsnumber()
        elif user_choice == '10':
            hashtags()
        elif user_choice == '11':
            info()
        elif user_choice == '12':
            likes()
        elif user_choice == '13':
            mediatype()
        elif user_choice == '14':
            photodes()
        elif user_choice == '15':
            photos()
        elif user_choice == '16':
            propic()
        elif user_choice == '17':
            stories()
        elif user_choice == '18':
            tagged()
        elif user_choice == '19':
            wcommented()
        elif user_choice == '20':
            wtagged()
        elif user_choice == '21':
            print("Exiting the tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
