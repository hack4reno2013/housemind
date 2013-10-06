# -*- coding: utf-8 -*-

# Connection parameters
CONN_STRING = "postgresql://postgres:gotest@localhost/"
DB_NAME = "housemind"
DB_STRING = CONN_STRING + DB_NAME

# Filesystem settings
import os
CUR_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))