class OddIndex:
    def __init__(self):
        self.inp = ""
        
    def input_s(self):
        self.inp = input(" string ")
      
    def details(self):
        x = self.inp[1::2]
        print (x)
        
    R=OddIndex()
    R.input_s()
    R.details()

