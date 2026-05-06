//! Interface traits for the BrewMaster Pro 3000 Coffee Machine
//!
//! This module contains trait definitions corresponding to the interface
//! specifications defined in the sphinx-needs documentation.
//! Each trait represents a communication contract between architectural
//! components as specified in docs/coffee-machine/index.rst

// @ BrewStrength enum, IMPL_BREW_STRENGTH, impl, [SWREQ_BREW_STRENGTH]
/// Brew strength selection for coffee brewing
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum BrewStrength {
    /// Weak: 180ml water, 3 minutes
    Weak,
    /// Medium: 180ml water, 4 minutes
    Medium,
    /// Strong: 180ml water, 5 minutes
    Strong,
}

// @ SafetyCommand enum, IMPL_SAFETY_CMD_ENUM, impl, [INTF_SAFETY_CMD]
/// Safety command types for emergency control
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum SafetyCommand {
    /// Immediate shutdown (<100ms response required)
    EmergencyStop,
    /// Clear emergency state after fault resolved
    ResumeNormal,
}

// @ UserCommand enum, IMPL_USER_CMD_ENUM, impl, [INTF_USER_CMD]
/// User command types for UI interaction
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum UserCommand {
    /// Start brewing with specified strength
    StartBrew(BrewStrength),
    /// Stop/cancel current brewing operation
    StopBrew,
    /// Select brew strength (without starting)
    SelectStrength(BrewStrength),
}

/// Temperature Status Interface (INTF_TEMP_STATUS)
///
/// **Provider**: Temperature Controller Module
///
/// **Consumer**: Brew Controller Module
///
/// **Description**: Provides current temperature readings and heating
/// status to the brew controller.
///
/// **Protocol**: Shared memory with atomic updates, 100ms refresh rate
// @ TemperatureStatus struct, IMPL_TEMP_STATUS, impl, [INTF_TEMP_STATUS]
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct TemperatureStatus {
    /// Current temperature in °C × 10 for 0.1°C resolution
    pub current_temp: i16,
    /// Target temperature in °C × 10
    pub target_temp: i16,
    /// True when within target range
    pub is_ready: bool,
    /// True when heating element is active
    pub heating_active: bool,
}

impl TemperatureStatus {
    /// Create a new temperature status
    pub fn new(current_temp: i16, target_temp: i16, is_ready: bool, heating_active: bool) -> Self {
        Self {
            current_temp,
            target_temp,
            is_ready,
            heating_active,
        }
    }

    /// Get current temperature in °C (floating point)
    pub fn current_temp_celsius(&self) -> f32 {
        self.current_temp as f32 / 10.0
    }

    /// Get target temperature in °C (floating point)
    pub fn target_temp_celsius(&self) -> f32 {
        self.target_temp as f32 / 10.0
    }
}

// @ TemperatureStatusProvider trait, IMPL_TEMP_STATUS_PROVIDER, impl, [INTF_TEMP_STATUS, COMP_TEMP_CTRL]
/// Trait for components that provide temperature status
///
/// Implements: Temperature Controller Module (COMP_TEMP_CTRL)
pub trait TemperatureStatusProvider {
    /// Get the current temperature status
    fn get_temperature_status(&self) -> TemperatureStatus;
}

// @ TemperatureStatusConsumer trait, IMPL_TEMP_STATUS_CONSUMER, impl, [INTF_TEMP_STATUS, COMP_BREW_CTRL]
/// Trait for components that consume temperature status
///
/// Implements: Brew Controller Module (COMP_BREW_CTRL)
pub trait TemperatureStatusConsumer {
    /// Update with new temperature status
    fn update_temperature_status(&mut self, status: TemperatureStatus);
}

/// Temperature Controller Status Interface (INTF_TEMP_CTRL_STATUS)
///
/// **Provider**: Temperature Controller Module (COMP_TEMP_CTRL)
///
/// **Consumer**: Safety Monitor Module (COMP_SAFETY_MON)
///
/// **Description**: Continuous status reporting from the Temperature Controller
/// to the Safety Monitor, including temperature readings and fault flags.
///
/// **Protocol**: Polled by safety monitor at 10Hz
// @ TempCtrlStatus struct, IMPL_TEMP_CTRL_STATUS, impl, [INTF_TEMP_CTRL_STATUS]
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct TempCtrlStatus {
    /// Module identifier (fixed value for Temperature Controller)
    pub module_id: u8,
    /// Heartbeat counter (incremented each control cycle)
    pub heartbeat_counter: u32,
    /// Bitfield of detected faults (0 = no fault)
    pub fault_flags: u16,
    /// Current measured temperature (°C × 10 for 0.1°C resolution)
    pub temperature_value: i16,
}

impl TempCtrlStatus {
    /// Create a new temperature controller status
    pub fn new(
        module_id: u8,
        heartbeat_counter: u32,
        fault_flags: u16,
        temperature_value: i16,
    ) -> Self {
        Self {
            module_id,
            heartbeat_counter,
            fault_flags,
            temperature_value,
        }
    }

    /// Check if any faults are present
    pub fn has_faults(&self) -> bool {
        self.fault_flags != 0
    }

