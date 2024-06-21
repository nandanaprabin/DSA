class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]

    def rear(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[-1]

def main():
    max_size = int(input("Enter the maximum size of the queue: "))
    queue = Queue(max_size)
    
    while True:
        print("\nChoose an operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Rear")
        print("5. Check if empty")
        print("6. Check if full")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            try:
                item = input("Enter the item to enqueue: ")
                queue.enqueue(item)
                print(f"Enqueued {item} to the queue.")
            except Exception as e:
                print(e)
        
        elif choice == 2:
            try:
                item = queue.dequeue()
                print(f"Dequeued {item} from the queue.")
            except Exception as e:
                print(e)
        
        elif choice == 3:
            try:
                item = queue.front()
                print(f"Front item is {item}.")
            except Exception as e:
                print(e)
        
        elif choice == 4:
            try:
                item = queue.rear()
                print(f"Rear item is {item}.")
            except Exception as e:
                print(e)
        
        elif choice == 5:
            if queue.is_empty():
                print("The queue is empty.")
            else:
                print("The queue is not empty.")
        
        elif choice == 6:
            if queue.is_full():
                print("The queue is full.")
            else:
                print("The queue is not full.")
        
        elif choice == 7:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()