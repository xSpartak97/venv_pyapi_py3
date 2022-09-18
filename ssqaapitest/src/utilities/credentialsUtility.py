import os


class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():
        os.environ['wc_key'] = 'ck_c0f44eb9487cbc8332097277f2925b76621743e1'
        os.environ['wc_secret'] = 'cs_f30496fde4076be29b4f7d11404bf06a82f1908f'
        wc_key = os.environ.get('wc_key')
        wc_secret = os.environ.get('wc_secret')

        if not wc_key or not wc_secret:
            raise Exception("The API credentials 'WC_KEY' and 'WC_SECRET' must be in env variable.")
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}


    @staticmethod
    def get_db_credentials():
        os.environ['MACHINE'] = 'machine1'
        os.environ['DB_USER'] = 'root'
        os.environ['DB_PASSWORD'] = 'root'
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception("The DB credentials 'DB_USER' and 'DB_PASSWORD' must be in env variable.")
        else:
            return {'db_user': db_user, 'db_password': db_password}