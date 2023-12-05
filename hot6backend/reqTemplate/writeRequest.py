class writeReq:
    def __init__(self, id, target, type, context):
        self.id = id
        self.target = target
        self.type = type
        self.context = context

    def __str__(self):
        return f"{self.id}, {self.target}, {self.type}, {self.context}"
