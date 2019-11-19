from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
	class Meta:
		model=Article 
		fields=['Title','Author','published_date','description']