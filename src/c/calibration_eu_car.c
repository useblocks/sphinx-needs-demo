/**
 * EU / passenger car (combi / cabrio) calibration profile - pseudo-code implementation
 *
 * Calibration profile: eu_car  (location = eu, vehicle type = passenger car (combi / cabrio))
 * Build tags: sphinx-build -t eu -t combi   (also the untagged default; -t eu -t cabrio) ...
 *
 * Holds the threshold values consumed by the shared Lane Keeping (SWREQ_002)
 * and Adaptive Cruise Control (SWREQ_005) modules for this location x type
 * combination. Only this file is traced for the matching build; its `impl`
 * needs link upward to SWREQ_002 and SWREQ_005. Every other profile traces its
 * own calibration file instead.
 *
 * This profile uses the UNECE R79 / EU GSR reference for passenger cars.
 */

#include "lane_keeping.h"
#include "acc.h"

/* EU passenger car (combi / cabrio) calibration - resolved from the (location x type) combination. */
#define LANE_DEVIATION_WARN_THRESHOLD_M   0.40f   /* SWREQ_002 tuning: eu_car */
#define FOLLOWING_TIME_GAP_S              2.0f   /* SWREQ_005 tuning: eu_car */

// @ Lane deviation warning - EU passenger car (combi / cabrio) calibration (0.40 m), IMPL_LKA_DEVIATION_CAL_EU_CAR, impl, [SWREQ_002]
/**
 * Trigger the lane-departure warning once the lateral offset exceeds the
 * EU passenger car (combi / cabrio) threshold of 0.40 m without an active turn signal.
 */
int check_lane_deviation_eu_car(const LaneKeepingModule *lka, int turn_signal_active)
{
    if (turn_signal_active)
        return 0;
    return lka->lane_offset_m > LANE_DEVIATION_WARN_THRESHOLD_M;
}

// @ Speed control headway - EU passenger car (combi / cabrio) calibration (2.0 s), IMPL_ACC_SPEED_CAL_EU_CAR, impl, [SWREQ_005]
/**
 * Adjust the speed setpoint to maintain the EU passenger car (combi / cabrio) following time gap of
 * 2.0 s relative to the vehicle ahead.
 */
void adjust_speed_eu_car(AdaptiveCruiseModule *acc)
{
    acc->target_speed_mps = acc->distance_m / FOLLOWING_TIME_GAP_S;
}
