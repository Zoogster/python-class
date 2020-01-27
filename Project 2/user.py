"""Base class for Student and Admin.

User -- The base class of Student and Admin.
get_id -- Gets ID of current user.
get_pin -- Gets PIN of current user.
"""


class User:
    def __init__(self, id, pin):
        self._id = id
        self._pin = pin

    def get_id(self):
        """Gets ID of current user.

        Returns self._id.
        """
        return self._id

    def get_pin(self):
        """Gets PIN of current user.

        Returns self._pin.
        """
        return self._pin
