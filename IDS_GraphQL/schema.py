import graphene
import graphql_jwt
from Authentication.schema import login_schema
from Core.schema import productdetails_schema
from idscore.schema import idscore_schema

# Combine all query types from different schemas into one Query class

class Query(
    login_schema.Query,
    productdetails_schema.Query,
    idscore_schema.Query,
    graphene.ObjectType
):
    pass


# Combine all mutation types from different schemas into one Mutation class

class Mutation(
    login_schema.Mutation,
    productdetails_schema.Mutation,
    idscore_schema.Mutation,
    graphene.ObjectType
):
    # Additional JWT token-related mutations
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()

# Define the GraphQL schema with combined Query and Mutation
schema = graphene.Schema(query=Query, mutation=Mutation)