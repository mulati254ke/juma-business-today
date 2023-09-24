class BusinessUnit:
    def __init__(self, name, description, characteristics, advantages, disadvantages):
        self.name = name
        self.description = description
        self.characteristics = characteristics
        self.advantages = advantages
        self.disadvantages = disadvantages

    def display_info(self):
        print(f"** {self.name} **")
        print(self.description)
        print("\nCharacteristics:")
        for char in self.characteristics:
            print(f"- {char}")
        print("\nAdvantages:")
        for adv in self.advantages:
            print(f"- {adv}")
        print("\nDisadvantages:")
        for disadv in self.disadvantages:
            print(f"- {disadv}")
        print("\n")


# Define a dictionary to store information about different forms of business units
business_units = {
    "Sole Proprietorship": BusinessUnit(
        name="Sole Proprietorship",
        description="A sole proprietorship is a business owned and operated by a single individual.",
        characteristics=[
            "Owned by one person",
            "Easy to form and dissolve",
            "Owner has unlimited liability",
            "Owner enjoys all the profits and bears all the losses",
            "Owner has complete control over the business",
        ],
        advantages=[
            "Easy to start and manage",
            "Owner has complete control over the business",
            "Owner enjoys all the profits",
        ],
        disadvantages=[
            "Owner has unlimited liability",
            "Owner bears all the losses",
            "Owner may have limited resources and expertise",
        ],
    ),
    # Add more forms of business units here
}


def main():
    print("Forms of Business Units - Information")
    print("=======================================")
    print("Choose a form of business unit to learn more:")
    for index, unit_name in enumerate(business_units.keys(), start=1):
        print(f"{index}. {unit_name}")

    try:
        choice = int(input("Enter the number of your choice: "))
        if 1 <= choice <= len(business_units):
            selected_unit_name = list(business_units.keys())[choice - 1]
            selected_unit = business_units[selected_unit_name]
            selected_unit.display_info()
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
