# File ini berisi definisi model data untuk item
# Dalam contoh ini, model Item sederhana berisi id, name, dan description
class Item:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
