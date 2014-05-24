from wtforms import Form, StringField, validators

class AlgorithmInputForm(Form):
    temp1 = StringField('temp1', [validators.Length(min=4, max=25)])
    temp2 = StringField('temp2', [validators.Length(min=4, max=25)])
    def render(self):
        response = ""
        for field in self:
            response += str(field)
        return response

def render_form():
    form = AlgorithmInputForm()
    form['temp1'].data = 'foo'
    form['temp2'].data = 'bar'
    return form
