from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """学習ノートのホームページ"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """全てのトピックを表示するページ"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """1つのトピックとそれに関連する全てのエントリを表示する"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """新しいトピックを追加する"""
    if request.method != 'POST':
        # データが提出されていないので空のフォームを作る
        form = TopicForm()
    else:
        # POSTデータを送信されたのでデータを処理する
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """特定のトピックに新しいエントリを追加する"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # データが提出されていないので空のフォームを作る
        form = EntryForm()
    else:
        # POSTデータを送信されたのでデータを処理する
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """既存のエントリを編集する"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # 初回リクエスト、現在のエントリをフォームに表示する
        form = EntryForm(instance=entry)
    else:
        # POSTデータを送信されたのでデータを処理する
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
