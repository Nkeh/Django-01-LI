from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NoteForm

# Create your views here.
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()



class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    form_class = NoteForm
    success_url = '/notes'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    form_class = NoteForm
    success_url = '/notes'

    
class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/notes'
    template_name = "notes/notes_delete.html"




# def noteDetail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/note-detail.html', {'note': note})

