Requirements Teen
=================

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
   :status: open
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
   :status: open
 
   The car must offer a range of customization options, including exterior colors, interior finishes, and optional accessories, allowing teenagers to personalize their vehicles to reflect their individual styles and preferences.

.. req:: Fuel Efficiency
   :id: TEEN_EFF
   :tags: teen, efficiency
   :author: ROBERT
   :release: REL_TEEN_2025_1
   :status: open
   
   The car should prioritize fuel efficiency, with a focus on eco-friendly technologies such as hybrid or electric powertrains, to minimize environmental impact and reduce operating costs for teenage drivers.

.. req:: User-Friendly Interface
   :id: TEEN_USER
   :tags: teen, user
   :author: ROBERT
   :release: REL_TEEN_2025_1
   :status: open

   The car's interface should be intuitive and easy to use, with a touchscreen infotainment system, voice recognition capabilities, and simplified controls to enhance the driving experience for teenage users.
