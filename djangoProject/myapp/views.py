from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm
from .models import ImageModel
# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'myapp/index.html'

    def get(self, request, *args, **kwargs):
        print("here")
        return super().get(request, *args, **kwargs)

class FileUpload(generic.FormView):
    template_name = 'myapp/file_upload_view.html'
    form_class = UploadForm
    success_url = reverse_lazy('myapp:upload')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        images = ImageModel.objects.all()
        return render(request, self.template_name, {'form':form, 'images':images})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # save the file
            # file = request.FILES["file"]
            form.save()
            # fs = FileSystemStorage()
            # filename = fs.save(file.name, file)
            return redirect(self.success_url)
        return render(request, self.template_name, {'form':form})