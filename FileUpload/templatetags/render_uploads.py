import os
from django import template
from django.http import request
from Elaboration.models import Elaboration
from FileUpload.models import UploadFile
from django.template import RequestContext

register = template.Library()

@register.inclusion_tag('uploads.html', takes_context=True)
def render_uploads(context, elaboration):
    elaboration = Elaboration.objects.get(id=elaboration.id)
    files = []
    index = 0
    for upload_file in UploadFile.objects.filter(user=elaboration.user, elaboration__id=elaboration.id):
        index = index + 1
        figure = 'Fig. ' + str(index)
        print("Fig: ", figure)
        files.append([os.path.basename(upload_file.upload_file.name),
                      round((upload_file.upload_file.size/1048576),2),
                      upload_file.upload_file.url,
                      figure])
    context.update( {'files':files} )
    return context