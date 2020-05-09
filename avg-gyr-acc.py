import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793
  AvgGyr = None
  G = None
  Gyr = None
  aG = None
  dg = None

  def execMain(self):

    
    self.G = (time.time() - self.__interpretation_started_timestamp__)
    self.dg = (time.time() - self.__interpretation_started_timestamp__) - self.G
    self.Gyr = 0
    self.aG = self.Gyr + self.dg * brick.gyroscope().read()[1]
    while True:
      self.dg = (time.time() - self.__interpretation_started_timestamp__) - self.G
      if (self.Gyr > 15):
        brick.display().showImage("media/trik_smile_sad.png")
        brick.motor("M3").powerOff()
        brick.motor("M4").powerOff()
        
      else:
        brick.motor("M3").setPower(100)
        brick.motor("M4").setPower(100)
        
        script.wait(1000)
        
        self.AvgGyr = self.Gyr + brick.gyroscope().read()[1]
        self.G = (time.time() - self.__interpretation_started_timestamp__)
        self.Gyr = self.Gyr + self.dg * (brick.gyroscope().read()[1] - self.AvgGyr) * 180 / (self.pi * 82026)

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
