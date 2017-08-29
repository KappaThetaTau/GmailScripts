..
  This file is written in reStructuredText, here is a quick reference:
  http://docutils.sourceforge.net/docs/user/rst/quickref.html

.. _introduction:

===============
Getting Started
===============
* Install `Python 3`_
* Install requirements

macOS
-----
.. code:: bash

    # Python 3

    brew install python3

    # Requirements

    python  -m pip install -r requirements.txt

    or 

    python3 -m pip install -r requirements.txt

Debian-based Linux
------------------
.. code:: bash

    # Python 3

    sudo add-apt-repository ppa:jonathonf/python-3.6
    sudo apt-get update
    sudo apt-get install python3.6
    sudo apt-get install python3-dev
    sudo apt-get install python-dev

    # Requirements

    sudo python    -m pip install -r requirements.txt
    sudo python3   -m pip install -r requirements.txt
    sudo python3.6 -m pip install -r requirements.txt


.. _Python 3: https://www.python.org/downloads/
