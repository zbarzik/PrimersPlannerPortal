import primer_algo_params

TEMPLATE_PAGE = """
{header}
{form}
{footer}
"""

TEMPLATE_HEADER = """
<h1>Welcome to Primer Planner Portal (temporary name)</h1>
<h2>Instructions:</h2>
do stuff and such
<hr>
"""

TEMPLATE_FOOTER = """
<hr>
here be text and links and other things
"""

TEMPLATE_FORM = """
<form name="primer_form" method="POST">
    {fields}
    <input type="submit" value="Submit">
</form>
"""

TEMPLATE_FIELD = """
<span style="display:inline-block; width: 300;">{fieldName}:</span><span style="display:inline-block; width: 500;">{fieldCode}</span><br/>
"""

def generateFields(paramObj):
    f = paramObj.makeWtfForm()
    fieldsStr = unicode("")
    for field in f:
        fieldsStr += unicode(TEMPLATE_FIELD.format(fieldName=field.label.text, fieldCode=str(field)))
    return fieldsStr

def generateForm(paramObj):
    return TEMPLATE_FORM.format(fields=generateFields(paramObj))

def generateHeader():
    return TEMPLATE_HEADER #placeholder

def generateFooter():
    return TEMPLATE_FOOTER #placeholder

def generatePage():
    paramObj = primer_algo_params.PrimerAlgoParams()
    return TEMPLATE_PAGE.format(header=generateHeader(),
                                form=generateForm(paramObj),
                                footer=generateFooter())

def validateForm(form):
    paramObj = primer_algo_params.PrimerAlgoParams()
    wtfForm = paramObj.makeWtfForm()
    for key, val in form.iteritems():
        wtfForm[key].data = val
        if not wtfForm[key].validate(wtfForm):
            print "Couldn't validate {key} with {value}".format(key=key,
                                                                value=val)
            return False
        else:
            print "Validated {key} with {value}".format(key=key,value=val)
    return True
        

if __name__ == "__main__":
    print generatePage()
