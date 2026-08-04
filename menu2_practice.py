def menu():
    print("=" * 40)
    print("         sAI-GPT MENU")
    print("=" * 40)
    print("1. Start Chat")
    print("2. Help")
    print("3. About")
    print("4. Exit")


menu()

choice = input("\nEnter your choice: ")

if choice == "1":
    print("Starting Chat...")

elif choice == "2":
    print("Showing Help...")

elif choice == "3":
    print("About sAI-GPT...")

elif choice == "4":
    print("Goodbye!")

else:
    print("Invalid Choice.")