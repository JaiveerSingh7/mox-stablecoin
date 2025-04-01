from src import dsc_engine
import pytest
import boa
from eth.codecs.abi.exceptions import EncodeError
from tests.conftest import COLLATERAL_AMOUNT
from eth_utils import to_wei


def test_reverts_if_token_lengths_are_different(dsc,eth_usd,btc_usd,weth,wbtc):
    with pytest.raises(EncodeError):
        dsc_engine.deploy([wbtc,weth,weth],[eth_usd,btc_usd],dsc.address)

# ------------------------------------------------------------------
#                        DEPOSIT COLLATERAL
# ------------------------------------------------------------------
def test_reverts_if_collateral_zero(some_user,weth,dsce):
    with boa.env.prank(some_user):
        weth.approve(dsce, COLLATERAL_AMOUNT)
        with boa.reverts():
            dsce.deposit_collateral(weth,0)

# ------------------------------------------------------------------
#                          PRICE TESTS
# ------------------------------------------------------------------
def test_get_token_amount_from_usd(dsce, weth):
    expected_weth = to_wei(0.05, "ether")
    actual_weth = dsce.get_token_amount_from_usd(weth, to_wei(100, "ether"))
    assert expected_weth == actual_weth


def test_get_usd_value(dsce, weth):
    eth_amount = to_wei(15, "ether")
    expected_usd = to_wei(30_000, "ether")
    actual_usd = dsce.get_usd_value(weth, eth_amount)
    assert expected_usd == actual_usd


