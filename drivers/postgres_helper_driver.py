#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import os

from psycopg2_helper.bp import PostgresHelper


def test_api():

    CREATE_TABLE_DDL = """
        CREATE TABLE IF NOT EXISTS test_schema.test8 (
            id serial PRIMARY KEY, 
            num integer, 
            data varchar
        );
    """

    os.environ['POSTGRES_HOST'] = 'localhost'

    api = PostgresHelper()
    assert api

    table_ops = api.ddl()
    assert table_ops

    table_ops.create_schema('test_schema')

    table_ops.create_table(CREATE_TABLE_DDL)
    table_ops.get_table_names('test_schema') == ['test8']

    table_ops.delete_table(name='test8', schema='test_schema')
    table_ops.get_table_names('test_schema') == []

    table_ops.delete_schema('test_schema')

    api.close()
    del os.environ['POSTGRES_HOST']


def main():
    from drivers import IntegrationWrapper
    wrapper = IntegrationWrapper()

    wrapper.call(test_api)

    wrapper.deconstruct_env()


if __name__ == "__main__":
    main()
