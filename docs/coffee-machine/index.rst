☕️ Coffee Machine Example
==========================

This example demonstrates a complete traceability chain for a coffee
machine system, from high-level requirements down to implementation
and test cases.

The **BrewMaster Pro 3000** is an advanced automatic coffee machine
designed for commercial and high-end residential use. Featuring
precision temperature control, customizable brew strength settings,
and comprehensive safety mechanisms, it represents the cutting edge of
coffee brewing technology. This document traces the complete
development lifecycle from initial customer needs through verified
implementation.

System Requirements
-------------------

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

   The coffee machine shall be able to brew coffee with user-selected
   strength (weak, medium, strong).

.. req:: Heat Water
   :id: REQ_HEAT_WATER
   :status: open
   :tags: heating, safety

   The coffee machine shall heat water to the appropriate temperature
   (85-95°C) for brewing coffee.

.. req:: User Interface
   :id: REQ_USER_INTERFACE
   :status: open
   :tags: ui, usability

   The coffee machine shall provide a user interface with buttons for
   selecting coffee strength and starting the brewing process.

.. req:: Safety Shutdown
   :id: REQ_SAFETY_SHUTDOWN
   :status: open
   :tags: safety, critical

   The coffee machine shall automatically shut down if the water
   temperature exceeds 100°C or if no water is detected.

Software Requirements
---------------------

The software requirements section refines the high-level system
requirements into detailed, implementable specifications for the
embedded control system. The BrewMaster Pro 3000 runs on a custom
Python-based embedded platform with real-time capabilities, chosen for
its rapid development cycle and extensive library support. These
requirements specify precise timing constraints, control algorithms,
and safety-critical behavior that must be implemented in software.
Each software requirement is traceable back to one or more system
requirements, ensuring complete coverage of customer needs.

.. swreq:: Temperature Regulation
   :id: SWREQ_TEMP_REGULATION
   :status: open
   :tags: control, heating
   :reqs: REQ_HEAT_WATER

   The temperature control software shall monitor the water temperature
   sensor and regulate the heating element to maintain temperature
   between 85-95°C using PID control.

.. swreq:: Over-Temperature Shutdown
   :id: SWREQ_OVERTEMP_SHUTDOWN
   :status: open
   :tags: safety, critical
   :reqs: REQ_SAFETY_SHUTDOWN

   The software shall continuously monitor water temperature and trigger
   an emergency shutdown within 100ms if temperature exceeds 100°C to
   prevent boiling and potential hazards.

.. swreq:: Brew Strength Selection
   :id: SWREQ_BREW_STRENGTH
   :status: open
   :tags: control, brewing
   :reqs: REQ_BREW_COFFEE

   The software shall implement brew strength selection by controlling
   the water flow rate and brewing time:

   - Weak: 180ml water, 3 minutes
   - Medium: 180ml water, 4 minutes
   - Strong: 180ml water, 5 minutes

.. swreq:: Button Input Handler
   :id: SWREQ_BUTTON_INPUT
   :status: open
   :tags: ui, input
   :reqs: REQ_USER_INTERFACE

   The software shall process button inputs with debouncing and trigger
   appropriate actions (strength selection, start brewing, stop/cancel).

.. swreq:: Water Level Monitoring
   :id: SWREQ_WATER_LEVEL
   :status: open
   :tags: safety, monitoring
   :reqs: REQ_SAFETY_SHUTDOWN

   The software shall continuously monitor the water level sensor and
   prevent brewing operations when water level is below minimum
   threshold.

Software Architecture
---------------------

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

.. needflow::
   :types: swarch
   :filter: docname is not None and "coffee-machine" in docname
   :show_link_names:

.. swarch:: Temperature Controller Module
   :id: SWARCH_TEMP_CTRL
   :status: open
   :tags: module, control
   :implements: SWREQ_TEMP_REGULATION
   :depends_on: SWARCH_SAFETY_MON

   Module responsible for PID-based temperature control. Interfaces:

   - Input: Temperature sensor (ADC)
   - Output: Heating element PWM control
   - Safety: Reports temperature status to Safety Monitor
   - Safety: Responds to emergency shutdown commands

