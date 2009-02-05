.. -*-doctest-*-

===================
collective.nextprev
===================

The collective.nextprev package extends Plone's next/previous
navigation for folders to collections (AKA topics or smart folders).
If a listing view is visited for a collection which has next/previous
navigation enabled, a cookie is set to remember the collection used
and any relevant query terms.  When a content item in the result set
is visited, this cookie will be used to determine the next and
previous item links.

Start with the default news folder, some news items, and the default
collection.

    >>> folder
    <ATFolder at /plone/Members/test_user_1_>
    >>> folder.contentValues()
    [<ATTopic at /plone/Members/test_user_1_/foo-topic-title>,
     <ATNewsItem at /plone/Members/test_user_1_/foo-news-item-title>,
     <ATNewsItem at /plone/Members/test_user_1_/bar-news-item-title>,
     <ATNewsItem at /plone/Members/test_user_1_/baz-news-item-title>]

One news item is not published and so doesn't show up in the
collection listing.

    >>> portal.portal_workflow.getInfoFor(
    ...     folder['bar-news-item-title'], 'review_state')
    'private'
    >>> folder['foo-topic-title'].queryCatalog(full_objects=True)
    [<ATNewsItem at /plone/Members/test_user_1_/foo-news-item-title>,
     <ATNewsItem at /plone/Members/test_user_1_/baz-news-item-title>]

Next/previous navigation is enabled for the folder.

    >>> folder.getNextPreviousEnabled()
    True

Open a browser at the news folder.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> browser.handleErrors = False
    >>> browser.open(folder.absolute_url())
