import os

from nose.plugins import Plugin


class DisableDocstring(Plugin):
    """Tells unittest not to use docstrings as test names."""

    name = 'disable-docstring'

    def options(self, parser, env=os.environ):
        super(DisableDocstring, self).options(parser, env=env)
        parser.add_option('--disable-docstring', action="store_true",
                          help=DisableDocstring.__doc__)

    def configure(self, options, conf):
        super(DisableDocstring, self).configure(options, conf)
        if options.disable_docstring:
            self.enabled = True
        if not self.enabled:
            return

    def describeTest(self, test):
        return '(%s) %s' % (test, test.test._testMethodName)


class EnablePydocstring(Plugin):
    """Tells unittest to use the whole pydoc string of a unit
    test as output upon failure.
    """

    name = 'enable-pydocstring'

    def options(self, parser, env=os.environ):
        #class doc is done twice so help text is pretty
        parser.add_option('--enable-pydocstring', action="store_true",
                          help="Tells unittest to use the whole pydoc string"
                          " of a unit test as ouput upon test failure.")

    def configure(self, options, conf):
        super(EnablePydocstring, self).configure(options, conf)
        if options.enable_pydocstring:
            self.enabled = True
        if not self.enabled:
            return

    def describeTest(self, test):
        return '({test_name}) \n {test_doc}'.format(test_name=test,
                                                 test_doc=test.test._testMethodDoc)

