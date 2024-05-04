from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Notes

# Create your views here.
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"



class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"



# def noteDetail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/note-detail.html', {'note': note})

