Software Architecture
=====================

The software architecture defines the modular structure of the
BrewMaster Pro 3000's embedded control system. The architecture
follows a layered approach with clear separation of concerns:
safety-critical functions are isolated in dedicated modules, control
algorithms are encapsulated for reusability, and user interface logic
is decoupled from core brewing operations. This modular design enables
independent testing, facilitates maintenance, and provides clear
interfaces between components.

The architecture emphasizes fail-safe design principles. The Safety
Monitor Module operates with the highest priority and can override all
other subsystems. Module dependencies are carefully managed to prevent
circular references and ensure deterministic behavior. The following
diagram shows the architectural modules and their relationships:

Components
----------

.. component:: Temperature Controller Module
   :id: COMP_TEMP_CTRL
   :status: open
   :tags: module, control
   :implements: SWREQ_TEMP_REGULATION
   :uses: INTF_SAFETY_CMD, INTF_SENSOR_DATA
   :startup_calls: SEQSTART_07
   :shutdown_calls: SEQSHTDWN_03
   :collapse: true
   :template: component_arch

   Module responsible for PID-based temperature control. Interfaces:

   - Input: Temperature sensor (ADC)
   - Output: Heating element PWM control
   - Safety: Reports temperature status to Safety Monitor
   - Safety: Responds to emergency shutdown commands

.. component:: Brew Controller Module
   :id: COMP_BREW_CTRL
   :status: open
   :tags: module, control
   :implements: SWREQ_BREW_STRENGTH
   :uses: INTF_TEMP_STATUS, INTF_SAFETY_CMD, INTF_USER_CMD
   :startup_calls: SEQSTART_09
   :shutdown_calls: SEQSHTDWN_05
   :collapse: true
   :template: component_arch

   Module managing the brewing process state machine. States: IDLE,
   HEATING, BREWING, COMPLETE, ERROR. Controls pump and valve timing
   based on selected strength. Waits for temperature ready signal before
   initiating brew cycle. Monitors safety status continuously.

.. component:: User Interface Module
   :id: COMP_UI_MODULE
   :status: open
   :tags: module, ui
   :implements: SWREQ_BUTTON_INPUT
   :startup_calls: SEQSTART_01, SEQSTART_03
   :collapse: true
   :template: component_arch

   Module handling all user interactions including button debouncing, LED
   status indicators, and display updates. Interfaces with the Brew
   Controller to send user commands (strength selection, start/stop).

.. component:: Safety Monitor Module
   :id: COMP_SAFETY_MON
   :status: open
   :tags: module, safety
   :implements: SWREQ_WATER_LEVEL, SWREQ_OVERTEMP_SHUTDOWN
   :uses: INTF_TEMP_CTRL_STATUS, INTF_BREW_CTRL_STATUS, INTF_SENSOR_DATA
   :startup_calls: SEQSTART_04, SEQSTART_06, SEQSTART_08, SEQSTART_10
   :shutdown_calls: SEQSHTDWN_02, SEQSHTDWN_04, SEQSHTDWN_06
   :collapse: true
   :template: component_arch

   Module performing continuous safety checks on temperature and water
   level. Implements fail-safe shutdown procedures.

.. component:: Hardware Abstraction Layer
   :id: COMP_HAL
   :status: open
   :tags: module, hardware, driver
   :startup_calls: SEQSTART_02, SEQSTART_05
   :shutdown_calls: SEQSHTDWN_01
   :collapse: true
   :template: component_arch

   Module providing abstraction over hardware sensors and actuators.
   Handles low-level sensor reading via ADC, signal conditioning, and
   calibration. Interfaces:

   - Input: Temperature sensor (NTC thermistor via ADC channel 0)
   - Input: Water level sensor (capacitive via ADC channel 1)
   - Output: Heating element control (PWM channel)
   - Output: Pump control (GPIO)

   Implements DMA-based ADC sampling at 100Hz with automatic averaging
   and outlier rejection for robust sensor readings.

Component Interfaces
--------------------

The following interfaces define the communication contracts between
architectural components. Each interface specifies the data exchanged,
protocols used, and timing constraints to ensure deterministic and
safe inter-component communication.

.. interface:: Temperature Status Interface
   :id: INTF_TEMP_STATUS
   :status: open
   :tags: interface, control
   :provided_by: COMP_TEMP_CTRL
   :collapse: true

   **Provider**: Temperature Controller Module

   **Consumer**: Brew Controller Module

   **Description**: Provides current temperature readings and heating
   status to the brew controller.

   **Data Elements**:

   - current_temp: int16 (°C × 10 for 0.1°C resolution)
   - target_temp: int16 (°C × 10)
   - is_ready: bool (true when within target range)
   - heating_active: bool

   **Protocol**: Shared memory with atomic updates, 100ms refresh rate

