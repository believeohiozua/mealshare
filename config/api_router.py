from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from decameal.users.api.views.forgot_password import ForgetPasswordView
from decameal.users.api.views.login import LoginView
from decameal.users.api.views.meal import Meals
from decameal.users.api.views.meal_detail import MealDetail
from decameal.users.api.views.notification_view import NotificationView
from decameal.users.api.views.register import RegisterView
from decameal.users.api.views.register_kitchen_staff import RegisterKitchenStaffView
from decameal.users.api.views.register_staff import RegisterStaffView
from decameal.users.api.views.reset_password import SetNewPasswordView
from decameal.users.api.views.ticket import TicketView
from decameal.users.api.views.update_ticket import UpdateTicketView
from decameal.users.api.views.users import UserViewSet
from decameal.users.api.views.verify_otp import OTPVerifyView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/forgot-password/", ForgetPasswordView.as_view(), name="forgot"),
    path("auth/reset-password/", SetNewPasswordView.as_view(), name="reset"),
    path("auth/register/staff", RegisterStaffView.as_view(), name="register_staff"),
    path("auth/verify/", OTPVerifyView.as_view(), name="verify"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path(
        "auth/register/kitchenstaff",
        RegisterKitchenStaffView.as_view(),
        name="register-kitchen-staff",
    ),
    path("meals/<uuid:pk>/", MealDetail.as_view(), name="meals"),
    path("meals/", Meals.as_view(), name="meals"),
    path(
        "users/<int:pk>/notifications/",
        NotificationView.as_view(),
        name="notifications",
    ),
    path("tickets/", TicketView.as_view(), name="tickets"),
    path("tickets/<uuid:pk>/", UpdateTicketView.as_view(), name="update-ticket"),
]

app_name = "api"
urlpatterns += router.urls