    /// Get temperature in °C (floating point)
    pub fn temperature_celsius(&self) -> f32 {
        self.temperature_value as f32 / 10.0
    }
}

// @ TempCtrlStatusProvider trait, IMPL_TEMP_CTRL_STATUS_PROVIDER, impl, [INTF_TEMP_CTRL_STATUS, COMP_TEMP_CTRL]
/// Trait for the Temperature Controller to expose its status to the Safety Monitor
///
/// Implements: Temperature Controller Module (COMP_TEMP_CTRL)
pub trait TempCtrlStatusProvider {
    /// Get the current temperature controller status
    fn get_temp_ctrl_status(&self) -> TempCtrlStatus;
}

// @ TempCtrlStatusConsumer trait, IMPL_TEMP_CTRL_STATUS_CONSUMER, impl, [INTF_TEMP_CTRL_STATUS, COMP_SAFETY_MON]
/// Trait for the Safety Monitor to consume temperature controller status
///
/// Implements: Safety Monitor Module (COMP_SAFETY_MON)
pub trait TempCtrlStatusConsumer {
    /// Process a temperature controller status update
    fn process_temp_ctrl_status(&mut self, status: TempCtrlStatus);
}

/// Brew Controller Status Interface (INTF_BREW_CTRL_STATUS)
///
/// **Provider**: Brew Controller Module (COMP_BREW_CTRL)
///
/// **Consumer**: Safety Monitor Module (COMP_SAFETY_MON)
///
/// **Description**: Continuous status reporting from the Brew Controller
/// to the Safety Monitor, including water level readings and fault flags.
///
/// **Protocol**: Polled by safety monitor at 10Hz
// @ BrewCtrlStatus struct, IMPL_BREW_CTRL_STATUS, impl, [INTF_BREW_CTRL_STATUS]
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct BrewCtrlStatus {
    /// Module identifier (fixed value for Brew Controller)
    pub module_id: u8,
    /// Heartbeat counter (incremented each control cycle)
    pub heartbeat_counter: u32,
    /// Bitfield of detected faults (0 = no fault)
    pub fault_flags: u16,
    /// Current water level (0–100%)
    pub water_level: u8,
}

impl BrewCtrlStatus {
    /// Create a new brew controller status
    pub fn new(
        module_id: u8,
        heartbeat_counter: u32,
        fault_flags: u16,
        water_level: u8,
    ) -> Self {
        Self {
            module_id,
            heartbeat_counter,
            fault_flags,
            water_level,
        }
    }

    /// Check if any faults are present
    pub fn has_faults(&self) -> bool {
        self.fault_flags != 0
    }
}

// @ BrewCtrlStatusProvider trait, IMPL_BREW_CTRL_STATUS_PROVIDER, impl, [INTF_BREW_CTRL_STATUS, COMP_BREW_CTRL]
/// Trait for the Brew Controller to expose its status to the Safety Monitor
///
/// Implements: Brew Controller Module (COMP_BREW_CTRL)
pub trait BrewCtrlStatusProvider {
    /// Get the current brew controller status
    fn get_brew_ctrl_status(&self) -> BrewCtrlStatus;
}

// @ BrewCtrlStatusConsumer trait, IMPL_BREW_CTRL_STATUS_CONSUMER, impl, [INTF_BREW_CTRL_STATUS, COMP_SAFETY_MON]
/// Trait for the Safety Monitor to consume brew controller status
///
/// Implements: Safety Monitor Module (COMP_SAFETY_MON)
pub trait BrewCtrlStatusConsumer {
    /// Process a brew controller status update
    fn process_brew_ctrl_status(&mut self, status: BrewCtrlStatus);
}

/// Safety Command Interface (INTF_SAFETY_CMD)
///
/// **Provider**: Safety Monitor Module
///
/// **Consumers**: Temperature Controller, Brew Controller
///
/// **Description**: Emergency shutdown commands from safety monitor to
/// all controlled subsystems.
///
/// **Protocol**: Interrupt-driven with hardware watchdog backup, highest priority
// @ SafetyCommandProvider trait, IMPL_SAFETY_CMD_PROVIDER, impl, [INTF_SAFETY_CMD, COMP_SAFETY_MON]
pub trait SafetyCommandProvider {
    /// Send a safety command to subsystems
    fn send_safety_command(&self, command: SafetyCommand);
}

// @ SafetyCommandConsumer trait, IMPL_SAFETY_CMD_CONSUMER, impl, [INTF_SAFETY_CMD, COMP_TEMP_CTRL, COMP_BREW_CTRL]
/// Trait for components that receive safety commands
///
/// Implements: Temperature Controller (COMP_TEMP_CTRL), Brew Controller (COMP_BREW_CTRL)
pub trait SafetyCommandConsumer {
    /// Handle a safety command (must respond within 100ms for EMERGENCY_STOP)
    fn handle_safety_command(&mut self, command: SafetyCommand);
}

