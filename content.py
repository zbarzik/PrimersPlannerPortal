import primer_algo_params

TEMPLATE_PAGE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <link href="/static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <link href="/static/bootstrap/css/bootstrap-responsive.min.css" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-latest.js"></script>
    <script src="/static/bootstrap/js/bootstrap.min.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {header}
  </head>
  <body>
    {form}
    {footer}
  </body>
</html>
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
<span style="display:inline-block; width: 300; {fieldColor}">{fieldName}:</span><span style="display:inline-block; width: 500;">{fieldCode}{fieldError}</span><br/>
"""

TEMPLATE_ASTERIX = """
<span style="display:inline-block; width: 300; color: red; ">{errorNotice}</span>
"""

def generateFields(wtForm):
    fieldsStr = unicode("")
    for field in wtForm:
        fieldsStr += unicode(TEMPLATE_FIELD.format(fieldError=getError(field, wtForm),
                                                   fieldColor=getColor(field, wtForm),
                                                   fieldName=field.label.text,
                                                   fieldCode=str(field)))
    return fieldsStr

def getColor(field, wtForm):
    if not field.validate(wtForm):
        return "color: red; "
    return ""

def getError(field, wtForm):
    if not field.validate(wtForm):
        return TEMPLATE_ASTERIX.format(errorNotice="*")
    return ""
    
def generateForm(wtForm):
    return TEMPLATE_FORM.format(fields=generateFields(wtForm))

def generateHeader():
    return TEMPLATE_HEADER #placeholder

def generateFooter():
    return TEMPLATE_FOOTER #placeholder

def generatePage(postForm):
    wtForm = None
    if postForm == None:
        paramObj = primer_algo_params.PrimerAlgoParams()
        print "Generated primerObj"
        wtForm = paramObj.makeWtForm()
        print "Generated wtForm"
    else:
        wtForm = populateForm(postForm)
        print "populated wtForm"
    return TEMPLATE_PAGE.format(header=generateHeader(),
                                form=generateForm(wtForm),
                                footer=generateFooter())

def populateForm(postForm):
    paramObj = primer_algo_params.PrimerAlgoParams()
    wtForm = paramObj.makeWtForm()
    wtForm.process(postForm)
    return wtForm

def validateForm(postForm):
    wtForm = populateForm(postForm)
    for key, val in postForm.iteritems():
        if not wtForm[key].validate(wtForm):
            print "Couldn't validate {key} with {value}".format(key=key,
                                                                value=val)
            return False
        else:
            print "Validated {key} with {value}".format(key=key,value=val)
    return True
        

if __name__ == "__main__":
    print generatePage()
