# -*- coding: utf-8 -*-

class BinTree(object):
    def __init__(self, inhalt=None):
        """
        Erzeugt einen Binärbaum.
        Wird kein Inhalt übergeben, ist der Baum leer.
        """
        self.inhalt = inhalt
        self.left = None
        self.right = None

    def hasItem(self):
        """
        Gibt True zurück, falls ein Wurzelinhalt gesetzt ist.
        """
        return self.inhalt is not None

    def getItem(self):
        """
        Liefert den Wurzelinhalt,
        oder wirft RuntimeError, wenn keiner vorhanden ist.
        """
        if self.hasItem():
            return self.inhalt
        else:
            raise RuntimeError("Es gibt keinen Wurzelinhalt.")

    def setItem(self, inhalt):
        """
        Setzt den Wurzelinhalt auf inhalt.
        """
        self.inhalt = inhalt

    def deleteItem(self):
        """
        Löscht den Wurzelinhalt (setzt ihn auf None).
        """
        self.inhalt = None

    def isLeaf(self):
        """
        True, wenn kein linker und kein rechter Teilbaum existiert.
        """
        return (self.left is None) and (self.right is None)

    def hasLeft(self):
        """
        True, wenn ein linker Teilbaum existiert.
        """
        return self.left is not None

    def getLeft(self):
        """
        Gibt den linken Teilbaum zurück oder None.
        """
        return self.left

    def setLeft(self, b):
        """
        Setzt den linken Teilbaum auf b.
        """
        if b is not None and not isinstance(b, BinTree):
            raise TypeError("left child must be a BinTree or None")
        self.left = b

    def deleteLeft(self):
        """
        Löscht den linken Teilbaum,
        wirft RuntimeError, falls keiner existiert.
        """
        if self.left is None:
            raise RuntimeError("Kein linker Teilbaum vorhanden.")
        self.left = None

    def hasRight(self):
        """
        True, wenn ein rechter Teilbaum existiert.
        """
        return self.right is not None

    def getRight(self):
        """
        Gibt den rechten Teilbaum zurück oder None.
        """
        return self.right

    def setRight(self, b):
        """
        Setzt den rechten Teilbaum auf b.
        """
        if b is not None and not isinstance(b, BinTree):
            raise TypeError("right child must be a BinTree or None")
        self.right = b

    def deleteRight(self):
        """
        Löscht den rechten Teilbaum,
        wirft RuntimeError, falls keiner existiert.
        """
        if self.right is None:
            raise RuntimeError("Kein rechter Teilbaum vorhanden.")
        self.right = None