/// User Command Interface (INTF_USER_CMD)
///
/// **Provider**: User Interface Module
///
/// **Consumer**: Brew Controller Module
///
/// **Description**: User commands and settings passed from UI to the
/// brewing state machine.
///
/// **Protocol**: Message queue with event-driven processing, debounced at UI layer
// @ UserCommandProvider trait, IMPL_USER_CMD_PROVIDER, impl, [INTF_USER_CMD, COMP_UI_MODULE]
pub trait UserCommandProvider {
    /// Send a user command to the brew controller
    fn send_user_command(&self, command: UserCommand);
}

// @ UserCommandConsumer trait, IMPL_USER_CMD_CONSUMER, impl, [INTF_USER_CMD, COMP_BREW_CTRL]
/// Trait for components that consume user commands
///
/// Implements: Brew Controller Module (COMP_BREW_CTRL)
pub trait UserCommandConsumer {
    /// Handle a user command
    fn handle_user_command(&mut self, command: UserCommand);
}

/// Sensor Data Interface (INTF_SENSOR_DATA)
///
/// **Provider**: Hardware sensors (temperature, water level)
///
/// **Consumers**: Temperature Controller, Safety Monitor
///
/// **Description**: Raw sensor readings from hardware via ADC.
///
/// **Protocol**: ADC DMA with double buffering, 100Hz sampling rate
// @ SensorData struct, IMPL_SENSOR_DATA, impl, [INTF_SENSOR_DATA]
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct SensorData {
    /// Temperature sensor ADC value (0-4095)
    pub temp_sensor_raw: u16,
    /// Water level sensor ADC value (0-4095)
    pub water_level_raw: u16,
    /// Timestamp in milliseconds
    pub sensor_timestamp: u32,
}

impl SensorData {
    /// Create new sensor data
    pub fn new(temp_sensor_raw: u16, water_level_raw: u16, sensor_timestamp: u32) -> Self {
        Self {
            temp_sensor_raw,
            water_level_raw,
            sensor_timestamp,
        }
    }
}

// @ SensorDataProvider trait, IMPL_SENSOR_DATA_PROVIDER, impl, [INTF_SENSOR_DATA, COMP_ADC_DRV]
/// Trait for components that provide sensor data
///
/// Implements: ADC Driver (COMP_ADC_DRV)
pub trait SensorDataProvider {
    /// Get the latest sensor readings
    fn get_sensor_data(&self) -> SensorData;
}

// @ SensorDataConsumer trait, IMPL_SENSOR_DATA_CONSUMER, impl, [INTF_SENSOR_DATA, COMP_TEMP_CTRL, COMP_SAFETY_MON]
/// Trait for components that consume sensor data
///
/// Implements: Temperature Controller (COMP_TEMP_CTRL), Safety Monitor (COMP_SAFETY_MON)
pub trait SensorDataConsumer {
    /// Process new sensor data
    fn process_sensor_data(&mut self, data: SensorData);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_temperature_status_conversions() {
        let status = TemperatureStatus::new(900, 950, true, false);
        assert_eq!(status.current_temp_celsius(), 90.0);
        assert_eq!(status.target_temp_celsius(), 95.0);
        assert_eq!(status.is_ready, true);
        assert_eq!(status.heating_active, false);
    }

    #[test]
    fn test_temp_ctrl_status_fault_detection() {
        let status_no_fault = TempCtrlStatus::new(1, 100, 0, 900);
        assert_eq!(status_no_fault.has_faults(), false);
        assert_eq!(status_no_fault.temperature_celsius(), 90.0);

        let status_with_fault = TempCtrlStatus::new(1, 101, 0x0001, 900);
        assert_eq!(status_with_fault.has_faults(), true);
    }

    #[test]
    fn test_brew_ctrl_status_fault_detection() {
        let status_no_fault = BrewCtrlStatus::new(2, 100, 0, 80);
        assert_eq!(status_no_fault.has_faults(), false);
        assert_eq!(status_no_fault.water_level, 80);

        let status_with_fault = BrewCtrlStatus::new(2, 101, 0x0001, 80);
        assert_eq!(status_with_fault.has_faults(), true);
    }

    #[test]
    fn test_brew_strength_enum() {
        let strength = BrewStrength::Medium;
        assert_eq!(strength, BrewStrength::Medium);
        assert_ne!(strength, BrewStrength::Weak);
    }

    #[test]
    fn test_user_command_variants() {
        let cmd1 = UserCommand::StartBrew(BrewStrength::Strong);
        let cmd2 = UserCommand::StopBrew;
        let cmd3 = UserCommand::SelectStrength(BrewStrength::Weak);

        match cmd1 {
            UserCommand::StartBrew(BrewStrength::Strong) => (),
            _ => panic!("Wrong command variant"),
        }

        match cmd2 {
            UserCommand::StopBrew => (),
            _ => panic!("Wrong command variant"),
        }

        match cmd3 {
            UserCommand::SelectStrength(BrewStrength::Weak) => (),
            _ => panic!("Wrong command variant"),
        }
    }

    #[test]
    fn test_sensor_data_creation() {
        let data = SensorData::new(2048, 3000, 12345);
        assert_eq!(data.temp_sensor_raw, 2048);
        assert_eq!(data.water_level_raw, 3000);
        assert_eq!(data.sensor_timestamp, 12345);
    }
}
