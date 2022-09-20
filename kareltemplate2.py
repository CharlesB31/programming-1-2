 from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for move"""
    move()

   def tl(self):
   """turn left"""
    turn_left

    def tr(self):
    """turn right"""
    self.tl()
    self.tl()
    self.tl()

    def ta(self):
    """turn around"""  
    self.tl()
    self.tl()

    def pick(self):
    """pick beeper"""
    pick_beeper()

    def put(self):
   """put beeper"""
    put_beeper

   def put2(self):
   """put 2 beeper in a line"""
   self.put()
   self.m()
   self.put

   def put5(self):
   """put 2 beepers in a line"""
   self.put2()
   self.m()
   self.put2()
   self.m()
   self.put()

   def h(self):
   """Print H using beepers"""
   self.tl()
   self.put5()
   self.trl()
   self.m()
   self.m()
   self.m()
   self.tr()
   self.put2()
   self.ta()
   self.m()
   self.m()
   self.tl()
   self.m()
   





  
def main():
    """ Karel code goes here! """
    
    pass


if __name__ == "__main__":
    run_karel_program()