from django.shortcuts import render

from .models import Topic


def index(request):
    """学習ノートのホームページ"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """全てのトピックを表示するページ"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """1つのトピックとそれに関連する全てのエントリを表示する"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
