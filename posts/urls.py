from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(template_name = "post_list.html"), name='all'),
    path('new/', CreatePost.as_view(template_name = "post_form.html"), name='create'),
    path('by/<slug:username>/', UserPosts.as_view(template_name = "user_post_list.html"), name='for_user'),
    path('by/<slug:username>/<int:pk>', PostDetail.as_view(template_name = "post_detail.html"), name='single'),
    path('delete/<int:pk>', DeletePost.as_view(template_name = "post_confirm_delete.html"), name='delete'),

]