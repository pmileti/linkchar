from django.urls import path 
from apis import views 
 
urlpatterns = [ 
    path('keyword', views.keyword),
    path('category', views.category),
    path('ordered-list', views.ordered_list),
    path('item', views.item),
    path('populate-apis', views.populate_apis),


]