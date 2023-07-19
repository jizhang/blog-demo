# -*- coding: utf-8 -*-

from hbase.ttypes import TPut, TColumnValue, TGet, TDelete, TColumn
from common import connect

with connect() as client:
    table = 'tsdata'
    row = 'sys.cpu.user:20180421:192.168.1.1'

    # put
    put_columns = [
        TColumnValue('cf', '1015', '0.28'),
        TColumnValue('cf', '1016', '0.35'),
        TColumnValue('cf', '1017', '0.25'),
    ]
    tput = TPut(row, put_columns)
    client.put(table, tput)

    # get all columns
    tget = TGet(row)
    tresult = client.get(table, tget)
    print(tresult)

    # delete
    delete_columns = [
        TColumn('cf', '1015'),
    ]
    tdelete = TDelete(row, delete_columns)
    client.deleteSingle(table, tdelete)

    # get specific columns
    get_columns = [
        TColumn('cf', '1015'),
        TColumn('cf', '1016'),
    ]
    tget = TGet(row, get_columns)
    tresult = client.get(table, tget)
    print(tresult)
