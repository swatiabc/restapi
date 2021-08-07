from django.db.models.query_utils import PathInfo
from rest_framework import serializers
from snippets.models import Article
from snippets.serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
a = Article(title='Article title',author='swati',email='asdf@gmail.com')
a.save()

serializer = ArticleSerializer(a)
print(serializer.data)

content = JSONRenderer().render(serializer.data)
print(content)

serializer = ArticleSerializer(Article.objects.all(),many=True)
print(serializer.data)

#############################################

serializers = ArticleSerializer()
print(repr(serializer))