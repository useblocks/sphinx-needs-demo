Test Cases
==========

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
   :collapse: true

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
   :collapse: true

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
   :collapse: true

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
   :collapse: true

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
   :collapse: true

   **Objective**: Verify complete brewing cycle from user input to coffee
   output.

   **Steps**:

   1. Select medium strength
   2. Press start button
   3. Monitor temperature, water flow, and timing

   **Expected**: System heats to 85-95°C, dispenses 180ml over 4 minutes,
   returns to idle state, no safety triggers.
