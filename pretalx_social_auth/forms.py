from django.forms.models import inlineformset_factory
from i18nfield.forms import I18nModelForm
from pretalx.common.forms import I18nEventFormSet
from pretalx.event.models import Event

from .models import SocialAuthButton


class SocialAuthButtonForm(I18nModelForm):
    class Meta:
        model = SocialAuthButton
        fields = ("backend", "label", "order", "enabled")


SocialAuthButtonFormSet = inlineformset_factory(
    Event,
    SocialAuthButton,
    form=SocialAuthButtonForm,
    formset=I18nEventFormSet,
    fk_name="event",
    can_delete=True,
    extra=1,
)
