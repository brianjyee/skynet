#!/bin/bash
cat skynet/table_defs/skynet.sqlite3.sql | sqlite3 skynet.db
cat tests/fixtures/skynet.sql | sqlite3 skynet.db
