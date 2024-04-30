====================
django-puppeteer-pdf
====================


Converts HTML to PDF
--------------------

Provides Django views to wrap the HTML to PDF conversion using `puppeteer <https://github.com/GoogleChrome/puppeteer>`_.

Forked from: `django-puppeteer-pdf:v0.1.4 <https://pypi.org/project/django-puppeteer-pdf/0.1.4/>`_.

Requirements
------------

cli for puppeteer `puppeteer-pdf <https://github.com/octavenz/puppeteer-pdf>`_.

Python 3.10+ are supported.
See Github Actions build status for details


Note
------------

* Documentation is not up to date but you can see working use cases in `examples` directory
* Reporting bugs and issues is welcomed

Installation
------------

Run ``pip install git+https://github.com/octavenz/django-puppeteer-pdf.git``.

By default it will execute the first ``puppeteer-pdf`` command found on your ``PATH``.

It is recommended to specify full path of puppeteer-pdf using one of the way mentioned below.

If you can't add puppeteer-pdf to your ``PATH``, you can set ``PUPPETEER_PDF_CMD`` to a
specific executable:

e.g. in ``settings.py``: ::

    PUPPETEER_PDF_CMD = '/path/to/my/puppeteer-pdf'

or alternatively as env variable: ::

    export PUPPETEER_PDF_CMD=/path/to/my/puppeteer-pdf

You may also set ``PUPPETEER_PDF_CMD_OPTIONS`` in ``settings.py`` to a dictionary
of default command-line options.

The default is: ::

    PUPPETEER_PDF_CMD_OPTIONS = {
        'format': 'A4',
    }


License
-------

MIT License (BSD-2-Clause). See the bundled `LICENSE <https://github.com/octavenz/django-puppeteer-pdf/blob/master/LICENSE>`_ file for more details.

Credits
-------

This package is a fork of `pypi/django-puppeteer-pdf`_ created by Namespace merged on top of
repository created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template with modifications by Octave.

.. _`pypi/django-puppeteer-pdf`: https://pypi.org/project/django-puppeteer-pdf/0.1.4/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
