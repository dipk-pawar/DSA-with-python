class Stack:
    def __init__(self):
        self.stack = []

    def push_element(self, element):
        self.stack.append(element)
        print("Pushed:", element)
        self.display()

    def pop_element(self):
        if self.stack:
            removed_element = self.stack.pop()
            print("Popped:", removed_element)
            self.display()
        else:
            print("Stack is empty")

    def check_top(self):
        if self.stack:
            print("Top element:", self.stack[-1])
        else:
            print("Stack is empty")

    def display(self):
        if self.stack:
            print("Stack:", self.stack)
        else:
            print("Stack is empty")


def main():
    stack_obj = Stack()

    while True:
        print("\n1. Push 2. Pop 3. Check Top 4. Display 5. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = input("Enter value to push: ")
            stack_obj.push_element(element)
        elif choice == 2:
            stack_obj.pop_element()
        elif choice == 3:
            stack_obj.check_top()
        elif choice == 4:
            stack_obj.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
