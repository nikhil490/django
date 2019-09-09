from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [

    # path('create/', views.post_new, name='create'),
    path('<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('<int:pk>/detail/', views.article_detail, name="detail"),
    path('<slug:types>/each/', views.article_each, name="each"),
    path('create/', views.post_new, name="create"),
    path('<int:pk>/update/', views.PostUpdateView, name='update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
]