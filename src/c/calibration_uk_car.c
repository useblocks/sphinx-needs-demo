/**
 * UK / passenger car (combi / cabrio) calibration profile - pseudo-code implementation
 *
 * Calibration profile: uk_car  (location = uk, vehicle type = passenger car (combi / cabrio))
 * Build tags: sphinx-build -t uk -t combi   (or -t uk -t cabrio) ...
 *
 * Holds the threshold values consumed by the shared Lane Keeping (SWREQ_002)
 * and Adaptive Cruise Control (SWREQ_005) modules for this location x type
 * combination. Only this file is traced for the matching build; its `impl`
 * needs link upward to SWREQ_002 and SWREQ_005. Every other profile traces its
 * own calibration file instead.
 *
 * This profile uses an earlier warning and a sportier headway than the EU reference.
 */

#include "lane_keeping.h"
#include "acc.h"

/* UK passenger car (combi / cabrio) calibration - resolved from the (location x type) combination. */
#define LANE_DEVIATION_WARN_THRESHOLD_M   0.30f   /* SWREQ_002 tuning: uk_car */
#define FOLLOWING_TIME_GAP_S              1.8f   /* SWREQ_005 tuning: uk_car */

// @ Lane deviation warning - UK passenger car (combi / cabrio) calibration (0.30 m), IMPL_LKA_DEVIATION_CAL_UK_CAR, impl, [SWREQ_002]
/**
 * Trigger the lane-departure warning once the lateral offset exceeds the
 * UK passenger car (combi / cabrio) threshold of 0.30 m without an active turn signal.
 */
int check_lane_deviation_uk_car(const LaneKeepingModule *lka, int turn_signal_active)
{
    if (turn_signal_active)
        return 0;
    return lka->lane_offset_m > LANE_DEVIATION_WARN_THRESHOLD_M;
}

// @ Speed control headway - UK passenger car (combi / cabrio) calibration (1.8 s), IMPL_ACC_SPEED_CAL_UK_CAR, impl, [SWREQ_005]
/**
 * Adjust the speed setpoint to maintain the UK passenger car (combi / cabrio) following time gap of
 * 1.8 s relative to the vehicle ahead.
 */
void adjust_speed_uk_car(AdaptiveCruiseModule *acc)
{
    acc->target_speed_mps = acc->distance_m / FOLLOWING_TIME_GAP_S;
}
