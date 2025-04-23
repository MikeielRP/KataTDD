class conjunto:
    def __init__(self,conjunto):
        self.conjunto=conjunto

    def promedio ( self ):
        if len(self.conjunto)==1:
            return (self.conjunto[0])
        else:
            return None