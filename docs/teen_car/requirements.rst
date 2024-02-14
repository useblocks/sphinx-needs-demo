{% set page="requirements.rst" %}
{% include "demo_page_header.rst" with context %}

.. _req_teen:

🙇 Requirements Teen
====================


.. req:: Safety Features
   :id: TEEN_SAFE
   :tags: teen, safe
   :author: ROBERT
   :release: REL_TEEN_2024_6
   :status: open

   The car must include advanced safety features such as automatic braking, collision avoidance systems, and adaptive cruise control to ensure the safety of teenage drivers.

.. req:: Connectivity and Entertainment
   :id: TEEN_CON
   :tags: teen, connection
   :author: ROBERT, PETER
   :release: REL_TEEN_2025_6
   :status: in progress
   :based_on: BASE_WIFI, BASE_BT
 
   The car should be equipped with built-in Wi-Fi, Bluetooth connectivity, and compatibility with smartphone integration systems to enable seamless communication and entertainment for teenagers on the go.

   .. uml::

        @startuml
       
        node Car {
         card ConnectBox
         card BluetoothDevice
         cloud WifiDevice

        }

        BluetoothDevice <--> ConnectBox
        WifiDevice <--> ConnectBox

        @enduml    

.. req:: Customization Options
   :id: TEEN_CUSTOM
   :tags: teen, customization
   :author: PETER
   :release: REL_TEEN_2024_6
   :status: closed
 
   The car must offer a range of customization options, including exterior colors, interior finishes, and optional accessories, allowing teenagers to personalize their vehicles to reflect their individual styles and preferences.

.. req:: Fuel Efficiency
   :id: TEEN_EFF
   :tags: teen, efficiency
   :author: ROBERT
   :release: REL_TEEN_2025_1
   :status: closed
   
   The car should prioritize fuel efficiency, with a focus on eco-friendly technologies such as hybrid or electric powertrains, to minimize environmental impact and reduce operating costs for teenage drivers.

.. req:: User-Friendly Interface
   :id: TEEN_USER
   :tags: teen, user
   :author: ROBERT
   :release: REL_TEEN_2025_1
   :status: open

   The car's interface should be intuitive and easy to use, with a touchscreen infotainment system, voice recognition capabilities, and simplified controls to enhance the driving experience for teenage users.


.. req:: Customer specific RADAR configuration
   :id: TEEN_CUSTOMER
   :tags: teen, customer
   :author: customer_a:ROBERT, customer_b:SARAH
   :release: REL_TEEN_2025_1
   :status: customer_a:open, customer_b:closed
   :customer: B

   We need to adapt the configuration of our RADAR system depending on the final customer.

   .. tip:: 
      :title: Demo feature hint: Variant handling
      :collapsible: 
   
      This Requirement is using variant handling.
      Depending on the value of the ``customer`` option (``A`` or ``B``), status and author get updated.

      The variant matrix looks like this:

      .. list-table::
         :header-rows: 1
         :stub-columns: 1

         - * customer
           * author
           * status
         - * A
           * ROBERT
           * open
         - * B
           * SARAH
           * closed


      | The used code for the options is:
      | **author**: ``customer_a:ROBERT, customer_b:SARAH``
      | **status**: ``customer_a:open, customer_b:closed``

      The value of ``customer`` in this example is: **[[copy("customer")]]**. Therefore ``author`` is finally **[[copy("author")]]** and ``status`` is **[[copy("status")]]**.

      Setting values of options can be done dynamically and triggered from outside. So different build commands could result in a totally different document thanks
      to the used ``needs_variant`` feature.
