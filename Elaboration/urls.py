from django.conf.urls import patterns, url
import Elaboration.views
urlpatterns = patterns('',
    url(r'^autosave$', Elaboration.views.save_elaboration, name='save'),
    url(r'^submit$', Elaboration.views.submit_elaboration, name='submit'),
)

