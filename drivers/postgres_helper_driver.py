#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import os
from psycopg2 import sql

from psycopg2_helper.bp import PostgresHelper


def test_api():

    CREATE_TABLE_DDL = """
        CREATE TABLE IF NOT EXISTS test_schema.test10 (
            num1 integer, 
            num2 integer
        );
    """

    os.environ['POSTGRES_HOST'] = 'localhost'

    api = PostgresHelper()
    assert api

    table_ops = api.ddl()
    assert table_ops

    crud_ops = api.crud()
    assert crud_ops

    schema_name = "test_schema"
    table_name = "test10"

    table_ops.create_schema(schema_name)

    table_ops.create_table(CREATE_TABLE_DDL)
    table_ops.get_table_names(schema_name) == ['test10']

    for i in range(0, 100):
        crud_ops.insert(schema_name=schema_name,
                        table_name=table_name,
                        values=[i, i + 100])

    print(crud_ops.read(f"SELECT * FROM {schema_name}.{table_name}"))

    for table_name in table_ops.get_table_names(schema_name):
        table_ops.delete_table(name=table_name, schema=schema_name)

    table_ops.get_table_names(schema_name) == []
    table_ops.delete_schema(schema_name)

    api.close()
    del os.environ['POSTGRES_HOST']


def main():
    from drivers import IntegrationWrapper
    wrapper = IntegrationWrapper()

    wrapper.call(test_api)

    wrapper.deconstruct_env()


if __name__ == "__main__":
    main()
