
class Observer():
    def __init__(self):
        self.list=[]
    def register_me(self,kod,callback):
        self.list.append({'code':kod,"def":callback})
    def _notify(self,kod):
        for a in self.list:
            if a['code']==kod:
                a['def']()