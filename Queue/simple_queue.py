class Queue:
    def __init__(self, limit):
        self.queue = []
        self.limit = limit

    def enqueue(self, element):
        if len(self.queue) < self.limit:
            self.queue.append(element)
            print("Added:", element)
        else:
            print("Sorry, the queue is full")

    def dequeue(self):
        if self.queue:
            removed_element = self.queue.pop(0)
            print("Removed:", removed_element)
        else:
            print("Sorry, the queue is empty")

    def display(self):
        if self.queue:
            print("Queue:", self.queue)
        else:
            print("Queue is empty")


def main():
    limit = 5
    queue_obj = Queue(limit)

    while True:
        print("\n1. Enqueue 2. Dequeue 3. Display 4. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = input("Enter value to enqueue: ")
            queue_obj.enqueue(element)
        elif choice == 2:
            queue_obj.dequeue()
        elif choice == 3:
            queue_obj.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
