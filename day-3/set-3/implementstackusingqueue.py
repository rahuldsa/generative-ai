from queue import Queue

class Stack:
    def __init__(self):
        self.queue = Queue()

    def push(self, item):
        self.queue.put(item)

    def pop(self):
        size = self.queue.qsize()
        if size == 0:
            return None

        for _ in range(size - 1):
            self.queue.put(self.queue.get())

        return self.queue.get()

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())
stack.push(3)
print(stack.pop())
print(stack.pop())
