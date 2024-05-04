from django.shortcuts import render
from .models import Notes
from django.http import Http404

# Create your views here.
def noteList(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes-list.html', {'notes': all_notes})

def noteDetail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'notes/note-detail.html', {'note': note})

