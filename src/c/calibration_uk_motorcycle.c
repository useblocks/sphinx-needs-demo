/**
 * UK / motorcycle calibration profile - pseudo-code implementation
 *
 * Calibration profile: uk_motorcycle  (location = uk, vehicle type = motorcycle)
 * Build tags: sphinx-build -t uk -t motorcycle ...
 *
 * Holds the threshold values consumed by the shared Lane Keeping (SWREQ_002)
 * and Adaptive Cruise Control (SWREQ_005) modules for this location x type
 * combination. Only this file is traced for the matching build; its `impl`
 * needs link upward to SWREQ_002 and SWREQ_005. Every other profile traces its
 * own calibration file instead.
 *
 * This profile uses the earliest warning of all profiles and a larger motorcycle headway.
 */

#include "lane_keeping.h"
#include "acc.h"

/* UK motorcycle calibration - resolved from the (location x type) combination. */
#define LANE_DEVIATION_WARN_THRESHOLD_M   0.20f   /* SWREQ_002 tuning: uk_motorcycle */
#define FOLLOWING_TIME_GAP_S              2.2f   /* SWREQ_005 tuning: uk_motorcycle */

// @ Lane deviation warning - UK motorcycle calibration (0.20 m), IMPL_LKA_DEVIATION_CAL_UK_MOTORCYCLE, impl, [SWREQ_002]
/**
 * Trigger the lane-departure warning once the lateral offset exceeds the
 * UK motorcycle threshold of 0.20 m without an active turn signal.
 */
int check_lane_deviation_uk_motorcycle(const LaneKeepingModule *lka, int turn_signal_active)
{
    if (turn_signal_active)
        return 0;
    return lka->lane_offset_m > LANE_DEVIATION_WARN_THRESHOLD_M;
}

// @ Speed control headway - UK motorcycle calibration (2.2 s), IMPL_ACC_SPEED_CAL_UK_MOTORCYCLE, impl, [SWREQ_005]
/**
 * Adjust the speed setpoint to maintain the UK motorcycle following time gap of
 * 2.2 s relative to the vehicle ahead.
 */
void adjust_speed_uk_motorcycle(AdaptiveCruiseModule *acc)
{
    acc->target_speed_mps = acc->distance_m / FOLLOWING_TIME_GAP_S;
}
