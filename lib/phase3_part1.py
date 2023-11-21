class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        return keyword.lower() in (self.title.lower(), self.artist.lower())


class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add(self, track):
        if isinstance(track, Track):
            self.tracks.append(track)

    def search(self, keyword):
        return [track for track in self.tracks if track.matches(keyword)]
    
##############################

class Task:
    def __init__(self, title):
        self.title = title
        self.complete = False

    def mark_complete(self):
        self.complete = True

    def is_complete(self):
        return self.complete
    
    
class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def all(self):
        return self.tasks

    def all_complete(self):
        if len(self.tasks) == 0:
            return False
        return all([task.is_complete() for task in self.tasks])
    
    
    
class TaskFormatter:
    def __init__(self, task): # task is an instance of Task
        pass

    def format(self):
        # Returns the task formatted as a string.
        # If the task is not complete, the format is:
        # - [ ] Task title
        # If the task is complete, the format is:
        # - [x] Task title
        pass