# -*- coding: utf-8 -*-

from hbase.ttypes import TScan, TColumn
from common import connect

with connect() as client:
    table = 'tsdata'

    tscan = TScan(
        startRow='sys.cpu.user:20180421',
        stopRow='sys.cpu.user:20180422',
        columns=[TColumn('cf', '1015')]
    )

    for tresult in client.getScannerResults(table, tscan, 10):
        print(tresult)

    try:
        num_rows = 1
        scanner_id = client.openScanner(table, tscan)
        while True:
            tresults = client.getScannerRows(scanner_id, num_rows)
            for tresult in tresults:
                print(tresult)

            if len(tresults) < num_rows:
                break
    finally:
        client.closeScanner(scanner_id)
