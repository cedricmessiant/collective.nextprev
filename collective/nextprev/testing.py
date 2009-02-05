from Products.PloneTestCase import ptc

from collective.testcaselayer import ptc as tcl_ptc

ptc.setupPloneSite()

class Layer(tcl_ptc.BasePTCLayer):
    """Install collective.formcriteria"""

    def afterSetUp(self):
        self.loginAsPortalOwner()

        self.portal.portal_workflow.doActionFor(
            self.folder, 'publish')

        self.folder.invokeFactory(
            type_name='Topic', id='foo-topic-title',
            title='Foo Topic Title')
        topic = self.folder['foo-topic-title']
        topic.addCriterion('Type', 'ATPortalTypeCriterion'
                           ).setValue('News Item')
        topic.addCriterion('review_state', 'ATSimpleStringCriterion'
                           ).setValue('published')
        topic.setSortCriterion('effective', True)
        self.portal.portal_workflow.doActionFor(topic, 'publish')

        self.login()

        self.folder.setNextPreviousEnabled(True)

        self.folder.invokeFactory(
            type_name='News Item', id='foo-news-item-title',
            title='Foo News Item Title')
        self.folder.invokeFactory(
            type_name='News Item', id='bar-news-item-title',
            title='Bar News Item Title')
        self.folder.invokeFactory(
            type_name='News Item', id='baz-news-item-title',
            title='Baz News Item Title')

        self.loginAsPortalOwner()

        self.portal.portal_workflow.doActionFor(
            self.folder['foo-news-item-title'], 'publish')
        self.portal.portal_workflow.doActionFor(
            self.folder['baz-news-item-title'], 'publish')

        self.logout()

layer = Layer([tcl_ptc.ptc_layer])
