.. dropdown:: Demo feature hint: Constraints

      For requirements two constraints are defined, which check if the ``status`` is set correctly and if a ``release`` is linked.

      If these constraints are not fulfilled, the need object gets a colored right border and the footer contains the reason why a
      constraint is not fulfilled.

      Constraints can be defined in the ``conf.py`` file:

      .. code-block:: python

         needs_constraints = {
            "status_set": {
               "check_0": "status is not None and status in ['open', 'in progress', 'closed']",
               "severity": "LOW",
               "error_message": "Status is invalid or not set!"
            },
            "release_set": {
               "check_0": "len(release)>0",
               "severity": "CRITICAL",
               "error_message": "Requirement is not planned for any release!"
            },
         }

      Depending on the *severity*, the build is stopped or a warning gets printed::

         /sphinx-needs-demo/docs/granny_car/requirements.rst:20: WARNING: Constraint len(release)>0 for need GRANNY_EXAMPLE FAILED! severity: CRITICAL Requirement is not planned for any release! [needs.constraint]

      Docs: `needs_constraints by Sphinx-Needs <https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-constraints>`__.
