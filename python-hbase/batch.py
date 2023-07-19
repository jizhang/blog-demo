# -*- coding: utf-8 -*-

from hbase.ttypes import TPut, TColumnValue, TGet, TDelete, TColumn
from common import connect

with connect() as client:
    table = 'tsdata'

    # put multiple
    tputs = [
        TPut(
            'sys.cpu.user:20180421:192.168.1.1',
            [
                TColumnValue('cf', '1015', '0.28'),
                TColumnValue('cf', '1016', '0.35'),
                TColumnValue('cf', '1017', '0.25'),
            ]
        ),
        TPut(
            'sys.cpu.user:20180421:192.168.1.2',
            [
                TColumnValue('cf', '1015', '0.45'),
                TColumnValue('cf', '1016', '0.32'),
                TColumnValue('cf', '1017', '0.58'),
            ]
        ),
    ]

    client.putMultiple(table, tputs)

    # get multiple
    tgets = [
        TGet(
            'sys.cpu.user:20180421:192.168.1.1',
            [TColumn('cf', '1015')]
        ),
        TGet(
            'sys.cpu.user:20180421:192.168.1.2',
            [TColumn('cf', '1015')]
        )
    ]
    for tresult in client.getMultiple(table, tgets):
        print(tresult)
