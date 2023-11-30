import uuid


def get_id():
    return uuid.uuid4()


class IDManager:
    def __int__(self):
        self.id_list = []

