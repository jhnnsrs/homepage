import graphene
from django.contrib.auth.models import User

from .models import *
from graphene import Node
from  graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

class MessageNode(DjangoObjectType):
    class Meta:
        model = Message
        interfaces = (Node,)
        filter_fields = ['name', 'id']

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (Node,)



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

    def resolve_associateddiseases(self, args, context, info):
        print(context.user)
        return self.associateddiseases.all()