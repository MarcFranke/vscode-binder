class DynArray:
    def __init__(self):
        """
        Erstellt ein leeres DynArray.
        """
        self.data = []
    
    def isEmpty(self):
        """
        Gibt True zurück, wenn das DynArray leer ist, sonst False.
        """
        return len(self.data) == 0
    
    def getItem(self, index):
        """
        Liefert das Element am spezifizierten index.
        """
        if index < 0 or index >= len(self.data):
            raise IndexError("index out of range")
        return self.data[index]
    
    def append(self, item):
        """
        Fuegt ein Element ans Ende des DynArrays an.
        """
        self.data.append(item)
    
    def insertAt(self, index, item):
        """
        Fügt das übergebene Element am spezifizierten index ein.
        """
        if index < 0 or index > len(self.data):
            raise IndexError("index out of range")
        self.data.insert(index, item)
    
    def setItem(self, index, item):
        """
        Überschreibt das Element am spezifizierten index 
        mit dem übergebenen Element.
        """
        if index < 0 or index >= len(self.data):
            raise IndexError("index out of range")
        self.data[index] = item
    
    def delete(self, index):
        """
        Löscht das Element am spezifizierten index ein.
        """
        if index < 0 or index >= len(self.data):
            raise IndexError("index out of range")
        del self.data[index]
    
    def getLength(self):
        """
        Liefert die Anzahl Elemente im DynArray.
        """
        return len(self.data)
    
    def __str__(self):
        """
        Ausgabe als String für print-Befehle
        """
        return f"DynArray({self.data})"