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

Start with the a folder, some content, and a collection.

    >>> folder
    <ATFolder at /plone/Members/test_user_1_>
    >>> folder.contentValues()
    [<ATTopic at /plone/Members/test_user_1_/foo-topic-title>,
     <ATNewsItem at /plone/Members/test_user_1_/foo-news-item-title>,
     <ATDocument at /plone/Members/test_user_1_/bar-page-title>,
     <ATNewsItem at /plone/Members/test_user_1_/baz-news-item-title>]

One item is a page and so doesn't show up in the collection listing.

    >>> folder['foo-topic-title'].queryCatalog(full_objects=True)
    [<ATNewsItem at /plone/Members/test_user_1_/foo-news-item-title>,
     <ATNewsItem at /plone/Members/test_user_1_/baz-news-item-title>]

Next/previous navigation is enabled for the folder.

    >>> folder.getNextPreviousEnabled()
    True

Open a browser at the folder.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> browser.handleErrors = False
    >>> browser.open(folder.absolute_url())

Visit one of the news items, the next link points to the next item in
the folder but not the next item in the collection.

    >>> browser.getLink('Foo News Item Title').click()
    >>> browser.getLink('Next')
    <Link text='Next: Bar Page Title Right arrow[IMG]'
    url='http://nohost/plone/Members/test_user_1_/bar-page-title'>
