from rest_framework import serializers
from .models import Article
# from rest_framework import Article
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Article
		fields=('Title','Author','published_date','description')



