from django.urls import path, re_path # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("result", views.result, name="result"),
    # path('social_links', views.social_links),
]

# from django.urls import path, re_path
# from . import views
# urlpattern=[
#     re_path(r'^company$', views.companyApi),
#     re_path(r'^company/([0-9]+)$',views.companyApi)
# ]