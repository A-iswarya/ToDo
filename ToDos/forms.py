from django import forms

#input form to add new todos
class ToDoForm(forms.Form):
    text = forms.CharField(max_length = 45,
                           widget = forms.TextInput(
                                                attrs = {'class' : 'form-control',
                                                        'placeholder' : 'Enter ToDo',
                                                        'aria-label' : 'ToDo',
                                                        'aria-describeby' : 'add-btn'}
                ));
