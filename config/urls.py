from django.contrib import admin
from django.urls import path
from mainapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('yangiliklar/', YangiliklarView.as_view(), name='yangiliklar'),
    path('news1/<int:pk>/', News1View.as_view(), name='news1'),
    path('mehnat/', MehnatView.as_view(), name='mehnat'),
    path('qabul/', QabulView.as_view(), name='qabul'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>/", set_language, name="set-language"),
    # uz-latn, uz-cyrl, ru, en
]
