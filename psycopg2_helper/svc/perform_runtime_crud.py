#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Common Runtime CRUD Operations """


from typing import List
from typing import Optional

from psycopg2 import connect
from psycopg2.extensions import connection

from baseblock import BaseObject


class PerformTableOperations(BaseObject):
    """ Perform Common Runtime CRUD Operations """

    def __init__(self,
                 conn: connection):
        """ Change Log

        Created:
            16-Nov-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)
        self.conn = conn
