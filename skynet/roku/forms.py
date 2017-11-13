from wtforms import fields, Form, validators


class RokuKeypressForm(Form):
    """Form for Roku keypress."""
    key = fields.StringField(u'key')

    def validate(self):
        if not super(RokuKeypressForm, self).validate():
            return False
        if not self.key.data:
            return False
        return True


class RokuLaunchForm(Form):
    """Form for Roku launch."""
    app_id = fields.IntegerField(u'app_id')

    def validate(self):
        if not super(RokuLaunchForm, self).validate():
            return False
        if not self.app_id.data:
            return False
        return True
