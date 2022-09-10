from mongoengine import Document, StringField, IntField, DateTimeField, FloatField, ListField, DictField, ObjectIdField


class Device01(Document):
    id_tago = ObjectIdField()
    time = DateTimeField()
    unit = StringField()
    value = FloatField()
    variable = StringField()
    metadata = DictField()
    group = ObjectIdField()
    device = ObjectIdField()
    test = ListField()
