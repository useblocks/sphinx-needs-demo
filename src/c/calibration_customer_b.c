/**
 * Customer B calibration profile - pseudo-code implementation
 *
 * Build variant: customer_b (sphinx-build -t customer_b ...)
 *
 * Provides the Customer B threshold values consumed by the shared Lane Keeping
 * (SWREQ_002) and Adaptive Cruise Control (SWREQ_005) modules. Only this file is
 * traced when the customer_b build tag is active; its `impl` needs link upward
 * to SWREQ_002 and SWREQ_005 for that build.
 */

#include "lane_keeping.h"
#include "acc.h"

/* Customer B favours a later warning and a comfortable headway. */
#define LANE_DEVIATION_WARN_THRESHOLD_M   0.5f   /* SWREQ_002 tuning: customer_b */
#define FOLLOWING_TIME_GAP_S              2.2f   /* SWREQ_005 tuning: customer_b */

// @ Lane deviation warning - Customer B calibration (0.5 m), IMPL_LKA_DEVIATION_CAL_B, impl, [SWREQ_002]
/**
 * Trigger the lane-departure warning once the lateral offset exceeds the
 * Customer B threshold of 0.5 m without an active turn signal.
 */
int check_lane_deviation_customer_b(const LaneKeepingModule *lka, int turn_signal_active)
{
    if (turn_signal_active)
        return 0;
    return lka->lane_offset_m > LANE_DEVIATION_WARN_THRESHOLD_M;
}

// @ Speed control headway - Customer B calibration (2.2 s), IMPL_ACC_SPEED_CAL_B, impl, [SWREQ_005]
/**
 * Adjust the speed setpoint to maintain the Customer B following time gap of
 * 2.2 s relative to the vehicle ahead.
 */
void adjust_speed_customer_b(AdaptiveCruiseModule *acc)
{
    acc->target_speed_mps = acc->distance_m / FOLLOWING_TIME_GAP_S;
}
