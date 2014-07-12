from wtforms import Form, DecimalField, StringField, TextAreaField, validators

class Param(object):
    def __init__(self, name = "", defaultValue = "", inputType = "numeric", minVal = -float('inf'), maxVal = float('inf'), regExp = None):
        self.name = name
        self.defaultValue = defaultValue
        self.inputType = inputType
        self.minVal = minVal
        self.maxVal = maxVal
        self.regExp = regExp
        
    def makeWtfField(self):
        retVal = None
        if self.inputType == "numeric":
            retVal = DecimalField(self.name, [validators.NumberRange(min=self.minVal, max=self.maxVal)], default=self.defaultValue)
        elif self.inputType == "stringArray":
            csv = self.defaultValue[0]
            for val in self.defaultValue[1:]:
                csv += ", " + val
            myValidators = []
            if self.regExp != None:
                myValidators = [validators.Regexp(regex=self.regExp), validators.Required()]
                print "managed to make validator"
            retVal = TextAreaField(self.name, myValidators, default=csv)
        elif self.inputType == "string":
            myValidators = []
            if self.regExp != None:
                myValidators = [validators.Regexp(regex=self.regExp), validators.Required()]
                print "managed to make validator"
            retVal = StringField(self.name, myValidators, default=self.defaultValue)
        else:
            raise ValueError("Illegal inputType")
        return retVal

    def getCamelCaseName(self):       
        tmpStr = ''.join(c.capitalize() or ' ' for c in self.name.split())
        return tmpStr[0].lower() + tmpStr[1:]

class PrimerAlgoParams(object):
    def __init__(self):
        print "defining PARAMS"
        self.PARAMS = [
            # Bacteria
            Param('Min product length', 140, minVal=10),
            Param('Max product length', 270, minVal=10),
            Param('Min number of sequences aplified by primer', 100e5, minVal = 0),

            # Single primer params
            Param('Max GC content', 70, maxVal=100, minVal=0),
            Param('Min GC clamp', 1, minVal=0, maxVal=5),
            Param('Max GC clamp', 4, minVal=0, maxVal=5),
            Param('Min primer length', 18, minVal=5, maxVal=100),
            Param('Max primer length', 22, minVal=5, maxVal=100),
            Param('Min primer temperature', 56, minVal=0, maxVal=100),
            Param('Max primer temperature', 62, minVal=0, maxVal=100),
            Param('Max repeat', 4, minVal=0),
            Param('Max poly run', 4, minVal=0),
            Param('Annealing oligo concentration [Mol]', 5e-8, minVal=0),
            Param('Salt concentration (monovalent) [Mol]', 0.05, minVal=0),

            # Self/Cross dimers
            Param('Min #NT match for dimer', 4, minVal=0), 
            Param('Min consecutive #NT match for dimer', 4, minVal=0),
            Param('Max dimer delta G [kcal/mol]', -11),
            Param('Min dimer delta G with adaptor [kcal/mol]', -15.5),

            # Pair/Chain design params
            Param('Delta Tm', 3, minVal=0),
            Param('Max pairs overlap', 0, minVal=0),

            # Adaptors
            Param('Adaptors', ['TACACGACGCTCTTCCGATCT', 'AGACGTGTGCTCTTCCGATCT'], inputType="stringArray", regExp="(^([atgcATGC]+((\n)?[\,]?(\s)?)*)+$)"),

            # Other product
            Param('hg match file', 'hg_matches', inputType="string"),
            Param('mm match file', 'mm_matches', inputType="string"),

            # Design directories and names
            Param('Dir', '/data2/fefuks/COMPASS/PrimersDesign/gg_201305_primers_multLen', inputType="string"),
            Param('Design name', 'FirstDesign', inputType="string"),
            Param('Primer list name', 'gg_multLen_primers', inputType="string"),
            ]

    def makeWtForm(self):
        class F(Form):
            pass
        print "Iterating over PARAMS"
        for param in self.PARAMS:
            #print param.name
            setattr(F, param.getCamelCaseName(), param.makeWtfField())
        print "Finished iterating"
        form = F()
        print "Generated form"
        return form


if __name__ == "__main__":
    myParams = PrimerAlgoParams()
    myForm = myParams.makeWtForm()
    for field in myForm:
        print field.label.text + ": " + str(field)
    
