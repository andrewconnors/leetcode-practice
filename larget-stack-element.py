class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack():
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()
    
    def get_max(self):
        return self.max_stack.peek()
    
    def push(self, item):
        self.stack.push(item)
        if self.max_stack.peek():
            if item > self.max_stack.peek():
                self.max_stack.push(item)
        else:
            self.max_stack.push(item)
    
    def pop(self):
        item = self.stack.pop()
        if item == self.max_stack.peek():
            self.max_stack.pop()
        return item

if __name__ == "__main__":
    ms = MaxStack()
    ms.push(6)
    ms.push(7)
    print(ms.get_max())
    ms.pop()
    ms.push(4)
    print(ms.get_max())
    

