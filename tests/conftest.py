import pytest
from moccasin.config import get_active_network
from script.deploy_dsc_engine import deploy_dsc_engine
from eth_account import Account
import boa
from eth_utils import to_wei

BALANCE = to_wei(10,"ether")
COLLATERAL_AMOUNT = to_wei(10,"ether")
# ------------------------------------------------------------------
#                          SESSION SCOPED
# ------------------------------------------------------------------
@pytest.fixture(scope="session")
def active_network():
    return get_active_network()

@pytest.fixture(scope="session")
def weth (active_network):
    return active_network.manifest_named("weth")


@pytest.fixture(scope="session")
def wbtc (active_network):
    return active_network.manifest_named("wbtc")

@pytest.fixture(scope="session")
def eth_usd (active_network):
    return active_network.manifest_named("eth_usd_price_feed")
@pytest.fixture(scope="session")

def btc_usd (active_network):
    return active_network.manifest_named("btc_usd_price_feed")

# ------------------------------------------------------------------
#                         FUNCTION SCOPED
# ------------------------------------------------------------------

@pytest.fixture
def dsc(active_network):
    return active_network.manifest_named("decentralized_stable_coin")

@pytest.fixture
def dsce(dsc,weth,wbtc,eth_usd,btc_usd):
    return deploy_dsc_engine(dsc)

@pytest.fixture
def some_user(weth,wbtc):
    entropy=13
    account=Account.create(entropy)
    boa.env.set_balance(account.address, BALANCE)
    with boa.env.prank(account.address):
        weth.mock_mint()
        wbtc.mock_mint()
    return account.address