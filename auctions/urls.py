from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create",views.create,name="create"),
    path("<int:item_id>",views.item,name="item"),
    path("watchlist",views.watchlist,name="watchlist"),
    path("category",views.categories,name="categories"),
    path("category/<str:category>",views.category,name="category")
]
