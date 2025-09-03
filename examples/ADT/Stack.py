class Stack:
    def __init__(self):
        """
        Erzeugt einen leeren Stack/Stapel/Keller.
        """
        self.items = []
    
    def push(self, item):
        """
        Legt ein Item oben auf den Stack.
        """
        self.items.append(item)
    
    def pop(self):
        """
        Löscht und liefert das oberste Element vom Stack.
        """
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def top(self):
        """
        Liefert das oberste Element, ohne es zu löschen.
        """
        if self.isEmpty():
            raise IndexError("top of empty stack")
        return self.items[-1]
    
    def isEmpty(self):
        """
        Gibt True zurück, wenn der Stack leer ist, sonst False.
        """
        return len(self.items) == 0
    
    def __str__(self):
        """
        Ausgabe als String für print-Befehle
        """
        return f"Stack({self.items})"
    
