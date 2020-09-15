from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    RecordingViewSet,
    EventViewSet,
    SubscriptionViewSet,
    CourseViewSet,
    GroupViewSet,
    ModuleViewSet,
    PaymentMethodViewSet,
    SubscriptionTypeViewSet,
    EnrollmentViewSet,
    LessonViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register("module", ModuleViewSet)
router.register("category", CategoryViewSet)
router.register("subscription", SubscriptionViewSet)
router.register("recording", RecordingViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("enrollment", EnrollmentViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)
router.register("lesson", LessonViewSet)
router.register("course", CourseViewSet)
router.register("event", EventViewSet)
router.register("group", GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
