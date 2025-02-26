"""learning_logsのURLパターンの定義"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # ホームページ
    path('', views.index, name='index'),
    # 全てのトピックを表示するページ
    path('topics/', views.topics, name='topics'),
    # 個別トピックの詳細ページ
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 新しいトピックを追加するページ
    path('new_topic/', views.new_topic, name='new_topic'),
    # 新しいエントリを追加するページ
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # エントリを編集するページ
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
