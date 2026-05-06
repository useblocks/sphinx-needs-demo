System Requirements
===================

The system requirements capture the fundamental capabilities that the
BrewMaster Pro 3000 must deliver to meet customer expectations and
safety standards. These high-level requirements define what the system
does from an external perspective, focusing on user-visible behavior
and safety constraints. Each requirement has been derived from market
analysis, customer feedback, and applicable safety regulations for
household appliances.

.. req:: Brew Coffee
   :id: REQ_BREW_COFFEE
   :status: open
   :tags: brewing, core
   :collapse: true

   The coffee machine shall be able to brew coffee with user-selected
   strength (weak, medium, strong).

.. req:: Heat Water
   :id: REQ_HEAT_WATER
   :status: open
   :tags: heating, safety
   :collapse: true

   The coffee machine shall heat water to the appropriate temperature
   (85-95°C) for brewing coffee.

.. req:: User Interface
   :id: REQ_USER_INTERFACE
   :status: open
   :tags: ui, usability
   :collapse: true

   The coffee machine shall provide a user interface with buttons for
   selecting coffee strength and starting the brewing process.

.. req:: Safety Shutdown
   :id: REQ_SAFETY_SHUTDOWN
   :status: open
   :tags: safety, critical
   :collapse: true

   The coffee machine shall automatically shut down if the water
   temperature exceeds 100°C or if no water is detected.
