import graphene
from .models import *
from graphene import Node
from  graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

class MessageNode(DjangoObjectType):
    class Meta:
        model = Message
        interfaces = (Node,)
        filter_fields = ['name', 'id']

class NameNode(DjangoObjectType):
    class Meta:
        model = Name
        interfaces = (Node,)
        filter_fields = ["name"]

class DiseaseNode(DjangoObjectType):
    class Meta:
        model = Disease
        interfaces = (Node,)
        filter_fields = ["name"]

class SymptomNode(DjangoObjectType):
    class Meta:
        model = Symptom
        interfaces = (Node,)
        filter_fields = ["name", "abstract", "description"]

    associateddiseases = DjangoFilterConnectionField(DiseaseNode)

    def resolve_associateddiseases(self, *args):
        return self.associateddiseases.all()