.. interface:: Safety Command Interface
   :id: INTF_SAFETY_CMD
   :status: open
   :tags: interface, safety
   :provided_by: COMP_SAFETY_MON
   :collapse: true

   **Provider**: Safety Monitor Module

   **Consumers**: Temperature Controller, Brew Controller

   **Description**: Emergency shutdown commands from safety monitor to
   all controlled subsystems.

   **Commands**:

   - EMERGENCY_STOP: Immediate shutdown (<100ms response required)
   - RESUME_NORMAL: Clear emergency state after fault resolved

   **Protocol**: Interrupt-driven with hardware watchdog backup, highest
   priority

.. interface:: Temperature Controller Safety Status Interface
   :id: INTF_TEMP_CTRL_STATUS
   :status: open
   :tags: interface, safety
   :provided_by: COMP_TEMP_CTRL
   :collapse: true

   **Provider**: Temperature Controller Module

   **Consumer**: Safety Monitor Module

   **Description**: Heartbeat and fault status reported by the
   Temperature Controller to the Safety Monitor for fault detection.

   **Data Elements**:

   - module_id: uint8
   - heartbeat_counter: uint32 (incremented each cycle)
   - fault_flags: uint16 (bitfield of detected faults)
   - temperature_value: int16 (current measured temperature)

   **Protocol**: Polled by safety monitor at 10Hz

.. interface:: Brew Controller Safety Status Interface
   :id: INTF_BREW_CTRL_STATUS
   :status: open
   :tags: interface, safety
   :provided_by: COMP_BREW_CTRL
   :collapse: true

   **Provider**: Brew Controller Module

   **Consumer**: Safety Monitor Module

   **Description**: Heartbeat and fault status reported by the Brew
   Controller to the Safety Monitor for fault detection.

   **Data Elements**:

   - module_id: uint8
   - heartbeat_counter: uint32 (incremented each cycle)
   - fault_flags: uint16 (bitfield of detected faults)
   - water_level: uint8 (0-100%)

   **Protocol**: Polled by safety monitor at 10Hz

.. interface:: User Command Interface
   :id: INTF_USER_CMD
   :status: open
   :tags: interface, ui
   :provided_by: COMP_UI_MODULE
   :collapse: true

   **Provider**: User Interface Module

   **Consumer**: Brew Controller Module

   **Description**: User commands and settings passed from UI to the
   brewing state machine.

   **Commands**:

   - START_BREW(strength: enum {WEAK, MEDIUM, STRONG})
   - STOP_BREW
   - SELECT_STRENGTH(strength: enum)

   **Protocol**: Message queue with event-driven processing, debounced at
   UI layer

.. interface:: Sensor Data Interface
   :id: INTF_SENSOR_DATA
   :status: open
   :tags: interface, hardware
   :provided_by: COMP_HAL
   :collapse: true

   **Provider**: Hardware sensors (temperature, water level)

   **Consumers**: Temperature Controller, Safety Monitor

   **Description**: Raw sensor readings from hardware via ADC.

   **Data Elements**:

   - temp_sensor_raw: uint16 (ADC value 0-4095)
   - water_level_raw: uint16 (ADC value 0-4095)
   - sensor_timestamp: uint32 (milliseconds)

   **Protocol**: ADC DMA with double buffering, 100Hz sampling rate

Static View
-----------

.. needflow::
   :types: component, interface
   :filter: docname is not None and "coffee-machine" in docname
   :link_types: uses, provided_by
   :show_link_names:
   :config: toptobottom

Dynamic View
------------

The sequence diagrams below show how the architectural components
interact at runtime. Participants map directly to the components
defined in the Static View.

The diagrams are generated by ``needsequence``, which traverses the ``startup_calls``
/ ``shutdown_calls`` links defined on each component need. Each :need:`seq_msg <SEQSTART_01>`
need in the chain represents one message; odd hops are *participants*,
even hops are *messages*.

Startup Sequence
^^^^^^^^^^^^^^^^

On power-on the system initialises hardware, validates initial sensor
readings, then brings all control modules online in dependency order
before signalling readiness to the user.

The sequence message needs (``SEQSTART_01``–``SEQSTART_10``) are
defined below. ``COMP_UI_MODULE`` is the starting participant.

