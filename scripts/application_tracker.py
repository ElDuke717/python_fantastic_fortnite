class ApplicationTracker:
    def __init__(self):
        self.data = {}

    def add_entry(self, entry_type, value):
        if entry_type in self.data:
            self.data[entry_type] += value
        else:
            self.data[entry_type] = value

    def update_entry(self, entry_type, new_value):
        if entry_type in self.data:
            self.data[entry_type] = new_value
        else:
            print(f"Entry type '{entry_type}' not found.")

    def print_data(self):
        for entry_type, value in self.data.items():
            print(f"{entry_type}: {value}")


data = [
    {"type": "Applications", "value": 22},
    {"type": "E-mail", "value": 2},
    {"type": "Phone Screens", "value": 1},
    {"type": "Interviews", "value": 0},
    {"type": "Rejections", "value": 9},
    {"type": "Acceptances", "value": 0},
    {"type": "Offers", "value": 0}
]

# Create an instance of ApplicationTracker
tracker = ApplicationTracker()

# Populate the tracker with data
for entry in data:
    tracker.add_entry(entry["type"], entry["value"])

# Print the initial data
print("Initial data:")
tracker.print_data()

# Update a specific entry
tracker.update_entry("Applications", 25)

# Print the updated data
print("\nUpdated data:")
tracker.print_data()
