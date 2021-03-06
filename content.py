import primer_algo_params

TEMPLATE_PAGE = """
<!DOCTYPE html>
<html lang="en">
  <head>
      {styling}
  </head>
  <body>
    {header}
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
<span style="display:inline-block; width: 300; {fieldColor}">{fieldName}:</span>
{fieldNewline}<span style="display:inline-block; width: 500;">{fieldCode}{fieldError}</span><br/>
"""

TEMPLATE_ASTERIX = """
<span style="display:inline-block; width: 300; color: red; ">{errorNotice}</span>
"""

CSS_TEMPLATE = """
<style>
body {
    font-family: "Times New Roman";
    background-color: #d0e4fe;
    font-size: 14px;
    text-align: center;
}
h1 {
}
h2 {
}
span {
    text-align: left;
}
input[type=text] {padding:5px; border:2px solid #ccc; 
-webkit-border-radius: 5px;
border-radius: 5px;
}
input[type=text]:focus {border-color:#333; }

input[type=submit] {padding:5px 15px; background:#ccc; border:0 none;
cursor:pointer;
-webkit-border-radius: 5px;
border-radius: 5px; }
textarea {padding:5px; border:2px solid #ccc; 
-webkit-border-radius: 5px;
border-radius: 5px;
}
textarea:focus {border-color:#333; }
</style>
"""

BOOSTRAP_TEMPLATE = """
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
{style}
"""


def getNewlineSpacer(field):
    if "textarea" in str(field):
        return "<br/>"
    return ""

def generateFields(wtForm):
    fieldsStr = unicode("")
    for field in wtForm:
        fieldsStr += unicode(TEMPLATE_FIELD.format(fieldError=getError(field, wtForm),
                                                   fieldColor=getColor(field, wtForm),
                                                   fieldName=field.label.text,
                                                   fieldNewline=getNewlineSpacer(field),
                                                   fieldCode=str(field)))
    return fieldsStr

def generate_style():
    return BOOSTRAP_TEMPLATE.format(style=CSS_TEMPLATE)

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
    return TEMPLATE_PAGE.format(styling=generate_style(),
                                header=generateHeader(),
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
            return None
        else:
            print "Validated {key} with {value}".format(key=key,value=val)
    return wtForm
        

if __name__ == "__main__":
    print generatePage()
