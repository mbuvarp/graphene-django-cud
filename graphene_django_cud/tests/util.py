from string import ascii_uppercase

import graphene
from graphene import Schema

from graphene_django_cud.tests.dummy_query import DummyQuery


def create_mutation_schema(*mutations):
    def to_snake_case(m):
        name = m.__name__
        name = name if not name.endswith("Mutation") else name[:-8]
        return "".join(["_" + s if i > 0 and s in ascii_uppercase else s for i, s in enumerate(name)]).lower()

    mut = {}
    for mutation in mutations:
        name = to_snake_case(mutation)
        mut[name] = mutation.Field()

    mutations_class = type("Mutations", (graphene.ObjectType,), mut)

    return Schema(query=DummyQuery, mutation=mutations_class)
