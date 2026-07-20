/**
 * Turn Signal Priority - right-hand drive variant
 *
 * Covers SWREQ_029
 *
 * This file is only traced in builds with vehicle.steering_side == "right"
 * (variant eu_right). Left-hand drive builds do not load it.
 */

#include "turn_signal.h"

// @ signal_overtake_rhd, IMPL_TS_RHD, impl, [SWREQ_029]
/**
 * On right-hand drive vehicles overtaking happens across the left lane,
 * so the left-side mirror zone must be confirmed clear before the turn
 * signal arms an overtaking maneuver.
 */
int signal_overtake_rhd(int signal_requested, int left_mirror_clear)
{
    /* stub: gate the overtake signal on the left-side mirror check */
    return signal_requested && left_mirror_clear;
}
