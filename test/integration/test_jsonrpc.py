import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

# from dashd import DashDaemon
# from dash_config import DashConfig
from advantaged import AdvantageDaemon
from advantage_config import AdvantageConfig


# def test_dashd():
def test_advantaged():
    # config_text = DashConfig.slurp_config_file(config.dash_conf)
    config_text = AdvantageConfig.slurp_config_file(config.advantage_conf)
    print(config_text)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'00004cd62c655e1492e4d87736f23fdd6ad260980007b72bc33373aed2b79258'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'00608a61e6795d83dd3ec9db646bd9658f4f51e64addfecd5684ea83c8bd63c7'
            # 0x0575f78ee8dc057deee78ef691876e3be29833aaee5e189bb0459c087451305a
    # creds = DashConfig.get_rpc_creds(config_text, network)
    # dashd = DashDaemon(**creds)
    # assert dashd.rpc_command is not None
    creds = AdvantageConfig.get_rpc_creds(config_text, network)
    advantaged = AdvantageDaemon(**creds)
    assert advantaged.rpc_command is not None
    
    assert hasattr(advantaged, 'rpc_connection')

    # Advantage testnet block 0 hash ==00608a61e6795d83dd3ec9db646bd9658f4f51e64addfecd5684ea83c8bd63c7 
    # test commands without arguments
    # info = dashd.rpc_command('getinfo')
#    info = advantaged.rpc_command('getinfo')
   # info_keys = [
#       'version',
 #      'protocolversion',
  #      'walletversion',
   #     'balance',
    #    'blocks',
     #   'timeoffset',
     #   'connections',
      #  'proxy',
       # 'difficulty',
        #'testnet',
     #   'keypoololdest',
      #  'keypoolsize',
      #  'paytxfee',
      #  'relayfee',
      #  'errors',
  #  ]
   # for key in info_keys:
    #    assert key in info
  #  assert info['testnet'] is is_testnet

    # test commands with args
    # assert dashd.rpc_command('getblockhash', 0) == genesis_hash
   # assert advantaged.rpc_command('getblockhash', 0) == genesis_hash
