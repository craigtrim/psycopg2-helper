#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from psycopg2_helper.dmo import PostgresConnector


def test_connection_1():

    dmo = PostgresConnector(database_name='postgres', host='localhost')
    assert dmo.conn


def main():
    from drivers import IntegrationWrapper
    wrapper = IntegrationWrapper()

    wrapper.call(test_connection_1)

    wrapper.deconstruct_env()


if __name__ == '__main__':
    main()
