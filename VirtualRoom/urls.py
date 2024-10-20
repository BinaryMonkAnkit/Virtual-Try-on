from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
# from . import views
# from VTR import views
# from api.views import CreateUserView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



# router = DefaultRouter()
# router.register(r'VTR_model', views.MyModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home, name='home'),
    # path('about/',views.about, name='about'),
    # path('contact/',views.contact, name='contact'),
    # path('VTR/',include('VTR.urls')),
    # path("__reload__/", include("django_browser_reload.urls")),
    # path('api/', include(router.urls)),
    # path('', TemplateView.as_view(template_name ='index.html')),    
    # path("api/user/register/", CreateUserView.as_view(), name="register"),
    # path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    # path("api-auth/", include("rest_framework.urls")),

    
    # path("api/", include("api.urls")),

    # path('api2/', include('api2.urls')),#For api2 

    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('VTR.urls'))

]
