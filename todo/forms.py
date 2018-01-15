from django import forms


class ToDoForm(forms.Form):
    text = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter TO-DO Item here... e.g. Remind Aniket to practice DJango',
            'aria-label': 'ToDo Item Text',
            'aria-describedby': 'basic-addon2',
        }
    ))
