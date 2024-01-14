from django import forms

from app_blog.models import Blogpost


class StyleFormMiXin(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_published':
                field.widget.attrs['class'] = 'form-control'


class BlogpostForm(StyleFormMiXin, forms.ModelForm):
    class Meta:
        model = Blogpost
        # fields = '__all__'
        fields = ('title', 'content', 'preview', 'is_published',)
