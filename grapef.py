class GrapeFalvours():
    def __init__(self, grape_family, grape_processed):
        self.grape_family = grape_family
        self.grape_processed = grape_processed
        

    def getGrapeFamily(self):
        return f"This belongs to {self.grape_family} family from US south east. It is processed."