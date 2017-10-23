from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static
from webtoursite import views


urlpatterns = [
	urlpatterns = [
	url(r'^webtoursite/', include('webtoursite.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^conta/', include('accounts.urls', namespace='accounts'))
]
]