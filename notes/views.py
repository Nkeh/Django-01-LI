from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Notes
from .forms import NoteForm

# Create your views here.
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"



class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"


class NotesCreateView(CreateView):
    model = Notes
    form_class = NoteForm
    success_url = '/notes'


class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NoteForm
    success_url = '/notes'

    




# def noteDetail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/note-detail.html', {'note': note})