.. dropdown:: Startup Sequence Messages

   .. seq_msg:: init()
      :id: SEQSTART_01
      :startup_calls: COMP_HAL
      :collapse: true

      HAL hardware initialisation call from UI Module.

   .. seq_msg:: init_ok
      :id: SEQSTART_02
      :startup_calls: COMP_UI_MODULE
      :collapse: true

      HAL confirms successful ADC calibration to UI Module.

   .. seq_msg:: start() — Safety Monitor
      :id: SEQSTART_03
      :startup_calls: COMP_SAFETY_MON
      :collapse: true

      UI Module requests Safety Monitor to start and run pre-checks.

   .. seq_msg:: read_sensors()
      :id: SEQSTART_04
      :startup_calls: COMP_HAL
      :collapse: true

      Safety Monitor polls HAL for initial sensor readings.

   .. seq_msg:: temp=22°C, water_level=85%
      :id: SEQSTART_05
      :startup_calls: COMP_SAFETY_MON
      :collapse: true

      HAL returns ``INTF_SENSOR_DATA`` values; Safety Monitor asserts
      pre-conditions (temp < 100 °C, water > threshold).

   .. seq_msg:: start() — Temp Controller
      :id: SEQSTART_06
      :startup_calls: COMP_TEMP_CTRL
      :collapse: true

      Safety Monitor starts Temperature Controller Module.

   .. seq_msg:: started (INTF_TEMP_CTRL_STATUS heartbeat)
      :id: SEQSTART_07
      :startup_calls: COMP_SAFETY_MON
      :collapse: true

      Temperature Controller confirms startup via heartbeat on ``INTF_TEMP_CTRL_STATUS``.

   .. seq_msg:: start() — Brew Controller
      :id: SEQSTART_08
      :startup_calls: COMP_BREW_CTRL
      :collapse: true

      Safety Monitor starts Brew Controller Module.

   .. seq_msg:: started (INTF_BREW_CTRL_STATUS heartbeat)
      :id: SEQSTART_09
      :startup_calls: COMP_SAFETY_MON
      :collapse: true

      Brew Controller confirms startup via heartbeat on ``INTF_BREW_CTRL_STATUS``.

   .. seq_msg:: system_ready
      :id: SEQSTART_10
      :startup_calls: COMP_UI_MODULE
      :collapse: true

      Safety Monitor signals system readiness to UI Module; UI illuminates
      the Ready LED.

.. needsequence:: Startup Sequence
   :start: COMP_UI_MODULE
   :link_types: startup_calls

Safety Shutdown Sequence
^^^^^^^^^^^^^^^^^^^^^^^^

If the Safety Monitor detects an over-temperature condition it issues
an ``EMERGENCY_STOP`` command on ``INTF_SAFETY_CMD`` to all controlled
subsystems. All modules must respond within 100 ms.

The sequence message needs (``SEQSHTDWN_01``–``SEQSHTDWN_06``) are
defined below. ``COMP_HAL`` is the starting participant (it is the
source of the over-temperature sensor reading).

.. dropdown:: Safety Shutdown Sequence Messages

   .. seq_msg:: temp=102°C (INTF_SENSOR_DATA — over-temp)
      :id: SEQSHTDWN_01
      :shutdown_calls: COMP_SAFETY_MON
      :collapse: true

      HAL reports temperature exceeding 100 °C threshold to Safety Monitor
      via ``INTF_SENSOR_DATA`` (polled every 100 ms).

   .. seq_msg:: EMERGENCY_STOP → Temp Controller
      :id: SEQSHTDWN_02
      :shutdown_calls: COMP_TEMP_CTRL
      :collapse: true

      Safety Monitor broadcasts ``EMERGENCY_STOP`` on ``INTF_SAFETY_CMD`` to
      Temperature Controller; response required within 100 ms.

   .. seq_msg:: fault_flags=OVERTEMP (INTF_TEMP_CTRL_STATUS)
      :id: SEQSHTDWN_03
      :shutdown_calls: COMP_SAFETY_MON
      :collapse: true

      Temperature Controller confirms shutdown and reports ``FAULT_OVERTEMP``
      flag via ``INTF_TEMP_CTRL_STATUS``.

   .. seq_msg:: EMERGENCY_STOP → Brew Controller
      :id: SEQSHTDWN_04
      :shutdown_calls: COMP_BREW_CTRL
      :collapse: true

      Safety Monitor broadcasts ``EMERGENCY_STOP`` on ``INTF_SAFETY_CMD`` to
      Brew Controller; brew cycle aborted, pump stopped.

   .. seq_msg:: fault_flags=ABORT (INTF_BREW_CTRL_STATUS)
      :id: SEQSHTDWN_05
      :shutdown_calls: COMP_SAFETY_MON
      :collapse: true

      Brew Controller confirms abort and reports ``FAULT_ABORT`` flag via ``INTF_BREW_CTRL_STATUS``.

   .. seq_msg:: fault_event(OVERTEMP)
      :id: SEQSHTDWN_06
      :shutdown_calls: COMP_UI_MODULE
      :collapse: true

      Safety Monitor notifies UI Module of over-temperature fault; UI
      illuminates the Error LED and displays the fault message.

.. needsequence:: Safety Shutdown Sequence
   :start: COMP_HAL
   :link_types: shutdown_calls
