from navigator import Navigator


def main():
    item_list = ['Books', 'Furniture', 'Electronics', 'Clothing', 'Toys']

    print("Logistics Delivery Simulation")
    logistics_medium = input("Enter logistics method (road/sea): ").strip().lower()
    navigator = Navigator()

    if logistics_medium == "sea":
        logistics = navigator.get_medium(logistics_medium)
        print(logistics.deliver("Books"))

    elif logistics_medium == "road":
        logistics = navigator.get_medium(logistics_medium)
        print(logistics.deliver("Furniture"))
    else:
        print("Invalid logistics method. Please choose 'road' or 'sea'.")


if __name__ == "__main__":
    main()
