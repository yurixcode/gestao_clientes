from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete
from .views import PersonList
from .views import PersonDetailView
from .views import PersonCreateView
from .views import PersonUpdateView
from .views import PersonDeleteView


urlpatterns = [
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),
    path('person_list/', PersonList.as_view(), name='person_list_cbv'),
    path('person_list/<int:pk>/', PersonDetailView.as_view(), name='person_detail_cbv'),
    path('person_create/', PersonCreateView.as_view(), name='person_create_cbv'),
    path('person_update/<int:pk>/', PersonUpdateView.as_view(), name='person_update_cbv'),
    path('person_delete/<int:pk>/', PersonDeleteView.as_view(), name='person_delete_cbv'),

]