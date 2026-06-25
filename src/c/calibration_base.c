/**
 * Default calibration profile - pseudo-code implementation
 *
 * Build variant: base (untagged build, no -t customer_* flag)
 *
 * Holds the baseline threshold values consumed by the shared Lane Keeping
 * (SWREQ_002) and Adaptive Cruise Control (SWREQ_005) modules. Only this file is
 * traced for an untagged (base) build; its `impl` needs link upward to SWREQ_002
 * and SWREQ_005. Customer builds trace their own calibration file instead.
 */

#include "lane_keeping.h"
#include "acc.h"

/* Baseline calibration - used whenever no customer build tag is active. */
#define LANE_DEVIATION_WARN_THRESHOLD_M   0.4f   /* SWREQ_002 tuning: base */
#define FOLLOWING_TIME_GAP_S              2.0f   /* SWREQ_005 tuning: base */

// @ Lane deviation warning - base calibration (0.4 m), IMPL_LKA_DEVIATION_CAL_BASE, impl, [SWREQ_002]
/**
 * Trigger the lane-departure warning once the lateral offset exceeds the
 * baseline threshold of 0.4 m without an active turn signal.
 */
int check_lane_deviation_base(const LaneKeepingModule *lka, int turn_signal_active)
{
    if (turn_signal_active)
        return 0;
    return lka->lane_offset_m > LANE_DEVIATION_WARN_THRESHOLD_M;
}

// @ Speed control headway - base calibration (2.0 s), IMPL_ACC_SPEED_CAL_BASE, impl, [SWREQ_005]
/**
 * Adjust the speed setpoint to maintain the baseline following time gap of
 * 2.0 s relative to the vehicle ahead.
 */
void adjust_speed_base(AdaptiveCruiseModule *acc)
{
    acc->target_speed_mps = acc->distance_m / FOLLOWING_TIME_GAP_S;
}
