import random 

from django.views.generic import TemplateView, RedirectView
from django_gamification.models import Badge

from app.models import ExampleUser


class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)

        user_data = []
        for user in ExampleUser.objects.all():
            acquired_badges = user.interface.badge_set.filter(acquired=True, revoked=False)
            award_badge_ids = [b.id for b in user.interface.badge_set.filter(acquired=False)]
            revoke_badge_ids = [b.id for b in acquired_badges]

            user_data.append({
                'id': user.id,
                'badges': ', '.join([b.name for b in acquired_badges]),
                'points': user.interface.points,
                'random_award_badge_id': random.choice(award_badge_ids) if award_badge_ids else None,
                'random_revoke_badge_id': random.choice(revoke_badge_ids) if revoke_badge_ids else None
            })

        context['users'] = user_data

        return context


class AwardBadgeView(RedirectView):
    pattern_name = 'main'

    def get_redirect_url(self, *args, **kwargs):
        badge_id = kwargs.pop('badge_id')

        badge = Badge.objects.filter(id=badge_id).first()
        badge.award()
        badge.save()

        return super(AwardBadgeView, self).get_redirect_url(*args, **kwargs)


class RevokeBadgeView(RedirectView):
    pattern_name = 'main'

    def get_redirect_url(self, *args, **kwargs):
        badge_id = kwargs.pop('badge_id')

        badge = Badge.objects.filter(id=badge_id).first()
        badge.force_revoke()
        badge.acquired = False  # We don't actually want to revoke it entirely in this example
        badge.revoked = False
        badge.save()

        return super(RevokeBadgeView, self).get_redirect_url(*args, **kwargs)
