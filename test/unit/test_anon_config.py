import pytest
import os
import sys
import re
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
os.environ['SENTINEL_ENV'] = 'test'
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), '../../lib')))
import config
# from dash_config import DashConfig
from advantage_config import AdvantageConfig


@pytest.fixture
# def dash_conf(**kwargs):
def advantage_conf(**kwargs):
    defaults = {
        # 'rpcuser': 'dashrpc',
        'rpcuser': 'advantagerpc',
        'rpcpassword': 'EwJeV3fZTyTVozdECF627BkBMnNDwQaVLakG3A4wXYyk',
        'rpcport': 29241,
    }

    # merge kwargs into defaults
    for (key, value) in kwargs.items():
        defaults[key] = value

    conf = """# basic settings
testnet=1 # TESTNET
server=1
rpcuser={rpcuser}
rpcpassword={rpcpassword}
rpcallowip=127.0.0.1
rpcport={rpcport}
""".format(**defaults)

    return conf


def test_get_rpc_creds():
    # dash_config = dash_conf()
    advantage_config = advantage_conf()
    # creds = DashConfig.get_rpc_creds(dash_config, 'testnet')
    creds = AdvantageConfig.get_rpc_creds(advantage_config, 'testnet')

    for key in ('user', 'password', 'port'):
        assert key in creds
    assert creds.get('user') == 'advantagerpc'
    assert creds.get('password') == 'EwJeV3fZTyTVozdECF627BkBMnNDwQaVLakG3A4wXYyk'
    assert creds.get('port') == 29241

    # dash_config = dash_conf(rpcpassword='s00pers33kr1t', rpcport=8000)
    advantage_config = advantage_conf(rpcpassword='s00pers33kr1t', rpcport=12345)
    # creds = DashConfig.get_rpc_creds(dash_config, 'testnet')
    creds = AdvantageConfig.get_rpc_creds(advantage_config, 'testnet')

    for key in ('user', 'password', 'port'):
        assert key in creds
    assert creds.get('user') == 'advantagerpc'
    assert creds.get('password') == 's00pers33kr1t'
    assert creds.get('port') == 12345

    no_port_specified = re.sub('\nrpcport=.*?\n', '\n', advantage_conf(), re.M)
    # creds = DashConfig.get_rpc_creds(no_port_specified, 'testnet')
    creds = AdvantageConfig.get_rpc_creds(no_port_specified, 'testnet')

    for key in ('user', 'password', 'port'):
        assert key in creds
    assert creds.get('user') == 'advantagerpc'
    assert creds.get('password') == 'EwJeV3fZTyTVozdECF627BkBMnNDwQaVLakG3A4wXYyk'
    assert creds.get('port') == 33129


# ensure advantage network (mainnet, testnet) matches that specified in config
# requires running advantaged on whatever port specified...
#
# This is more of a advantaged/jsonrpc test than a config test...
