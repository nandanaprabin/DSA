class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def find_middle(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        middle_index = self.size() // 2
        return self.items[middle_index]

def main():
    stack = Stack()
    
    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Find middle element")
        print("5. Check if empty")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter the item to push: ")
            stack.push(item)
            print(f"Pushed {item} to the stack.")
        
        elif choice == 2:
            try:
                item = stack.pop()
                print(f"Popped {item} from the stack.")
            except Exception as e:
                print(e)
        
        elif choice == 3:
            try:
                item = stack.peek()
                print(f"Top item is {item}.")
            except Exception as e:
                print(e)
        
        elif choice == 4:
            try:
                item = stack.find_middle()
                print(f"Middle element is {item}.")
            except Exception as e:
                print(e)
        
        elif choice == 5:
            if stack.is_empty():
                print("The stack is empty.")
            else:
                print("The stack is not empty.")
        
        elif choice == 6:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
