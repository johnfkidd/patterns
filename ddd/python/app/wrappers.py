class CallableValueObject:
    def __init__(self, value, **methods):
        self._value = value
        self._methods = methods

    def __call__(self):
        return self._value

    def __getattr__(self, name):
        if name in self._methods:
            return self._methods[name]
        raise AttributeError(f"{name} is not a valid method")
