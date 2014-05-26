from wtforms import Form, DecimalField, validators

class AlgorithmInputForm(Form):
    # bacteria
    minProdLen = DecimalField('minProdLen',[validators.NumberRange(min=100, max=200)], default=140)
    maxProdLen = DecimalField('maxProdLen', [validators.NumberRange(min=100, max=200)])
    minBacNum = DecimalField('minBacNum', [validators.NumberRange(min=500, max=2000)])

    # single primer params
    max_GC_content = DecimalField('max_GC_content', [validators.NumberRange(min=100, max=200)])
    min_GC_clamp = DecimalField('min_GC_clamp', [validators.NumberRange(min=100, max=200)])
    max_GC_clamp = DecimalField('max_GC_clamp', [validators.NumberRange(min=100, max=200)])
    minPrimerLen = DecimalField('minPrimerLen', [validators.NumberRange(min=100, max=200)])
    maxPrimerLen = DecimalField('maxPrimerLen', [validators.NumberRange(min=100, max=200)])
    minTm = DecimalField('minTm', [validators.NumberRange(min=100, max=200)])
    maxTm = DecimalField('maxTm', [validators.NumberRange(min=100, max=200)])
    max_repeat = DecimalField('max_repeat', [validators.NumberRange(min=100, max=200)])
    max_run = DecimalField('max_run', [validators.NumberRange(min=100, max=200)])
    primer_conc = DecimalField('primer_conc', [validators.NumberRange(min=100, max=200)])
    salt_conc = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])

    # self/cross dimers
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])
    minProdLen = DecimalField('minProdLen', [validators.NumberRange(min=100, max=200)])



    def render(self):
        response = ""
        for field in self:
            response += str(field)
        return response

def render_form():
    form = AlgorithmInputForm()
    return form
