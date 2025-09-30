class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.back == None:
            self.front = new_node
            self.back = new_node
            self.length += 1
            return
        self.back.next = new_node
        self.back = new_node
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")    
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.back = None
        return temp.data
   
    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty queue")
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.length +=1
    
    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        popped_node = self.top
        self.top = self.top.next
        self.length -=1
        return popped_node.data

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self.top.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def printStack(self):
        currnode = self.top
        while currnode:
            print(currnode.data,end= " <- ")
            currnode = currnode.next
        print()

class HashTable:
    def __init__(self, size =10):
        self.list = [[] for _ in range(size)]

    def add(self, name):
        index = self.hash_function(name)
        self.list[index].append(name)

    def hash_function(self, data):
        sum_of_chars = 0
        for char in data:
            sum_of_chars += ord(char)

        return sum_of_chars % 10
    
    def contains(self, name):
        index = self.hash_function(name)
        return name in self.list[index]
    
    def remove(self, name):
        index = self.hash_function(name)
        bucket = self.list[index]
        if name in bucket:
            bucket.remove(name)
            return True
        return False

    def printHash(self):
        print(self.list)

##Queue
print("Queue")
# 1. Dequeue en cola vacía, debe ser error
q = Queue()
try:
    q.dequeue()
except IndexError as e:
    print("Test 1:", e)   
# Resultado: "Dequeue from empty queue"

# 2. Enqueue y Dequeue normal, debe salir primero A y luego B
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
print("Test 2:", q.dequeue() == "A" and q.dequeue() == "B")  
# Resultado: True
q.dequeue()

# 3. Peek y size, Peek debe regresar "X", tamaño debe ser 2
q.enqueue("X")
q.enqueue("Y")
print("Test 3:", q.peek() == "X" and q.size() == 2)  
# Resultado: True 

##Stack
print()
print("Stack")
# 1. Pop en pila vacía, debe ser error
s = Stack()
try:
    s.pop()
except IndexError as e:
    print("Test 1:", e)   
# Resultado: "Pop from empty stack"

# 2. Push y Pop normal, debe salir primero 30 y luego 20
s.push(10)
s.push(20)
s.push(30)
print("Test 2:", s.pop() == 30 and s.pop() == 20)  
# Resultado: True
s.pop()

# 3. Peek y size, Peek debe regresar "B", tamaño debe ser 2
s.push("A")
s.push("B")
print("Test 3:", s.peek() == "B" and s.size() == 2)  
# Resultado: True

##Hash
print()
print("Hash")
# 1. Remove de elemento inexistente, debe regresar False
h = HashTable(100)
print("Test 1:", h.remove("Inexistente"))  
# Resultado: False

# 2. Add y contains, "Jair" existe, "Felipe" no
h.add("Jair")
h.add("Manuel")
print("Test 2:", h.contains("Jair") and not h.contains("Felipe"))  
# Resultado: True

# 3. Add y luego remove, después debe ser False
h.add("Felipe")
print("Antes de remove:", h.contains("Felipe"))   # True
h.remove("Felipe")
print("Test 3:", not h.contains("Felipe"))  
# Resultado: True

