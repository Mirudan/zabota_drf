from django.urls import path

from vaccine_and_treatment_app.views import TreatmentList, TreatmentCreate, TreatmentUpdate, TreatmentDelete, \
    VaccineRabiesList, VaccineRabiesCreate, VaccineRabiesDelete, VaccineRabiesUpdate

urlpatterns = [
    path('', TreatmentList.as_view(), name='список обработок'),
    path('create/', TreatmentCreate.as_view(), name='создание записи об обработке'),
    path('<int:pk>/update/', TreatmentUpdate.as_view(), name='обновление записи об обработке'),
    path('<int:pk>/delete/', TreatmentDelete.as_view(), name='удаление записи об обработке'),
    path('vaccine/', VaccineRabiesList.as_view(), name='список вакцин от бешенства'),
    path('vaccine/create/', VaccineRabiesCreate.as_view(), name='создание записи о вакцинации от бешенства'),
    path('vaccine/<int:pk>/update/', VaccineRabiesUpdate.as_view(), name='обновление записи о вакцине от бешенства'),
    path('vaccine/<int:pk>/delete/', VaccineRabiesDelete.as_view(), name='удаление записи о вакцине от бешенства')

]
