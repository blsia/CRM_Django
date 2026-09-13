from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Register(UserCreationForm):
    email = forms.EmailField(
        label="", 
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2.5 text-sm text-slate-900 rounded-md bg-white border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600 dark:bg-neutral-700 dark:border-neutral-600 dark:text-slate-50', 
            'placeholder': 'Email Address'
        })
    )
    first_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2.5 text-sm text-slate-900 rounded-md bg-white border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600 dark:bg-neutral-700 dark:border-neutral-600 dark:text-slate-50', 
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2.5 text-sm text-slate-900 rounded-md bg-white border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600 dark:bg-neutral-700 dark:border-neutral-600 dark:text-slate-50', 
            'placeholder': 'Last Name'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)

        input_tailwind_class = 'w-full px-3 py-2.5 text-sm text-slate-900 rounded-md bg-white border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600 dark:bg-neutral-700 dark:border-neutral-600 dark:text-slate-50'

        # Username Field
        self.fields['username'].widget.attrs['class'] = input_tailwind_class
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="text-xs text-slate-500 dark:text-neutral-400">Maksimal 150 karakter. Hanya huruf, angka, dan karakter @/./+/-/_.</span>'

        # Password 1 Field
        self.fields['password1'].widget.attrs['class'] = input_tailwind_class
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="text-xs text-slate-500 dark:text-neutral-400 list-disc list-inside space-y-1 mt-1"><li>Password tidak boleh mirip dengan informasi pribadi.</li><li>Minimal 8 karakter.</li><li>Tidak boleh password yang terlalu umum.</li></ul>'

        # Password 2 Field
        self.fields['password2'].widget.attrs['class'] = input_tailwind_class
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="text-xs text-slate-500 dark:text-neutral-400">Masukkan password yang sama untuk konfirmasi.</span>'