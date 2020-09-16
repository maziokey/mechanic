
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from allauth.account.forms import LoginForm, SignupForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, Submit, Row, Column

class CustomUserCreationForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # Add magic stuff to redirect back.
        self.helper.layout.append(
            HTML(
                "{% if redirect_field_value %}"
                "<input type='hidden' name='{{ redirect_field_name }}'"
                " value='{{ redirect_field_value }}' />"
                "{% endif %}"
            )
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # Add magic stuff to redirect back.
        self.helper.layout.append(
            HTML(
                "{% if redirect_field_value %}"
                "<input type='hidden' name='{{ redirect_field_name }}'"
                " value='{{ redirect_field_value }}' />"
                "{% endif %}"
            )
        )

        # Add password reset link.
        self.helper.layout.append(
            HTML(
                "<p><a class='button secondaryAction' href={url}>{text}</a></p>".format(
                    url=reverse('account_signup'),
                    text=_('Forgot Password?')
                )
            )
        )
'''
        # Add submit button like in original form.
        self.helper.layout.append(
            HTML(
                '<button class="btn btn-primary btn-link btn-wd btn-lg" type="submit">'
                '%s</button>' % _('Log In')
            )
        )

        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'check_me_out',
            Submit('submit', 'Sign in')
        )

        #self.helper.form_class = 'form'
        #self.helper.label_class = 'col-xs-2 hide'
        #self.helper.field_class = 'col-xs-8'

<div class="input-group">
    <div class="input-group-prepend">
        <span class="input-group-text">
        <i class="material-icons">face</i>
        </span>
    </div>
    <input type="text" class="form-control" placeholder="First Name">
</div>



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2', )

'''