.. swarch:: Brew Controller Module
   :id: SWARCH_BREW_CTRL
   :status: open
   :tags: module, control
   :implements: SWREQ_BREW_STRENGTH
   :depends_on: SWARCH_TEMP_CTRL, SWARCH_SAFETY_MON

   Module managing the brewing process state machine. States: IDLE,
   HEATING, BREWING, COMPLETE, ERROR. Controls pump and valve timing
   based on selected strength. Waits for temperature ready signal before
   initiating brew cycle. Monitors safety status continuously.

.. swarch:: User Interface Module
   :id: SWARCH_UI_MODULE
   :status: open
   :tags: module, ui
   :implements: SWREQ_BUTTON_INPUT
   :depends_on: SWARCH_BREW_CTRL

   Module handling all user interactions including button debouncing, LED
   status indicators, and display updates. Interfaces with the Brew
   Controller to send user commands (strength selection, start/stop).

.. swarch:: Safety Monitor Module
   :id: SWARCH_SAFETY_MON
   :status: open
   :tags: module, safety
   :implements: SWREQ_WATER_LEVEL, SWREQ_OVERTEMP_SHUTDOWN

   Module performing continuous safety checks on temperature and water
   level. Implements fail-safe shutdown procedures.

Implementation
--------------

The implementation phase translates the architectural designs into
working code. All BrewMaster Pro 3000 software is implemented in
Python 3.11, running on a Raspberry Pi Compute Module with real-time
extensions. The implementation follows strict coding standards
including comprehensive type hinting, defensive programming practices,
and extensive inline documentation.

Each implementation artifact maps directly to an architectural module,
ensuring traceability from design to code. The code is organized in
the ``src/coffee_controller.py`` module, with clear class boundaries
matching the architectural decomposition. All safety-critical code
undergoes additional review and is marked with special annotations for
audit purposes.

.. impl:: Temperature PID Controller
   :id: IMPL_TEMP_PID
   :status: open
   :tags: python, control
   :realizes: SWARCH_TEMP_CTRL

   Implementation: ``src/coffee_controller.py::TemperatureController``

   PID controller with Kp=2.0, Ki=0.5, Kd=1.0 tuned for rapid heating
   with minimal overshoot.

.. impl:: Brew State Machine
   :id: IMPL_BREW_FSM
   :status: open
   :tags: python, control
   :realizes: SWARCH_BREW_CTRL

   Implementation: ``src/coffee_controller.py::BrewStateMachine``

   Finite state machine managing brewing workflow with configurable
   timing parameters per strength setting.

.. impl:: Button Handler
   :id: IMPL_BUTTON_HANDLER
   :status: open
   :tags: python, ui
   :realizes: SWARCH_UI_MODULE

   Implementation: ``src/coffee_controller.py::ButtonHandler``

   Interrupt-driven button handler with 50ms debounce timeout. Sends
   commands to the brew state machine to select strength and initiate
   brewing.

.. impl:: Safety Watchdog
   :id: IMPL_SAFETY_WATCHDOG
   :status: open
   :tags: python, safety
   :realizes: SWARCH_SAFETY_MON

   Implementation: ``src/coffee_controller.py::SafetyWatchdog``

   Runs at 10Hz monitoring all safety-critical parameters. Implements
   hardware watchdog timer reset to prevent lockup.

Test Cases
----------

Comprehensive testing ensures that the BrewMaster Pro 3000 meets all
specified requirements and operates safely under all conditions. The
test strategy employs multiple levels:

- **Unit Tests**: Verify individual components in isolation (temperature
  control, button debouncing, state machine transitions)
- **Integration Tests**: Validate interactions between modules (brew
  controller coordinating with temperature controller)
- **System Tests**: End-to-end verification of complete brewing cycles
- **Safety Tests**: Dedicated verification of all safety-critical
  functions under normal and fault conditions

