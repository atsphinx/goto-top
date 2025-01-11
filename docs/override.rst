==================
Override resources
==================

You can override generating resources on any projects.

Spec of default implementation
==============================

.. todo:: Write it

Contents guide
==============

Button content
--------------

It uses ``goto-top/navigation.html`` in directory on one of ``templates_path``.

If you override only it, it must include element that has attribute ``id="gotoTop"``.

Style of button
---------------

It uses ``goto-top/style.css`` in directory on one of ``html_static_path``.

Handler JavaScript
------------------

It uses ``goto-top/main.js`` in directory on one of ``html_static_path``.
