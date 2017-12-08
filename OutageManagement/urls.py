from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^outage/$', views.OutageListView.as_view(), name='outage'),
]

# # Add URLConf for librarian to renew a book.
# urlpatterns += [
#     url(r'^outage/(?P<pk>[-\w]+)/activate/$', views.renew_book_librarian, name='renew-book-librarian'),
# ]


# Add URLConf to create, update, and delete books
urlpatterns += [  
    url(r'^outage/create/$', views.OutageCreate.as_view(), name='outage_create'),
    url(r'^outage/(?P<pk>\d+)/update/$', views.OutageUpdate.as_view(), name='outage_update'),
    url(r'^outage/(?P<pk>\d+)/delete/$', views.OutageDelete.as_view(), name='outage_delete'),
]
