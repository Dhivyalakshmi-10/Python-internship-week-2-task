import random

# Different nickname combination styles
def combine_names(name1, name2):
    styles = [
        name1[:2] + name2[-2:],  # First 2 of name1 + last 2 of name2
        name1[:len(name1)//2] + name2[len(name2)//2:],  # First half + second half
        "".join(random.choice(name1 + name2) for _ in range(4)),  # Random chars
        name1[:3] + name2[:3],  # First 3 letters of both
        name1[::-1][:2] + name2[::-1][:2]  # Reverse combo
    ]
    return styles

def nickname_generator():
    history = []
    while True:
        name1 = input("Enter first name: ").capitalize()
        name2 = input("Enter second name: ").capitalize()

        styles = combine_names(name1, name2)
        print("\n✨ Generated Nicknames:")
        for idx, nickname in enumerate(styles, 1):
            print(f"{idx}. {nickname}")
            history.append(nickname)

        choice = input("\nDo you want to try again? (y/n): ")
        if choice.lower() != 'y':
            print("\n📜 Nickname History:", history)
            print("👋 Exiting Nickname Generator...")
            break

if __name__ == "__main__":
    nickname_generator()
