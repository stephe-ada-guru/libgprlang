libgprlang
==========

Libgprlang is a project to provide a semantic engine for the AdaCore
gpr project definition language, using AdaCore's
[langkit](http://github.com/AdaCore/langkit). In particular, it
provides an indentation engine for use by Emacs gpr-mode.

Setup
-----

To generate and build the library and executables:

- Install the GNAT tools and compiler. You can find the GPL version of them on
  <http://libre.adacore.com>. Minimum version GPL 2016.

- Build and install the `gpl-2016` branch of
  the
  [GNATcoll library from GitHub](https://github.com/AdaCore/gnatcoll)
  (for license compatibility). libgprlang does not require the Python
  gnatcoll component.

- Install [Quex version 0.65.4](http://downloads.sourceforge.net/project/quex/DOWNLOAD/quex-0.65.4.tar.gz)
  Follow the installation guide in the Quex `README`

- Install the Python dependencies, using a virtualenv:

~~~
$ cd libgprlang
$ virtualenv env
$ source env/bin/activate
$ pip install -r REQUIREMENTS.dev
~~~

Build, Install
--------------

Generate Ada code for libgprlang:

    $ python gpr/manage.py generate

Build library and executables:

    $ python gpr/manage.py build

Subsequent builds:

    $ python gpr/manage.py make

Install:

    FIXME: $ python gpr/manage.py install ?
    FIXME: gprinstall?

Testing
-------

Run all tests:

    $ gpr/manage.py test

Run one test:

    $ gpr/manage.py test --testsuite-args gpr/testsuite/tests/parser/project_0

Documentation
-------------

The developer and user's documentation for Libgprlang is in `ada/doc`. You can
consult it as a text files or you can build it.  For instance, to generate HTML
documents, run from the top directory:

    $ make -C ada/doc html

And then open the following file in your favorite browser:

    ada/doc/_build/html/index.html
