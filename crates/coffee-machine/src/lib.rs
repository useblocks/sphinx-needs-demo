//! BrewMaster Pro 3000 Coffee Machine Controller
//!
//! This crate implements the embedded controller software for the BrewMaster Pro 3000
//! automatic coffee machine, following the architectural specifications defined in
//! the sphinx-needs documentation.
//!
//! # Architecture
//!
//! The software is organized into modular components that communicate through
//! well-defined interfaces (traits):
//!
//! - Temperature Controller: PID-based temperature regulation
//! - Brew Controller: State machine managing brewing workflow
//! - User Interface: Button handling and user interaction
//! - Safety Monitor: Continuous safety checks and emergency shutdown
//! - Hardware Abstraction Layer: Sensor data acquisition and actuator control
//!
//! # Interface Traceability
//!
//! All interfaces in this crate correspond to specifications from
//! `docs/coffee-machine/index.rst`:
//!
//! - `INTF_TEMP_STATUS`      → [`TemperatureStatus`](interfaces::TemperatureStatus)
//! - `INTF_SAFETY_CMD`       → [`SafetyCommand`](interfaces::SafetyCommand)
//! - `INTF_TEMP_CTRL_STATUS` → [`TempCtrlStatus`](interfaces::TempCtrlStatus)
//! - `INTF_BREW_CTRL_STATUS` → [`BrewCtrlStatus`](interfaces::BrewCtrlStatus)
//! - `INTF_USER_CMD`         → [`UserCommand`](interfaces::UserCommand)
//! - `INTF_SENSOR_DATA`      → [`SensorData`](interfaces::SensorData)

pub mod interfaces;
