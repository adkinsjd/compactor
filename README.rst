compactor
=========
.. image:: https://travis-ci.org/adkinsjd/compactor.svg?branch=master
    :target: https://travis-ci.org/adkinsjd/compactor

compactor is a pure python implementation of libprocess, the actor library
underpinning `mesos <https://mesos.apache.org>`_.


documentation
=============

compactor documentation is available at `readthedocs <https://compactor.readthedocs.org>`_.
an example framework built using compactor is `pesos <https://github.com/wickman/pesos>`_,
a pure python implementation of the mesos framework api.

Additional Documentation
========================

This version of compactor adds two environment variable options:

LIBPROCESS_ADVERTISE_IP and
LIBPROCESS_ADVERTISE_PORT

These are the ip/port pair sent to the external host in the "from" part of
the libprocess message. This is good for when you have routed a public ip/port
to your machine, but you cannot directly bind to that public ip/port.
