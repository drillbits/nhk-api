class Choices(object):
    def __init__(self, model, code_map, name_map):
        self.model = model
        self.code_map = code_map
        self.name_map = name_map

    def code(self, key):
        return self.code_map.get(key, None)

    def name(self, key):
        return self.name_map.get(key, None)

    def detect(self, s):
        if isinstance(s, self.model):
            return s
        obj = self.code(s) or self.name(s)
        if obj:
            return obj
        else:
            raise KeyError("%s: %s not found" % (self.model.__name__, s))
