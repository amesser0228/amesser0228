"""Class to implement linked list node"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


'''Class to implement linked list'''


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("End")

    def last_node_data(self):
        if not self.head:
            return "The list is empty."
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node.data


my_list1 = LinkedList()

my_list1.append(1)
my_list1.append(2)
my_list1.append(3)
my_list1.append(4)

# Ensure the list is not empty before calling last_node_data
if my_list1.head:
    last_data = my_list1.last_node_data()
    user_input = input(f"Enter any number greater than {last_data}: ")
else:
    user_input = input("Enter any number: ")

my_list1.append(user_input)

print('linked list 1: ', end="")
my_list1.display()
