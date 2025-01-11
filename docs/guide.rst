==========
User guide
==========

Installation
============

You can install from PyPI.

.. code-block:: console
   :caption: Example for using pip

   pip install atsphinx-goto-top

Usage
=====

You can use only register into your ``conf.py``.

.. code-block::
   :caption: conf.py

   extensions = [
       ..., # Other your extensions
       "atsphinx.goto_top",
   ]

When document build, it append the button into bottom of page.

Configuration
=============

.. confval:: goto_top_template_id
   :type: string
   :default: ``"tmpl_gotoTop"``

   This value is used for id ``<template>`` element.

   You need not set it other than ID id conflicted.

.. confval:: goto_top_content_id
   :type: string
   :default: ``"gotoTop"``

   You need not set it other than ID id conflicted.

.. confval:: goto_top_side
   :type: string
   :default: ``"right"``

   This value is used as CSS property. You muse set ``"left"`` or ``"right"``
