from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from nps_django import views

router = routers.DefaultRouter()
router.register(r'passholders', views.PassholderViewSet)
router.register(r'passes', views.PassViewSet)
router.register(r'parks', views.ParkViewSet)
router.register(r'visits', views.VisitViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('registration/', views.registration, name='passholder_registration'),
    path('uservisits/<str:email>', views.UserVisitView.as_view()),
    path('userpass/<str:email>/<int:pass_id>', views.UserPassView.as_view())
]