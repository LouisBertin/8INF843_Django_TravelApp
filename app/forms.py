from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput

from .models import Preference, Post


class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = ('cigarette', 'animal', 'discussion', 'big_suitcase')


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'passengers_nb', 'departure', 'arrival', 'departure_date')
        widgets = {
            'departure_date': DateTimePickerInput(
                options={
                    "sideBySide": True,
                }
            ),
        }