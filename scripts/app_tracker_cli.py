# Import the argparse library for creating a command-line interface
import argparse

# Sample data (replace this with your actual data)
data = [
    { 'type': 'Applications', 'value': 22 },
    { 'type': 'E-mail', 'value': 2 },
    { 'type': 'Phone Screens', 'value': 1 },
    { 'type': 'Interviews', 'value': 0 },
    { 'type': 'Rejections', 'value': 9 },
    { 'type': 'Acceptances', 'value': 0 },
    { 'type': 'Offers', 'value': 0 }
]

# Define a function to view the application tracker data
def view_data():
    print("Application Tracker Data:")
    for item in data:
        print(f"{item['type']}: {item['value']}")

# Define a function to update a data value based on type
def update_value(data_type, new_value):
    for item in data:
        if item['type'] == data_type:
            item['value'] = new_value
            print(f"Updated {data_type} value to {new_value}")
            break
    else:
        print(f"Data type '{data_type}' not found.")

# Define the main function that handles command-line arguments
def main():
    # Create an ArgumentParser object for handling command-line arguments
    parser = argparse.ArgumentParser(description="Application Tracker CLI")
    
    # Define command-line arguments using the add_argument method
    parser.add_argument("--view", action="store_true", help="View the application tracker data")
    parser.add_argument("--update", nargs=2, help="Update a data value (type new_value)")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check the parsed arguments and execute the corresponding actions
    if args.view:
        view_data()
    elif args.update:
        data_type, new_value = args.update
        update_value(data_type, int(new_value))
    else:
        print("Use --view to view data or --update to update data.")

# Execute the main function if the script is run as the main module
if __name__ == "__main__":
    main()
