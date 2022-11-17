#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import os

from psycopg2_helper.bp import PostgresHelper


def test_api():

    CREATE_TABLE_DDL = """
        CREATE TABLE test6 (
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
    # table_ops.delete_table(name='test', schema='test_schema')

    print(table_ops.get_table_names('test_schema'))
    table_ops.create_schema('test_schema')
    table_ops.create_table(CREATE_TABLE_DDL)
    print(table_ops.get_table_names('test_schema'))
    table_ops.delete_table(name='test6', schema='test_schema')

    table_ops.close()
    del os.environ['POSTGRES_HOST']


def main():
    from drivers import IntegrationWrapper
    wrapper = IntegrationWrapper()

    wrapper.call(test_api)

    wrapper.deconstruct_env()


if __name__ == "__main__":
    main()
