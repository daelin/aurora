
# Uses the hostname for generated URLs from 'sites' table
# at the index defined with SITE_ID.
SITE_ID = 1

# Use other paths if you intend to run this without vagrant
MEDIA_ROOT = '/vagrant/aurora/media'
STATIC_ROOT = '/vagrant/aurora/static'

MEDIA_URL = '/media/'

# Use %%NEXT_URL%% pattern inside SSO_URI to replace it with
# the previously requested url to get redirected to it after
# a successfull SSO auth.
SSO_URI = '/temporary_uri/?param=%%NEXT_URL%%'

LECTURER_USERNAME = 'lecturer'
LECTURER_SECRET = 'lecturersecret'

SSO_SHARED_SECRET = 'ssosecret'