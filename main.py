from menu_actions import handle_view, handle_add, handle_update, handle_delete


def main():
    while True:
        print("\nShop Management System")
        print("1. View Products")
        print("2. Delete Product")
        print("3. Update Product")
        print("4. Add New Product")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                handle_view()
            elif choice == 2:
                handle_delete()
            elif choice == 3:
                handle_update()
            elif choice == 4:
                handle_add()
            elif choice == 5:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice! Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__== "__main__":
    main()