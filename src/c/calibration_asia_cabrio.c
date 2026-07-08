/**
 * ASIA / cabrio calibration profile - pseudo-code implementation
 *
 * Calibration profile: asia_cabrio  (location = asia, vehicle type = cabrio)
 * Build tags: sphinx-build -t asia -t cabrio ...
 *
 * Holds the threshold values consumed by the shared Lane Keeping (SWREQ_002)
 * and Adaptive Cruise Control (SWREQ_005) modules for this location x type
 * combination. Only this file is traced for the matching build; its `impl`
 * needs link upward to SWREQ_002 and SWREQ_005. Every other profile traces its
 * own calibration file instead.
 *
 * This profile uses the latest warning (open-top wind buffeting tolerated) with a comfort headway.
 */

#include "lane_keeping.h"
#include "acc.h"

/* ASIA cabrio calibration - resolved from the (location x type) combination. */
#define LANE_DEVIATION_WARN_THRESHOLD_M   0.55f   /* SWREQ_002 tuning: asia_cabrio */
#define FOLLOWING_TIME_GAP_S              2.1f   /* SWREQ_005 tuning: asia_cabrio */

// @ Lane deviation warning - ASIA cabrio calibration (0.55 m), IMPL_LKA_DEVIATION_CAL_ASIA_CABRIO, impl, [SWREQ_002]
/**
 * Trigger the lane-departure warning once the lateral offset exceeds the
 * ASIA cabrio threshold of 0.55 m without an active turn signal.
 */
int check_lane_deviation_asia_cabrio(const LaneKeepingModule *lka, int turn_signal_active)
{
    if (turn_signal_active)
        return 0;
    return lka->lane_offset_m > LANE_DEVIATION_WARN_THRESHOLD_M;
}

// @ Speed control headway - ASIA cabrio calibration (2.1 s), IMPL_ACC_SPEED_CAL_ASIA_CABRIO, impl, [SWREQ_005]
/**
 * Adjust the speed setpoint to maintain the ASIA cabrio following time gap of
 * 2.1 s relative to the vehicle ahead.
 */
void adjust_speed_asia_cabrio(AdaptiveCruiseModule *acc)
{
    acc->target_speed_mps = acc->distance_m / FOLLOWING_TIME_GAP_S;
}
