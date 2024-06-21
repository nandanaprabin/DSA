class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.max_size

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

def main():
    max_size = int(input("Enter the maximum size of the stack: "))
    stack = Stack(max_size)
    
    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Check if full")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            try:
                item = input("Enter the item to push: ")
                stack.push(item)
                print(f"Pushed {item} to the stack.")
            except Exception as e:
                print(e)
        
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
            if stack.is_empty():
                print("The stack is empty.")
            else:
                print("The stack is not empty.")
        
        elif choice == 5:
            if stack.is_full():
                print("The stack is full.")
            else:
                print("The stack is not full.")
        
        elif choice == 6:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()