All tests are automated and integrated into the continuous integration
pipeline. Safety-critical tests are executed on hardware-in-the-loop
test benches that simulate real sensors, actuators, and fault
conditions. Test coverage targets are set based on the criticality of
each component.

.. test:: Test Temperature Control
   :id: TEST_TEMP_CONTROL
   :status: open
   :tags: unit, control
   :specs: SWREQ_TEMP_REGULATION

   **Objective**: Verify temperature controller maintains target
   temperature within ±2°C.

   **Steps**:

   1. Initialize controller with target 90°C
   2. Simulate temperature sensor readings from 20°C to 95°C
   3. Record PWM output at each temperature

   **Expected**: PWM duty cycle decreases as temperature approaches
   target, maintains oscillation within ±2°C of setpoint.

.. test:: Test Brew Strength Settings
   :id: TEST_BREW_STRENGTH
   :status: open
   :tags: integration, brewing
   :specs: SWREQ_BREW_STRENGTH

   **Objective**: Verify all three strength settings produce correct
   timing and water volume.

   **Test Cases**:

   - Weak: Assert 180ml water dispensed in 3 min ±5s
   - Medium: Assert 180ml water dispensed in 4 min ±5s
   - Strong: Assert 180ml water dispensed in 5 min ±5s

.. test:: Test Button Debouncing
   :id: TEST_BUTTON_DEBOUNCE
   :status: open
   :tags: unit, ui
   :specs: SWREQ_BUTTON_INPUT

   **Objective**: Verify button handler correctly debounces rapid inputs.

   **Steps**:

   1. Simulate 10 button presses within 200ms
   2. Count triggered events

   **Expected**: Only 1-2 events triggered (first press + possible bounce
   after 50ms timeout).

.. test:: Test Safety Shutdown
   :id: TEST_SAFETY_SHUTDOWN
   :status: open
   :tags: integration, safety
   :specs: SWREQ_OVERTEMP_SHUTDOWN, SWREQ_WATER_LEVEL

   **Objective**: Verify safety monitor triggers shutdown on critical
   conditions.

   **Test Cases**:

   - Over-temperature: Set temp > 100°C, assert shutdown within 100ms
   - Low water: Set water level < threshold, assert brewing prevented
   - Watchdog timeout: Block safety loop, assert hardware reset within 1s

.. test:: Test End-to-End Brewing
   :id: TEST_E2E_BREWING
   :status: open
   :tags: system, e2e
   :specs: SWREQ_BREW_STRENGTH, SWREQ_TEMP_REGULATION, SWREQ_BUTTON_INPUT

   **Objective**: Verify complete brewing cycle from user input to coffee
   output.

   **Steps**:

   1. Select medium strength
   2. Press start button
   3. Monitor temperature, water flow, and timing

   **Expected**: System heats to 85-95°C, dispenses 180ml over 4 minutes,
   returns to idle state, no safety triggers.

Traceability Overview
---------------------

Complete traceability is a cornerstone of the BrewMaster Pro 3000
development process. Every line of code can be traced back through
architectural designs and requirements to the original customer need
or safety regulation. Conversely, every requirement can be traced
forward to its implementation and verification test cases. This
bidirectional traceability ensures nothing is missed and enables rapid
impact analysis when requirements change.

The sphinx-needs tool automates traceability management, maintaining
links between artifacts and generating visual diagrams. This example
demonstrates:

- **Requirements → SW Requirements**: High-level needs decomposed into
  software-specific requirements
- **SW Requirements → Architecture**: Requirements mapped to software
  modules
- **Architecture → Implementation**: Architectural designs realized in
  code
- **Implementation → Tests**: All implementations verified through test
  cases

Use the query tools to explore the relationships between these needs
and verify complete traceability coverage.

Traceability Diagram
^^^^^^^^^^^^^^^^^^^^

The following diagram shows all needs and their connections in this
coffee machine example:

.. needflow::
   :types: req, swreq, swarch, impl, test
   :filter: docname is not None and "coffee-machine" in docname
   :show_link_names:
   :show_filters:
