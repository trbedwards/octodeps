from django.conf.urls import include, url

from jobs import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    # url(r'^admin/', include(admin.site.urls)),
]
