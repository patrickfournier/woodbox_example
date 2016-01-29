===============
Woodbox Example
===============

This is an example application built with the Woodbox framework.

Adding data types
=================

In ``app/models``, create a new file named ``YOUR_TYPE_model.py`` (replace
YOUR_TYPE by the name of your new data type, in lower case) and
define your model.

Define an API for your data
===========================

In ``app/api_v1``, create a new file name ``YOUR_TYPE.py`` (again,
replace YOUR_TYPE by the name of your new data type, in lower case)
and create a class ``YourTypeSchema``, used to map database fields to
JSON API fields; only map what you want to expose through the API.

Expose the API
==============

In ``app/api_v1/__init__.py``, using
``woodbox.record_api.make_api()``, publish the API. You use
``make_api`` to bind your model, your schema, a list of API access
control functions and a record access control object.

That's it: you now have a REST API to create, read, update and delete
your new type, and your data will be persisted to a SQL database.
