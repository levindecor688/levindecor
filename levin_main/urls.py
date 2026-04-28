from django.conf.urls import url
from levin_main import views


urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^events/(?P<name_slug>.*)/$', views.events, name='events'),
    url(r'^products/(?P<name_slug>.*)/(?P<sheet_number>.*)/$', views.product_detail_single, name='product_detail_single'),
    url(r'^products/(?P<name_slug>.*)/$', views.product_detail, name='product_detail'),
    url(r'^products/$', views.products, name='products'),
    url(r'^privacy-policy/$', views.privacy_policy, name='privacy_policy'),

    url(r'^product_search/$', views.product_search, name='product_search'),

    # catalogue
    url(r'^catalogues/$', views.catalogues, name='catalogues'),
    url(r'^catalogue/1mm/$', views.catalogue_1mm, name='catalogue_1mm'),
    url(r'^catalogue/elite/$', views.catalogue_elite, name='catalogue_elite'),
    # url(r'^catalogue/lemore/$', views.catalogue_lemore, name='catalogue_lemore'),

    url(r'^error-found/$', views.error, name='error'),

]
