from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'app1'
urlpatterns = [
    path("", views.MovieView.as_view(), name='home'),
    path("movie/<int:id>/", views.Single_Movie_View.as_view(), name='movie'),
    path("movie/add/", views.AddMovieView.as_view(), name='add-movie'),
    path("movie/update/<int:id>/", views.update, name="movie-update"),
    path("movie/delete/<int:id>/", views.del_movie, name="dele")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
