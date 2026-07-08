/**
 * ASIA / combi calibration profile - pseudo-code implementation
 *
 * Calibration profile: asia_combi  (location = asia, vehicle type = combi)
 * Build tags: sphinx-build -t asia -t combi ...
 *
 * Holds the threshold values consumed by the shared Lane Keeping (SWREQ_002)
 * and Adaptive Cruise Control (SWREQ_005) modules for this location x type
 * combination. Only this file is traced for the matching build; its `impl`
 * needs link upward to SWREQ_002 and SWREQ_005. Every other profile traces its
 * own calibration file instead.
 *
 * This profile uses a later warning and a comfort-oriented headway.
 */

#include "lane_keeping.h"
#include "acc.h"

/* ASIA combi calibration - resolved from the (location x type) combination. */
#define LANE_DEVIATION_WARN_THRESHOLD_M   0.50f   /* SWREQ_002 tuning: asia_combi */
#define FOLLOWING_TIME_GAP_S              2.2f   /* SWREQ_005 tuning: asia_combi */

// @ Lane deviation warning - ASIA combi calibration (0.50 m), IMPL_LKA_DEVIATION_CAL_ASIA_COMBI, impl, [SWREQ_002]
/**
 * Trigger the lane-departure warning once the lateral offset exceeds the
 * ASIA combi threshold of 0.50 m without an active turn signal.
 */
int check_lane_deviation_asia_combi(const LaneKeepingModule *lka, int turn_signal_active)
{
    if (turn_signal_active)
        return 0;
    return lka->lane_offset_m > LANE_DEVIATION_WARN_THRESHOLD_M;
}

// @ Speed control headway - ASIA combi calibration (2.2 s), IMPL_ACC_SPEED_CAL_ASIA_COMBI, impl, [SWREQ_005]
/**
 * Adjust the speed setpoint to maintain the ASIA combi following time gap of
 * 2.2 s relative to the vehicle ahead.
 */
void adjust_speed_asia_combi(AdaptiveCruiseModule *acc)
{
    acc->target_speed_mps = acc->distance_m / FOLLOWING_TIME_GAP_S;
}
