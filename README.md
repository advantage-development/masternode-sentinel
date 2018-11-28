[![](https://img.shields.io/badge/latest%20version-v1.1.2-green.svg)](https://github.com/advantageymousbitcoin/sentinel/releases/tag/v1.1.2)


# ADVANTAGE Sentinel

An all-powerful toolset for ADVANTAGE.


Sentinel is an autonomous agent for persisting, processing and automating ADVANTAGE governance objects and tasks.

Sentinel is implemented as a Python application that binds to a local version advantaged instance on each ADVANTAGE Masternode.

This guide covers installing Sentinel onto an existing 12.1 Masternode in Ubuntu 14.04 / 16.04 / 18.04.

## Quick Setup Script

### 1. For a quick install, run this install script

```
chmod 777 setup.sh
./setup.sh
```

## Full Installation

### 1. Install Prerequisites

Make sure Python version 2.7.x or above is installed:

```
python --version
```

Update system packages and ensure virtualenv is installed:

```
sudo apt-get update
sudo apt-get -y install python-virtualenv
sudo apt-get install virtualenv
```
Make sure the local ADVANTAGE daemon running is at least version X (X)

```
advantage-cli getinfo | grep version
```

### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

```
git clone https://github.com/advantageymousbitcoin/sentinel.git 
cd sentinel
virtualenv ./venv
./venv/bin/pip install -r requirements.txt
```

### 3. Set up Cron

Set up a crontab entry to call Sentinel every minute:

```
crontab -e
```

In the crontab editor, add the lines below, replacing '/home/YOURUSERNAME/sentinel' to the path where you cloned sentinel to:

**PLEASE NOTE**: The following will only work if you are signed in as **NON-ROOT** user. You can check it by using "whoami" command.

```    
* * * * * cd /home/YOURUSERNAME/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1
```

**IF** you are a **ROOT**, user type the following:

```   
* * * * * cd /root/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1
```

### 4. Test the Configuration

Test the config by runnings all tests from the sentinel folder you cloned into

```
./venv/bin/py.test ./test
```

With all tests passing and crontab setup, Sentinel will stay in sync with advantaged and the installation is complete

## Configuration

An alternative (non-default) path to the `advantage.conf` file can be specified in `sentinel.conf`:

```
advantage_conf=/path/to/advantage.conf
```

If you want to use Sentinel on ADVANTAGE TESTNET, you need to add the following in `sentinel.conf`:

```    
#network=mainnet
network=testnet
```

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

```
SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py
```


### License

Released under the MIT license, under the same terms as ADVANTAGECore itself. See [LICENSE](LICENSE) for more info.

### Credits to Dash Core
