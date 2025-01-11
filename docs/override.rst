==================
Override resources
==================

You can override generating resources on any projects.

Spec of default implementation
==============================

#. Render ``<script>``, ``<link>`` and ``<template>`` elements.

   * Template is detected by ``goto_top_design`` of ``conf.py``.

#. ``<script>`` append navigation content into document body based from ``<template>``.
#. Browser display navigation disigned by css refered ``<link>``.

Contents guide
==============

Button content
--------------

It uses ``goto-top/navigation.html`` in directory on one of ``templates_path``.

If you override only it, it must include element that has attribute ``id="{{ goto_top.content_id }}"``.

Style of button
---------------

It uses ``goto-top/style.css`` in directory on one of ``html_static_path``.

Handler JavaScript
------------------

It uses ``goto-top/main.js`` in directory on one of ``html_static_path``.
