/**
 * Customer A calibration profile - pseudo-code implementation
 *
 * Build variant: customer_a (sphinx-build -t customer_a ...)
 *
 * Provides the Customer A threshold values consumed by the shared Lane Keeping
 * (SWREQ_002) and Adaptive Cruise Control (SWREQ_005) modules. SWREQ_002 and
 * SWREQ_005 link to the `impl` needs below only when the customer_a build tag
 * is active (variant-resolved `variant_impl` link).
 */

#include "lane_keeping.h"
#include "acc.h"

/* Customer A favours an early lane-departure warning and a sporty headway. */
#define LANE_DEVIATION_WARN_THRESHOLD_M   0.3f   /* SWREQ_002 tuning: customer_a */
#define FOLLOWING_TIME_GAP_S              1.8f   /* SWREQ_005 tuning: customer_a */

// @ Lane deviation warning - Customer A calibration (0.3 m), IMPL_LKA_DEVIATION_CAL_A, impl, [SWREQ_002]
/**
 * Trigger the lane-departure warning as soon as the lateral offset exceeds the
 * Customer A threshold of 0.3 m without an active turn signal.
 */
int check_lane_deviation_customer_a(const LaneKeepingModule *lka, int turn_signal_active)
{
    if (turn_signal_active)
        return 0;
    return lka->lane_offset_m > LANE_DEVIATION_WARN_THRESHOLD_M;
}

// @ Speed control headway - Customer A calibration (1.8 s), IMPL_ACC_SPEED_CAL_A, impl, [SWREQ_005]
/**
 * Adjust the speed setpoint to maintain the Customer A following time gap of
 * 1.8 s relative to the vehicle ahead.
 */
void adjust_speed_customer_a(AdaptiveCruiseModule *acc)
{
    acc->target_speed_mps = acc->distance_m / FOLLOWING_TIME_GAP_S;
}
