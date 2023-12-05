class searchReq:
    def __init__(self, id, uuid, type, context):
        self.id = id
        self.uuid = uuid
        self.type = type
        self.context = context

    def __str__(self):
        return f"{self.id}, {self.uuid} {self.type}, {self.context}"
