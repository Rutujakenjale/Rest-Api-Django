from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from blogapp import views


urlpatterns = [
   
    # url(r'^$', 'blogapp.views.home', name='home'),
    url(r'^admin/', admin.site.urls),
    url('', include('blogapp.urls')),
    # (?# url(r'^articles/',views.ArticleList.as_view()),)


]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)