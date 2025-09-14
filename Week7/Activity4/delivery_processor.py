from navigator import Navigator


def main():
    ROAD_MEDIUM = "road"
    SEA_MEDIUM = "sea"
    item_list = ["Books", "Furniture", "Electronics", "Clothing", "Toys"]

    print("Logistics Delivery Simulation")
    logistics_medium = input("Enter logistics method (road/sea): ").strip().lower()
    navigator = Navigator()

    if logistics_medium == SEA_MEDIUM:
        logistics = navigator.get_medium(logistics_medium)
        print(logistics.deliver("Books"))

    elif logistics_medium == ROAD_MEDIUM:
        logistics = navigator.get_medium(logistics_medium)
        print(logistics.deliver("Furniture"))
    else:
        print("Invalid logistics method. Please choose 'road' or 'sea'.")


if __name__ == "__main__":
    main()
