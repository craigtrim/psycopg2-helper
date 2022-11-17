#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Postgres Helper API """


from baseblock import BaseObject

from psycopg2_helper.dmo import PostgresConnector
from psycopg2_helper.svc import PerformTableOperations


class PostgresHelper(BaseObject):
    """ Postgres Helper API """

    def __init__(self):
        """ Change Log

        Created:
            16-Nov-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)
        self._dmo_connector = PostgresConnector()
        self.conn = self._dmo_connector.conn

    def close(self) -> None:
        self._dmo_connector.close()

    def ddl(self) -> PerformTableOperations:
        return PerformTableOperations(self.conn)
