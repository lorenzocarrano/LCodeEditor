from threading import Lock
import sys
class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

class StdOutManager(Singleton):
    def __init__(self):
        self._mutexLock = Lock()
        self.stdoutInstance = sys.stdout

    def stdoutPrint(self, data, endCharacter, fOut=None, mode="w"):
        self._mutexLock.acquire()
        if fOut == None:
            sys.stdout = self.stdoutInstance
            print(data, end=endCharacter)
        else:
            f = open(fOut, mode)
            sys.stdout = f
            print(data, end=endCharacter)
            sys.stdout = self.stdoutInstance
            f.close()
        self._mutexLock.release()
'''
#test
if __name__ == "__main__":
    inst = StdOutManager()
    inst.stdoutPrint("test")
'''
