from .nodes import *
import graphene
from graphene_django.filter import DjangoFilterConnectionField

class Query(graphene.ObjectType):

    message = graphene.Node.Field(MessageNode)
    all_messages = DjangoFilterConnectionField(MessageNode)

    symptom = graphene.Node.Field(SymptomNode)
    all_symptoms = DjangoFilterConnectionField(SymptomNode)

    disease = graphene.Node.Field(DiseaseNode)
    all_diseases = DjangoFilterConnectionField(DiseaseNode)



schema = graphene.Schema(query=Query)