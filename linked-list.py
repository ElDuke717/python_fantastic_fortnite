# Define a class for the individual nodes in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data for this node
        self.next = None   # Initialize the next pointer to None

# Define a class for the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list to None (empty list)

    # Method to append a new node with data to the end of the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:
            self.head = new_node  # If the list is empty, set the new node as the head
            return
        current = self.head  # Start from the head of the list
        while current.next:
            current = current.next  # Traverse the list until the last node
        current.next = new_node  # Set the next of the last node to the new node

    # Method to display the elements of the linked list
    def display(self):
        current = self.head  # Start from the head of the list
        while current:
            print(current.data, end=" -> ")  # Print the data of the current node
            current = current.next  # Move to the next node
        print("None")  # Print "None" to indicate the end of the list

# Create an instance of the linked list
my_list = LinkedList()

# Append elements to the linked list
my_list.append(10)
my_list.append(20)
my_list.append(30)

# Display the linked list
my_list.display()
my_list.append(40)
my_list.display()
