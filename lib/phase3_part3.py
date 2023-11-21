class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.locked = True

    def read(self):
        if self.locked:
            raise Exception("Go away!")
        return self.diary.read()

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False
    
    
    
class Diary:
    def __init__(self, contents):
        self.contents = contents
        pass

    def read(self):
        return self.contents