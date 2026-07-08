/**
 * ASIA / motorcycle calibration profile - pseudo-code implementation
 *
 * Calibration profile: asia_motorcycle  (location = asia, vehicle type = motorcycle)
 * Build tags: sphinx-build -t asia -t motorcycle ...
 *
 * Holds the threshold values consumed by the shared Lane Keeping (SWREQ_002)
 * and Adaptive Cruise Control (SWREQ_005) modules for this location x type
 * combination. Only this file is traced for the matching build; its `impl`
 * needs link upward to SWREQ_002 and SWREQ_005. Every other profile traces its
 * own calibration file instead.
 *
 * This profile uses a mid-range warning and the largest headway of all profiles.
 */

#include "lane_keeping.h"
#include "acc.h"

/* ASIA motorcycle calibration - resolved from the (location x type) combination. */
#define LANE_DEVIATION_WARN_THRESHOLD_M   0.35f   /* SWREQ_002 tuning: asia_motorcycle */
#define FOLLOWING_TIME_GAP_S              2.6f   /* SWREQ_005 tuning: asia_motorcycle */

// @ Lane deviation warning - ASIA motorcycle calibration (0.35 m), IMPL_LKA_DEVIATION_CAL_ASIA_MOTORCYCLE, impl, [SWREQ_002]
/**
 * Trigger the lane-departure warning once the lateral offset exceeds the
 * ASIA motorcycle threshold of 0.35 m without an active turn signal.
 */
int check_lane_deviation_asia_motorcycle(const LaneKeepingModule *lka, int turn_signal_active)
{
    if (turn_signal_active)
        return 0;
    return lka->lane_offset_m > LANE_DEVIATION_WARN_THRESHOLD_M;
}

// @ Speed control headway - ASIA motorcycle calibration (2.6 s), IMPL_ACC_SPEED_CAL_ASIA_MOTORCYCLE, impl, [SWREQ_005]
/**
 * Adjust the speed setpoint to maintain the ASIA motorcycle following time gap of
 * 2.6 s relative to the vehicle ahead.
 */
void adjust_speed_asia_motorcycle(AdaptiveCruiseModule *acc)
{
    acc->target_speed_mps = acc->distance_m / FOLLOWING_TIME_GAP_S;
}
