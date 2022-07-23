from django.contrib import admin
from django.urls import path
from drinks.views import drink_list,send_file,store_data,auth,logout_user
from drinks.views import UserUpload
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', drink_list,name="drinks"),
    path("drinks/<path:filename>",send_file),
    path("register",store_data),
    path("auth",auth),
    path("logout",logout_user,name="logout"),
    path("upload",UserUpload.button,name="image_upload")]


urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
