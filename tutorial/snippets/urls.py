from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # path('article',views.article_list,name="article"),
    # path('detail/<int:pk>',views.article_detail,name="detail")

    path('article/',views.ArticleList.as_view()),
    path('detail/<int:pk>',views.ArticleDetail.as_view()),
    path('mixinlist',views.MixinArticleList.as_view()),
    path('mixindetail/<int:pk>',views.MixinArticleDetail.as_view()),
    path('genericlist',views.GenericArticleList.as_view()),
    path('genericdetail/<int:pk>',views.GenericArticleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)