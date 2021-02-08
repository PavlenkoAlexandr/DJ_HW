import os
from django.shortcuts import render
from django.conf import settings
from datetime import datetime


def file_list(request, date=None):

    template_name = 'index.html'
    files = os.listdir(settings.FILES_PATH)
    files = [
        {
            'name': file,
            'ctime': datetime.fromtimestamp(os.stat(os.path.join(settings.FILES_PATH, file)).st_ctime),
            'mtime': datetime.fromtimestamp(os.stat(os.path.join(settings.FILES_PATH, file)).st_mtime)
        } for file in files if datetime.fromtimestamp(os.stat(os.path.join(settings.FILES_PATH, file)).st_ctime) == date]

    context = {
        'files': files,
        'date': date  # Этот параметр необязательный
    }
    return render(request, template_name, context)


def file_content(request, name):
    with open(os.path.join(settings.FILES_PATH, name)) as f:
        content = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

