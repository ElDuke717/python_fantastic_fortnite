import argparse

# Sample data (replace this with your actual data)
data = [
    { 'type': 'Applications', 'value': 22 },
    { 'type': 'E-mail', 'value': 2 },
    { 'type': 'Phone Screens', 'value': 1 },
    # ... other data items ...
]

def view_data():
    print("Application Tracker Data:")
    for item in data:
        print(f"{item['type']}: {item['value']}")

def update_value(data_type, new_value):
    for item in data:
        if item['type'] == data_type:
            item['value'] = new_value
            print(f"Updated {data_type} value to {new_value}")
            break
    else:
        print(f"Data type '{data_type}' not found.")

def main():
    parser = argparse.ArgumentParser(description="Application Tracker CLI")
    parser.add_argument("--view", action="store_true", help="View the application tracker data")
    parser.add_argument("--update", nargs=2, help="Update a data value (type new_value)")

    args = parser.parse_args()

    if args.view:
        view_data()
    elif args.update:
        data_type, new_value = args.update
        update_value(data_type, int(new_value))
    else:
        print("Use --view to view data or --update to update data.")

if __name__ == "__main__":
    main()
