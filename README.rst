Steno3D Parser: .stl
********************

.. image:: https://travis-ci.org/seequent/steno3d-stl.svg?branch=master
    :target: https://travis-ci.org/seequent/steno3d-stl

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: https://github.com/seequent/steno3d-stl/blob/master/LICENSE

.. image:: https://img.shields.io/badge/download-PyPI-yellow.svg
    :target: https://pypi.python.org/pypi/steno3d_stl

Welcome to the .stl file parser plugin for `Steno3D <https://www.steno3d.com>`_
by `Seequent <https://www.seequent.com>`_. This repository supplements the
`Steno3D Python client library <https://github.com/seequent/steno3dpy>`_.

To install this parser, simply

.. code::

    pip install steno3d_stl

On import, this parser plugs in to the `steno3d.parsers` module. It can be
used as follows:

.. code:: python

    import steno3d
    import steno3d_stl
    parser = steno3d.parsers.stl('yourfile.stl')
    (stl_project,) = parser.parse()

This parser supports binary and ASCII .stl files. Basic documentation for these
files can be found on
`Wikipedia <https://en.wikipedia.org/wiki/STL_(file_format)>`_.
This parser does not support any non-standard features such as color,
materials, or multiple solids in one file. Additionally, in ASCII files,
extra newlines are not allowed.

If you are interested in additional features you may
`submit an issue <https://github.com/seequent/steno3d-stl/issues>`_
or consider directly contributing to the
`github repository <https://github.com/seequent/steno3d-stl>`_. `Parser
guidelines <https://python.steno3d.com/en/latest/content/parsers.html>`_
are available online.

To learn more, about Steno3D, visit `steno3d.com <https://www.steno3d.com>`_, the
`Steno3D source repository <https://github.com/seequent/steno3dpy>`_, and our
`online documentation <https://steno3d.com/docs>`_.
