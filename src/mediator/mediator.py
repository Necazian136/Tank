class Mediator:
    actions = {}

    def register(self, name: str, func: callable):
        self.actions[name] = func

    def call(self, name, *args, **kwargs):
        if self.actions.get(name):
            return self.actions[name](*args, **kwargs)
        return None
