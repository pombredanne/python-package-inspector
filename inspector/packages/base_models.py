from neo4django import Outgoing
from neo4django.db import models


class PythonNode(models.NodeModel):
    name = models.StringProperty()
    owner = models.Relationship('PythonNode',
        rel_type=Outgoing.OWNER,
        single=True,
        related_name='members')


class CodeNode(PythonNode):
    code = models.StringProperty()
    line_number = models.IntegerProperty()
