from django.shortcuts import render, redirect
from .models import MediaFile
from .forms import MediaFileForm

def home(request):
    media = MediaFile.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/home.html', {'media': media})

def upload_media(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MediaFileForm()
    return render(request, 'gallery/upload.html', {'form': form})
