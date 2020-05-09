import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793
  T = None
  dt = None
  stop = None

  /* Threads declarations */
  var TASK_aeffa5b074e3bb529c1cc5c8f9d72;

  /* Threads */
  TASK_aeffa5b074e3bb529c1cc5c8f9d72 = function()
  {
    self.dt = 0
    self.T = (time.time() - self.__interpretation_started_timestamp__)
    while True:
      self.dt = (time.time() - self.__interpretation_started_timestamp__) - self.T
      if self.dt > 10000 and brick.encoder("E3").read() < 5000:
        Threading.sendMessage("main", 1)
        
      if self.dt > 10000:
        self.T = (time.time() - self.__interpretation_started_timestamp__)
        brick.encoder("E3").reset()
        
  }

  def execMain(self):

    
    while not brick.keys().wasPressed(Right):
      script.wait(100)
    
    self.stop = 0
    Threading.startThread("Attention", "TASK_aeffa5b074e3bb529c1cc5c8f9d72")
    self.stop = Threading.receiveMessage(False)
    
    while True:
      if (brick.sensor("A1").read() < 30):
        brick.motor("M3").powerOff()
        brick.motor("M4").powerOff()
        
        brick.motor("M3").setPower(-(100))
        brick.motor("M4").setPower(-(100))
        
        script.wait(3000)
        
        brick.motor("M3").powerOff()
        brick.motor("M4").powerOff()
        
        brick.motor("M4").setPower(100)
        
        script.wait(400)
        
      else:
        brick.motor("M3").setPower(100)
        brick.motor("M4").setPower(100)
        

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
