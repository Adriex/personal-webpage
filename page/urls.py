from django.conf.urls import url
import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^portfolio/$", views.portfolio, name='portfolio'),
    url(r"^gallery/$", views.gallery, name='gallery'),
    url(r"^search/$", views.searcher, name='entries'),
    url(r"^contact/$", views.contact, name='contact'),
    url(r"^googled7cdce528f07c7ad.html/$", views.indexation, name='inx'),
    url(r'^post/(?P<id_entry>[0-9]+)$', views.seeEntry , name='seeEntry')
]
