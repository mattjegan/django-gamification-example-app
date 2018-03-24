from django.urls import path

from app.views import MainView, AwardBadgeView, RevokeBadgeView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('award-badge/<int:badge_id>/', AwardBadgeView.as_view(), name='award-badge'),
    path('revoke-badge/<int:badge_id>/', RevokeBadgeView.as_view(), name='revoke-badge')
]
