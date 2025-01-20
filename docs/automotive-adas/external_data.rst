🌎 External Data Examples
=========================

Github
------

Links
~~~~~

Links to GitHub objects are set directly in the Sphinx-Needs objects by using 
`string-links <https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-string-links>`__.

See for instance the `github` option of :need:`SWREQ_001` or :need:`SWREQ_002`

PRs
~~~
.. needservice:: github-prs
   :specific: useblocks/sphinx-needs-demo/3
   :layout: adas

.. needextend:: GH_PR_3
   :+links: SWREQ_001


.. tip:: 
   :title: Show used documentation code.
   :collapsible:
   
   .. code-block:: rst
   
      .. needservice:: github-prs
         :specific: useblocks/sphinx-needs-demo/3
         :layout: adas

      .. needextend:: GH_PR_3
         :+links: SWREQ_001

Issues
~~~~~~

.. needservice:: github-issues
   :query: repo:useblocks/sphinx-needs-demo adas
   :id_prefix: GH_ISSUE_

.. needextend:: "Lane Marking" in title
   :+links:  SWREQ_001

.. needextend:: "Lane Deviation" in title
   :+links:  SWREQ_002

.. tip:: 
   :title: Show used documentation code.
   :collapsible:
   
   .. code-block:: rst

      .. needservice:: github-issues
         :query: repo:useblocks/sphinx-needs-demo adas
         :id_prefix: GH_ISSUE_

      .. needextend:: "Lane Marking" in title
         :+links:  SWREQ_001

      .. needextend:: "Lane Deviation" in title
         :+links:  SWREQ_002



Jira
----

Links
~~~~~
Links to Jira objects are set directly in the Sphinx-Needs objects by using 
`string-links <https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-string-links>`__.

See for instance the `jira` option of :need:`NEED_001` or :need:`REQ_001`