/**
 * Turn Signal Priority - left-hand drive variant
 *
 * Covers SWREQ_028
 *
 * This file is only traced in builds with vehicle.steering_side == "left"
 * (variants eu_left and america). Right-hand drive builds do not load it.
 */

#include "turn_signal.h"

// @ signal_overtake_lhd, IMPL_TS_LHD, impl, [SWREQ_028]
/**
 * On left-hand drive vehicles overtaking happens across the right lane,
 * so the right-side mirror zone must be confirmed clear before the turn
 * signal arms an overtaking maneuver.
 */
int signal_overtake_lhd(int signal_requested, int right_mirror_clear)
{
    /* stub: gate the overtake signal on the right-side mirror check */
    return signal_requested && right_mirror_clear;
}
