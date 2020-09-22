from django.shortcuts import render, reverse, HttpResponseRedirect
from file_app.models import File
from file_app.forms import FileForm

def file_view(request):
    return render(request, 'index.html', {'files': File.objects.all()})

def form_view(request):
    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                name = data.get('name'),
                parent = data.get('parent'),
                isFile = data.get('isFile')
            )
            return HttpResponseRedirect(reverse('home'))
    form = FileForm()
    return render(request, 'form.html', {'form': form})    
