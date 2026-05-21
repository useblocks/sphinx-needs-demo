"""
Teen car module.

.. impl:: Teen Car Module
   :id: TEEN_IMPL_CAR
   :implements: TEEN_DIST, TEEN_RADAR

   Overall implementation of all Teen Car specifications.
"""

import time


class TeenCar:
    """
    Our Teen car, called "TeenTrek".

    This class is the main entrance to all software functions.
    """

    def __init__(self, color):
        """
        Initiliases the teen car.

        @param color: HEX value of car. Example #FFCC00
        """
        self.color = color
        return

    def _drive(self, max_speed=100):
        """
        Drives the car with given max speed.


        :param max_speed: max speed in km/h. Example "120".
        """
        print("doing magic stuff")
        return

    def _get_position(self):
        """get the current position of the car"""

        position = "somewhere"
        return position

    def auto_drive(self, target, sleep=0.1):
        """
        .. impl:: Drive the passengers autonomously to the given target address.
           :id: TEEN_IMPL_RADAR
           :implements: TEEN_RADAR

        :param target: Adress of the target. Example: Mystreet, MyTown
        :param sleep: Sleep value in seconds. Used to "save ressources" ;)
        """

        target_reached = False
        while not target_reached:
            pos = self._get_position()
            if target == pos:
                target_reached = True
            self._drive()
            time.sleep(sleep)
