class EventLog:
    def __init__(self, source, events = None):
        self.source = source
        self.events = list({events})

