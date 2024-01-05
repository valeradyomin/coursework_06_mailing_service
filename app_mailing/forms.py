from django import forms

from app_mailing.models import MailingSrv, Mail


class StyleFormMiXin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active' and field_name != 'is_published':
                field.widget.attrs['class'] = 'form-control'


class MailingSrvForm(StyleFormMiXin, forms.ModelForm):
    class Meta:
        model = MailingSrv
        fields = ('recipients', 'start', 'finish', 'status', 'frequency',)


class MailForm(StyleFormMiXin, forms.ModelForm):
    class Meta:
        model = Mail
        fields = '__all__'

