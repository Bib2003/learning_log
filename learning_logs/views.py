from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner = request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """show a single topic and all its entries"""
    topic = Topic.objects.get(id = topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    
    # Get the entries related to the topic.
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        #no data submitted; create a blank form
        form = TopicForm()

    else:
        # POST data submitted; process data.
        form = TopicForm(data = request.POST)
        if form.is_valid():
            new_topic = form.save(commit = False)   #Don't save to DB yet
            new_topic.owner = request.user    # Assign the current user as owner
            new_topic.save()  #Now save to DB
            form.save()
            return redirect('learning_logs:topics') 

    # display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """add a new entry for a particular topic"""
    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':
        # no data submitted: create a blank form
        form = EntryForm()

    else:
        # POST data submitted; process data
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)
        
    # display a blank or invalid form.
    context = {'topic':topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance = entry)

    else:
        # POST data submitted; process data
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

# delete an existing topic
@login_required
def delete_topic(request, topic_id):
    """Delete an existing topic."""
    topic = Topic.objects.get(id = topic_id)

    if request.method == 'POST':
        # Initial request; pre-fill form with the current topic.
        form = TopicForm(instance = topic)
        topic.delete()
        print("Deleting topic")
        # Redirect to the topics page after deletion.
        return redirect('learning_logs:topics')

    else:
        # POST data submitted; process data
        form = TopicForm(instance = topic, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/delete_topic.html', context)

    
# delete an existing entry
@login_required
def delete_entry(request, entry_id):
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    if request.method == 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance = entry)
        entry.delete()
        print("Deleting entry")
        return redirect('learning_logs:topic', topic_id = topic.id)

    else:
        # POST data submitted; process data
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/delete_entry.html', context)


    