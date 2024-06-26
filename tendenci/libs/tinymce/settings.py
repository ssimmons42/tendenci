import os
from django.conf import settings
from tendenci.apps.theme.templatetags.static import static

DEFAULT_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG',
        {'theme': "simple", 'relative_urls': False})

USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)

USE_COMPRESSOR = getattr(settings, 'TINYMCE_COMPRESSOR', False)

USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER',
        'filebrowser' in settings.INSTALLED_APPS)

if 'staticfiles' in settings.INSTALLED_APPS or 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    JS_URL = static(getattr(settings, 'TINYMCE_JS_URL', 'tiny_mce/tiny_mce.js'))
else:
    JS_URL = getattr(settings, 'TINYMCE_JS_URL', '%sjs/tiny_mce/tiny_mce.js' % settings.MEDIA_URL)
    JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT', os.path.join(settings.MEDIA_ROOT, 'js/tiny_mce'))

JS_URL = f"{JS_URL}{settings.TINYMCE_DEFAULT_CONFIG['cache_suffix']}"
JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]
