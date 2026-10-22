from django import forms

from .models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            "away_team",
            "home_team",
            "date",
            "time",
            "tv_channel",
            "notes",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        away_team = cleaned_data.get("away_team")
        home_team = cleaned_data.get("home_team")

        if away_team and home_team:
            if away_team.casefold() == home_team.casefold():
                raise forms.ValidationError(
                    "The home and away teams must be different."
                )

        return cleaned_data
