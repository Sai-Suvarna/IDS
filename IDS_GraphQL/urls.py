from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from Object_Detection.schema import wordsearch_schema, imageupload_schema
from graphene_file_upload.django import FileUploadGraphQLView
from Authentication.schema import login_schema
from Core.schema import productdetails_schema

from idscore.schema import idscore_schema

# Define urlpatterns for Django application

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
   
    # URLs for GraphQL endpoints with CSRF exemption and GraphiQL enabled

  
    # login_schema GraphQL endpoint
    path('login/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=login_schema))),

    # productdetails_schema GraphQL endpoint
    path('productdetails/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=productdetails_schema))),

    # idscore_schema GraphQL endpoint
    path('idsdetails/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=idscore_schema))),

    # word_search schema GraphQL endpoint
    path('searchword/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=wordsearch_schema))),

    # imageupload_schema GraphQL endpoint using FileUploadGraphQLView
    path('upload/', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True, schema=imageupload_schema))),
]







