from Products.PloneTestCase import ptc

from collective.testcaselayer import ptc as tcl_ptc

ptc.setupPloneSite()

class Layer(tcl_ptc.BasePTCLayer):
    """Install collective.formcriteria"""

    def afterSetUp(self):
        pass

layer = Layer([tcl_ptc.ptc_layer])
