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

    def has_item(self):
        """
        Gibt True zurück, falls ein Wurzelinhalt gesetzt ist.
        """
        return self.inhalt is not None

    def get_item(self):
        """
        Liefert den Wurzelinhalt,
        oder wirft RuntimeError, wenn keiner vorhanden ist.
        """
        if self.has_item():
            return self.inhalt
        else:
            raise RuntimeError("Es gibt keinen Wurzelinhalt.")

    def set_item(self, inhalt):
        """
        Setzt den Wurzelinhalt auf inhalt.
        """
        self.inhalt = inhalt

    def delete_item(self):
        """
        Löscht den Wurzelinhalt (setzt ihn auf None).
        """
        self.inhalt = None

    def is_leaf(self):
        """
        True, wenn kein linker und kein rechter Teilbaum existiert.
        """
        return (self.left is None) and (self.right is None)

    def has_left(self):
        """
        True, wenn ein linker Teilbaum existiert.
        """
        return self.left is not None

    def get_left(self):
        """
        Gibt den linken Teilbaum zurück oder None.
        """
        return self.left

    def set_left(self, b):
        """
        Setzt den linken Teilbaum auf b.
        """
        self.left = b

    def delete_left(self):
        """
        Löscht den linken Teilbaum,
        wirft RuntimeError, falls keiner existiert.
        """
        if self.left is None:
            raise RuntimeError("Kein linker Teilbaum vorhanden.")
        self.left = None

    def has_right(self):
        """
        True, wenn ein rechter Teilbaum existiert.
        """
        return self.right is not None

    def get_right(self):
        """
        Gibt den rechten Teilbaum zurück oder None.
        """
        return self.right

    def set_right(self, b):
        """
        Setzt den rechten Teilbaum auf b.
        """
        self.right = b

    def delete_right(self):
        """
        Löscht den rechten Teilbaum,
        wirft RuntimeError, falls keiner existiert.
        """
        if self.right is None:
            raise RuntimeError("Kein rechter Teilbaum vorhanden.")
        self.right = None
