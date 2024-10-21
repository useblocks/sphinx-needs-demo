🖌 SW Architecture
=================

.. note::

   This part is under heavy development.

.. system:: Test Sys
   :id: ARCH_SYS
   :contains: ARCH_COMP_1, ARCH_COMP_2

   .. needarch::
      
      node "{{need().title}}" as node {
      {{uml("ARCH_COMP_1") }}
      {{uml("ARCH_COMP_2") }}
      ' should be {{import("contains") }}
      }

.. component:: Test Comp 1
   :id: ARCH_COMP_1
   :contains: ARCH_INT_1, ARCH_INT_2

   .. needarch::

      card "{{need().title}}" as ARCH_COMP_1 #ccc{
      {{import("contains") }}
      }

.. component:: Test Comp 2
   :id: ARCH_COMP_2

   .. needarch::

      card "{{need().title}}" as ARCH_COMP_2 #ccc

.. interface:: Test Int 1
   :id: ARCH_INT_1

   .. needarch::

      circle "Test Int 1" as ARCH_INT_1 #AA2222

.. interface:: Test Int 2
   :id: ARCH_INT_2

   .. needarch::

      circle "Test Int 2" as ARCH_INT_2 #22AAAA

Sequence diagrams
-----------------

.. needuml::

   actor "User" as user
   entity "{{needs["ARCH_INT_1"].title}}" as ARCH_INT_1
   entity "{{needs["ARCH_INT_2"].title}}" as ARCH_INT_2
   participant "{{needs["ARCH_COMP_2"].title}}" as ARCH_COMP_2

   user -> ARCH_INT_1 : Triggers interface via button
   ARCH_INT_1 -> ARCH_INT_2 : New message
   ARCH_INT_2 -> ARCH_COMP_2: Inform component


Timing diagram
--------------

.. needuml::

   robust "{{needs["ARCH_COMP_1"].title}}" as {{needs["ARCH_COMP_1"].id}}
   concise "{{needs["ARCH_SYS"].title}}" as {{needs["ARCH_SYS"].id}}

   @0
   {{needs["ARCH_COMP_1"].id}} is Idle
   {{needs["ARCH_SYS"].id}} is Idle

   @100
   {{needs["ARCH_COMP_1"].id}} is Waiting
   {{needs["ARCH_SYS"].id}} is Processing

   @300
   ARCH_COMP_1 is Processing
   ARCH_SYS is Waiting