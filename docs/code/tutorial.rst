Introduction to Predix Services
===============================

These files use and test Predix functionalities such as creating OAuth2 clients
and users `[1]`_, streaming timeseries data `[2]`_, adding an analytic `[3]`_,
using pre-made analytics `[4]`_, and using the Predix analytics API.

Script Description Table
------------------------

====================  ===========
Script                Description
====================  ===========
00-helloworld.py_     Clone helloworld_ app and push to cloud using ``predix.app_name`` as domain for application.
01-setup_uaa.py_      Test logging in as application users varying in
                      authentication privileges.
04-timeseries.py_     Explore timeseries_ API. Test ingestion of a message,
                      which is timeseries data and uses websockets_ for
                      streaming, then query for outliers.
05-analytics.py_      Get ``SampleInputData`` artifact from an analytic and
                      send an execution POST request to analytic API.
make_plots.py_        Creates graphs of test data from Josh Edwards. The graphs
                      are used to help understand what kind of analysis should
                      be performed.
comparison.ipynb_     Execute `Short-Time Fourier Transform`_ analytic and
                      compare Predix analysis to similar analysis using
                      ``scipy.signal`` analysis.
run_analytics.ipynb_  Notebook to run Predix analytics on Caterpillar sample
                      data. `ARMA Time Series`_ is used on one year (364 days)
                      worth of Hauler data.
====================  ===========

These scripts all depend on the functions in the ``tutorial/predix`` package,
for complete documentation on all these functions and members go to
:ref:`predix-module-documentation`.

.. _[1]: https://www.predix.io/resources/tutorials/journey.html#1613
.. _[2]: https://www.predix.io/resources/tutorials/journey.html#1612
.. _[3]: https://www.predix.io/resources/tutorials/journey.html#1615
.. _[4]: https://www.predix.io/docs/#hcwYlgq4

.. _00-helloworld.py: https://github.com/maneyko/predix/blob/master/tutorial/00-helloworld.py
.. _01-setup_uaa.py: https://github.com/maneyko/predix/blob/master/tutorial/01-setup_uaa.py
.. _04-timeseries.py: https://github.com/maneyko/predix/blob/master/tutorial/04-timeseries.py
.. _05-analytics.py: https://github.com/maneyko/predix/blob/master/tutorial/05-analytics.py
.. _make_plots.py: https://github.com/maneyko/predix/blob/master/tutorial/make_plots.py
.. _comparison.ipynb: https://github.com/maneyko/predix/blob/master/tutorial/comparison.ipynb
.. _run_analytics.ipynb: https://github.com/maneyko/predix/blob/master/tutorial/run_analytics.ipynb

.. _helloworld: https://github.com/PredixDev/predix-nodejs-starter
.. _timeseries: https://www.predix.io/resources/tutorials/tutorial-details.html?tutorial_id=1556&tag=1605&journey=Build%20a%20basic%20application&resources=1580,1569,1523,1544,1547,1549,1556,1553,1570
.. _websockets: https://en.wikipedia.org/wiki/WebSocket
.. _Short-Time Fourier Transform: https://www.predix.io/analytics/analytic.html?id=2095
.. _ARMA Time Series: https://www.predix.io/analytics/analytic.html?id=2067

.. _Predix Module API Documentation: http://pterodactyl.datainnovationlab.tech/code/index.html#predix-module-api-documentation


.. vim: nowrap
