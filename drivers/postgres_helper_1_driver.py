#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import os
from functools import partial
from psycopg2_helper.bp import PostgresHelper


def test_api():

    schema_name = 'test_schema'
    table_name = 'test10'

    CREATE_TABLE_DDL = """
        CREATE TABLE IF NOT EXISTS schemaname.tablename (
            num1 integer,
            num2 integer
        );
    """

    CREATE_TABLE_DDL = CREATE_TABLE_DDL.replace('schemaname', schema_name)
    CREATE_TABLE_DDL = CREATE_TABLE_DDL.replace('tablename', table_name)

    os.environ['POSTGRES_HOST'] = 'localhost'

    api = PostgresHelper()
    assert api

    assert api.ddl
    assert api.crud

    api.ddl.create_schema(schema_name)

    api.ddl.create_table(CREATE_TABLE_DDL)
    assert table_name in api.ddl.get_table_names(schema_name)

    insert_data = partial(
        api.crud.insert,
        schema_name=schema_name,
        table_name=table_name,
        column_names=[
            'num1',
            'num2'
        ])

    for i in range(0, 100):
        insert_data(column_values=[i, i + 100])

    print(api.crud.read(f'SELECT * FROM {schema_name}.{table_name}'))

    for table_name in api.ddl.get_table_names(schema_name):
        api.ddl.delete_table(name=table_name, schema=schema_name)

    api.ddl.get_table_names(schema_name) == []
    api.ddl.delete_schema(schema_name)

    api.close()
    del os.environ['POSTGRES_HOST']


def main():
    from drivers import IntegrationWrapper
    wrapper = IntegrationWrapper()

    wrapper.call(test_api)

    wrapper.deconstruct_env()


if __name__ == '__main__':
    main()
