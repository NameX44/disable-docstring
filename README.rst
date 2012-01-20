==================
Disable Docstrings
==================

This is a Nose_ plugin that tells unittest not to use test docstrings as
test names. Instead it uses the name of the test itself.

Install::

  pip install disabledoc

Usage::

  nosetests -v --disable-docstring

===================
Enable PyDocStrings
===================

This is a Nose_ plugin that tells unittest not to truncate doc strings
to one line on failure.  Instead a whole doc string accross mutliple
lines will be output on failure.

Usage::

  nosetests --enable-pydocstring

.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
