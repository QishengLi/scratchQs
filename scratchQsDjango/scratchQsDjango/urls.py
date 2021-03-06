"""scratchQsDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from scratchQs import views
from scratchQs import views as scratchq_views
from django.contrib.auth import views as auth_views
from scratchQs.views import UserFormView, login_view


urlpatterns = [
    url(r'^scratchQs/admin/', admin.site.urls),
    #url(r'^scratchQs/$', scratchq_views.index, name="index"),
    url(r'^scratchQs/questions/', scratchq_views.IndexView.as_view(), name="index"),
    url(r'^scratchQs/filter/(?P<filter_by>.*)/$', scratchq_views.filter_results, name="filter_results"),
    url(r'^scratchQs/(?P<question_id>[0-9])/filter/(?P<filter_answer_by>.*)/$', scratchq_views.filter_answers, name="filter_answers"),

    url(r'^scratchQs/(?P<question_id>[0-9])/$', scratchq_views.answers, name="answers"),
    url(r'^scratchQs/community/(?P<community_id>[0-9]+)/$', scratchq_views.community_questions, name="community_questions"),
    url(r'^scratchQs/signup', scratchq_views.signup, name="signup"),
    url(r'^scratchQs/add_question', scratchq_views.add_question),
    #url(r'^scratchQs/answer/$', scratchq_views.answer_page, name="answer_page") #not working yet
    url(r'^upvote_question', scratchq_views.upvote_question, name="upvote_question"),
    url(r'^downvote_question', scratchq_views.downvote_question, name="downvote_question"),
    url(r'^upvote_answer', scratchq_views.upvote_answer, name="upvote_answer"),
    url(r'^downvote_answer', scratchq_views.downvote_answer, name="downvote_answer"),
    url(r'^scratchQs/add_answer/', scratchq_views.add_answer, name="add_answer"),
    url(r'^scratchQs/search/keyword=(?P<search_text>.*)/', scratchq_views.search_question, name="search_question"),
    url(r'^scratchQs/register/', UserFormView.as_view(), name='register'),
    url(r'^scratchQs/login/', login_view, name='login'),

    # url(r'^scratchQs/loginn/$', auth_views.login, name='login'), #still working
]
