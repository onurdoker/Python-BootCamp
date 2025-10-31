"""
Create a menu program (by defining category and food subcategories).
"""


class Menu:
    def __init__(self):
        self.menu = {
            "Appetizers": {
                "Soups": ["Ezogelin Soup", "Chicken Soup"],
                "Mezze": ["Hummus", "Haydari", "Eggplant Salad"],
            },
            "Main Courses": {
                "Meat Dishes": ["Iskender Kebab", "Adana Kebab", "Urfa Kebab"],
                "Chicken Dishes": ["Chicken Skewer", "Chicken Saute", "Oven Chicken"],
                "Seafood": ["Grilled Sea Bass", "Shrimp Casserole", "Fried Calamari"],
            },
            "Side Dishes": {
                "Salads": ["Seasonal Salad", "Arugula Salad"],
                "Rice": ["Pilaf", "Bulgur Pilaf"],
            },
            "Desserts": {
                "Hot Desserts": ["Kunefe", "Pudding"],
                "Cold Desserts": ["Magnolia", "Profiterole"],
            },
            "Beverages": {
                "Hot Drinks": ["Tea", "Turkish Coffee"],
                "Cold Drinks": ["Cola", "Lemonade"],
            },
        }

    def display_menu(self):
        print("========== RESTAURANT MENU ==========")

        for category, subcategories in self.menu.items():
            print(f"{category.upper()}")

            for subcategory, dishes in subcategories.items():
                print(f"\t{subcategory}")
                for dish in dishes:
                    print(f"\t\t- {dish}")


def search_category(self, category_name):
    if category_name in self.menu:
        print(f"{category_name}")
        for subcategory, dishes in self.menu[category_name].keys():
            print(f"\t{subcategory}:")
            for dish in dishes:
                print(f"\t\t- {dish}")
    else:
        print(f"\n {category_name} not found in the menu.")


if __name__ == "__main__":
    restaurant_menu = Menu()

    while True:
        print("========== MENU MANAGEMENT SYSTEM ==========")
        print("1. Display Menu")
        print("2. Search Category")
        print("3. Exit")

        choice = input("\nPlease enter your choice (1-3): ")

        if choice == "1":
            restaurant_menu.display_menu()

        elif choice == "2":
            print("\nCategories:", ", ".join(restaurant_menu.menu.keys()))
            category_name = input("\nPlease enter the category name: ")
            restaurant_menu.search_category(category_name)

        elif choice == "3":
            print("Exiting program... \nHave a nice day.")
            break
        else:
            print("\nInvalid choice. Please try again.")

        input("\nPress Enter to continue...")
