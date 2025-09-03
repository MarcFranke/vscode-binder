class Queue:
    def __init__(self):
        """
        Erzeugt eine leere Queue/Schlange.
        """
        self.items = []
    
    def enqueue(self, item):
        """
        Fuegt ein Element ans Ende der Schlange an.
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Löscht und liefert das forderste Element der Queue.
        """
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)
    
    def head(self):
        """
        Liefert das forderste Element ohne es zu löschen.
        """
        if self.isEmpty():
            raise IndexError("front from empty queue")
        return self.items[0]
    
    def isEmpty(self):
        """
        Gibt True zurück, wenn die Queue leer ist, sonst False.
        """
        return len(self.items) == 0
    
    def __str__(self):
        """
        Ausgabe als String für print-Befehle
        """
        return f"Queue({self.items})"
    