#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import os
from functools import partial

from psycopg2_helper.bp import PostgresHelper


def test_api():

    schema_name = "test_schema"
    table_name = "test21"

    CREATE_TABLE_DDL = """
        CREATE TABLE IF NOT EXISTS schemaname.tablename (
            source_user varchar(32), 
            target_user varchar(32),
            thread_ts varchar(32),
            channel varchar(32)            
        );
    """

    CREATE_TABLE_DDL = CREATE_TABLE_DDL.replace('schemaname', schema_name)
    CREATE_TABLE_DDL = CREATE_TABLE_DDL.replace('tablename', table_name)

    os.environ['POSTGRES_HOST'] = 'localhost'

    api = PostgresHelper()
    assert api

    table_ops = api.ddl()
    assert table_ops

    crud_ops = api.crud()
    assert crud_ops

    table_ops.create_schema(schema_name)

    table_ops.create_table(CREATE_TABLE_DDL)
    assert table_ops.get_table_names(schema_name) == [table_name]

    insert_data = partial(
        crud_ops.insert,
        schema_name=schema_name,
        table_name=table_name,
        column_names=[
            'source_user',
            'target_user',
            'thread_ts',
            'channel'
        ])

    for i in range(0, 100):
        insert_data(column_values=["iceberg", "student",
                    "12323233.2323", "test-23020202"])

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
