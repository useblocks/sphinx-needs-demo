/**
 * EU / motorcycle calibration profile - pseudo-code implementation
 *
 * Calibration profile: eu_motorcycle  (location = eu, vehicle type = motorcycle)
 * Build tags: sphinx-build -t eu -t motorcycle ...
 *
 * Holds the threshold values consumed by the shared Lane Keeping (SWREQ_002)
 * and Adaptive Cruise Control (SWREQ_005) modules for this location x type
 * combination. Only this file is traced for the matching build; its `impl`
 * needs link upward to SWREQ_002 and SWREQ_005. Every other profile traces its
 * own calibration file instead.
 *
 * This profile uses an earlier warning and a larger headway, as a leaning two-wheeler has less lateral margin.
 */

#include "lane_keeping.h"
#include "acc.h"

/* EU motorcycle calibration - resolved from the (location x type) combination. */
#define LANE_DEVIATION_WARN_THRESHOLD_M   0.25f   /* SWREQ_002 tuning: eu_motorcycle */
#define FOLLOWING_TIME_GAP_S              2.4f   /* SWREQ_005 tuning: eu_motorcycle */

// @ Lane deviation warning - EU motorcycle calibration (0.25 m), IMPL_LKA_DEVIATION_CAL_EU_MOTORCYCLE, impl, [SWREQ_002]
/**
 * Trigger the lane-departure warning once the lateral offset exceeds the
 * EU motorcycle threshold of 0.25 m without an active turn signal.
 */
int check_lane_deviation_eu_motorcycle(const LaneKeepingModule *lka, int turn_signal_active)
{
    if (turn_signal_active)
        return 0;
    return lka->lane_offset_m > LANE_DEVIATION_WARN_THRESHOLD_M;
}

// @ Speed control headway - EU motorcycle calibration (2.4 s), IMPL_ACC_SPEED_CAL_EU_MOTORCYCLE, impl, [SWREQ_005]
/**
 * Adjust the speed setpoint to maintain the EU motorcycle following time gap of
 * 2.4 s relative to the vehicle ahead.
 */
void adjust_speed_eu_motorcycle(AdaptiveCruiseModule *acc)
{
    acc->target_speed_mps = acc->distance_m / FOLLOWING_TIME_GAP_S;
}
