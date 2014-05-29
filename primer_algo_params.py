from wtforms import Form, DecimalField, StringField, validators

class Param(object):
    def __init__(self, name = "", defaultValue = "", inputType = "numeric", minVal = 0, maxVal = 100):
        self.name = name
        self.defaultValue = defaultValue
        self.inputType = inputType
        self.minVal = minVal
        self.maxVal = maxVal
        
    def makeWtfField(self):
        retVal = None
        if self.inputType == "numeric":            
            retVal = DecimalField(self.name, [validators.NumberRange(min=self.minVal, max=self.maxVal)], default=self.defaultValue)
        elif self.inputType == "stringArray":
            csv = self.defaultValue[0]
            for val in self.defaultValue[1:]:
                csv += ", " + val
            retVal = StringField(self.name, default=csv)
        elif self.inputType == "string":
            retVal = StringField(self.name, default=self.defaultValue)
        else:
            raise ValueError("Illegal inputType")
        return retVal

    def getCamelCaseName(self):       
        tmpStr = ''.join(c.capitalize() or ' ' for c in self.name.split(' '))
        return tmpStr[0].lower() + tmpStr[1:]

class PrimerAlgoParams(object):
    def __init__(self):        
        self.PARAMS = [
            # Bacteria
            Param('min Prod Length', 140),
            Param('max Prod Length', 270),
            Param('min Bac Num', 100e3),

            # Single primer params
            Param('max GC content', 70),
            Param('min GC clamp', 1),
            Param('max GC clamp', 4),
            Param('min Primer Len', 18),
            Param('max Primer Len', 22),
            Param('min Tm', 56),
            Param('max Tm', 62),
            Param('max repeat', 4),
            Param('max run', 4),
            Param('primer conc', 50e-9),
            Param('salt conc', 0.05),

            # Self/Cross dimers
            Param('min Match', 4), 
            Param('dBases', 4),
            Param('temp Delta G', 37),
            Param('min Dimer Delta G', -11),
            Param('min Adaptor Delta G', -15.5),

            # Pair/Chain design params
            Param('delta Tm', 3),
            Param('max Overlap', 0),

            # Adaptors
            Param('adaptors', ['TACACGACGCTCTTCCGATCT', 'AGACGTGTGCTCTTCCGATCT'], inputType="stringArray"),

            # Other product
            Param('hg match file', 'hg_matches', inputType="string"),
            Param('mm match file', 'mm_matches', inputType="string"),

            # Design directories and names
            Param('dir', '/data2/fefuks/COMPASS/PrimersDesign/gg_201305_primers_multLen', inputType="string"),
            Param('design name', 'FirstDesign', inputType="string"),
            Param('primer list name', 'gg_multLen_primers', inputType="string"),
            ]

    def makeWtfForm(self):
        class F(Form):
            pass
        for param in self.PARAMS:
            setattr(F, param.getCamelCaseName(), param.makeWtfField())
        form = F()
        return form


if __name__ == "__main__":
    myParams = PrimerAlgoParams()
    myForm = myParams.makeWtfForm()
    for field in myForm:
        print field.label.text + ": " + str(field)
    
