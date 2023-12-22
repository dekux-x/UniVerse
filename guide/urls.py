from django.urls import path

from . import views

app_name = "guide"

urlpatterns = [
    path("", views.index, name = "index"),
    path("set_grants/", views.set_grants, name='set_grants'),
    path("sign-up/", views.sign_up, name="sign_up"),
    path("grant_chance/", views.grant_chance, name = 'grant_chance'),
    path("<int:univ_id>/detail/", views.detail, name = 'detail'),
    path("<int:faculty_id>/faculty_detail/", views.faculty_detail, name = 'faculty_detail'),
    path("<int:program_id>/program_detail/", views.program_detail, name = 'program_detail'),
    path("<int:id>/add_fav/", views.add_favorit, name="add_favorite"),
    path("fav_univ/", views.fav_univ_index, name="fav_univ_index"),
    path("fav_prog/", views.fav_prog_index, name="fav_prog_index"),
    path("compare/", views.compare, name="compare"),
]

