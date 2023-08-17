class Stack:
    stack = []

    def __int__(self):
        self.stack = []

    def push_element(self):
        element = input('Enter your number : ')
        self.stack.append(element)
        print(self.stack)

    def pop_element(self):
        self.stack.pop()
        print(self.stack)

    def check_top(self):
        if len(self.stack) > 0:
            print(self.stack[-1])
        else:
            print("stack is empty")


while True:
    print("1. Push 2. Pop 3. Check Top 4. Quit")

    choice = int(input("Enter your choice : "))
    stack_obj = Stack()
    if choice == 1:
        stack_obj.push_element()
    elif choice == 2:
        stack_obj.pop_element()
    elif choice == 3:
        stack_obj.check_top()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
