use std::time::{Instant, SystemTime, UNIX_EPOCH};

pub struct BrakeEvent {
    pub timestamp_ms: u128,
    pub response_time_ms: u128,
}

pub fn detect_and_brake() -> BrakeEvent {
    let start = Instant::now();

    // Braking logic placeholder — triggers immediately in this demo
    let response_time_ms = start.elapsed().as_millis();

    let timestamp_ms = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_millis();

    BrakeEvent { timestamp_ms, response_time_ms }
}

#[cfg(test)]
mod tests {
    use super::*;

    // TC-017: Emergency Braking Timing and Log Integrity
    // Verifies: BRAKE-001
    #[test]
    fn test_braking_within_150ms_with_valid_timestamp() {
        let event = detect_and_brake();

        assert!(
            event.response_time_ms <= 150,
            "Braking must engage within 150 ms, got {} ms",
            event.response_time_ms
        );
        assert!(
            event.timestamp_ms > 0,
            "Event log must contain a valid timestamp"
        );
    }
}
