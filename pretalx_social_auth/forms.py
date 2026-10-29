from django.forms.models import inlineformset_factory
from i18nfield.forms import I18nModelForm
from pretalx.common.forms import I18nEventFormSet
from pretalx.event.models import Event

from .models import SocialAuthButton


class SocialAuthButtonForm(I18nModelForm):
    def __init__(self, *args, **kwargs):
        # I18nEventFormSet passes the event through to every form, so accept it
        # here even though this form does not need it.
        kwargs.pop("event", None)
        super().__init__(*args, **kwargs)

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
