from mongoengine import Document, StringField, IntField, DateTimeField, FloatField, ListField, DictField, ObjectIdField


class Device01(Document): #leituras de alguma coisa
    id_tago = ObjectIdField()
    time = DateTimeField()
    unit = StringField()
    value = FloatField()
    variable = StringField()
    metadata = DictField()
    group = ObjectIdField()
    device = ObjectIdField()
    test = ListField()
