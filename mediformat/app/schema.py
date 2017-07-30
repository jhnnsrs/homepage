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

    user = graphene.Field(UserNode)

    def resolve_user(self, args, context, info):
        user = context.user
        if user.is_anonymous():
            anonymous = User.objects.get(pk=2)
            print(anonymous)
            return anonymous
        else:
            print(user.id)
            it = User.objects.get(pk=user.id)
            print(it)
            return it



schema = graphene.Schema(query=Query)