import sys
from subprocess import run
from libqtile.widget import base



class Prayer(base.InLoopPollText):
    def __init__(self,interval:int, **config):
        base.InLoopPollText.__init__(self,**config)
        self.update_interval = interval 
    def get_prayer(self):
        n_prayer = str(run(['next-prayer','--hybrid'],capture_output=True).stdout.decode("utf-8")).replace("\n", "").replace("AM",'').replace("PM",'')
        r_time = str(run(['next-prayer','--left'],capture_output=True).stdout.decode("utf-8")).replace("\n", "")[:5]
        out_put = f'{n_prayer}⏱️{r_time}'
        return out_put
    def poll(self):
        time  = self.get_prayer()
        return time

