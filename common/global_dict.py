# 保障全局字典不被污染
class GlobalDict(object):
    _global_dict = {}
    def  set_dict(self,key,value):
        self._global_dict[key] = value
    def get_dict(self,key):
        return self._global_dict[key]
    def show_dict(self):
        return self._global_dict