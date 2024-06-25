class Observer:
    def update(self, message):
        pass

class Logger(Observer):
    def __init__(self):
        self.log_file = 'app.log'

    def notify(self, message):
        self.update(message)

    def update(self, message):
        with open(self.log_file, 'a') as log:
            log.write(f'{message}\n')