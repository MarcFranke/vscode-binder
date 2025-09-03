# example.py - Beispiele für die Datenstrukturen
from datastructures import Stack, Queue, DynArray, BinTree

# Stack Demo - LIFO (Last In, First Out)
stapel = Stack()
stapel.push("A")
stapel.push("B")
stapel.push("C")
print(f"Stack: {stapel}")
print(f"Pop: {stapel.pop()}")  # Gibt "C" zurück

# Queue Demo - FIFO (First In, First Out) 
warteschlange = Queue()
warteschlange.enqueue("Kunde 1")
warteschlange.enqueue("Kunde 2")
print(f"Queue: {warteschlange}")
print(f"Dequeue: {warteschlange.dequeue()}")  # Gibt "Kunde 1" zurück

# DynArray Demo - Dynamisches Array
array = DynArray()
array.append("Python")
array.append("Java")
array.insertAt(1, "C++")
print(f"Array: {array}")
print(f"Element 0: {array.getItem(0)}")  # Gibt "Python" zurück