import os

import pymysql
from ssqaapitest.src.utilities.credentialsUtility import CredentialsUtility
from ssqaapitest.src.configs.hosts_config import DB_HOST
import logging as logger


class DBUtility(object):

    def __init__(self):
        creds = CredentialsUtility()
        self.creds = creds.get_db_credentials()

        self.machine = os.environ.get('MACHINE')
        assert self.machine, f"Environment variable 'MACHINE' must be set"

        self.env = os.environ.get('ENV', 'test')

        self.host = DB_HOST[self.machine][self.env]['host']
        self.port = DB_HOST[self.machine][self.env]['port']
        self.database = DB_HOST[self.machine][self.env]['database']
        self.table_prefix = DB_HOST[self.machine][self.env]['table_prefix']

    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.creds['db_user'],
                                     password=self.creds['db_password'], port=8889)
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()

        try:
            logger.debug(f"Executing: {sql}")
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n Error:{str(e)}")
        finally:
            conn.close()

        return rs_dict


    def execute_sql(self, sql):
        pass
