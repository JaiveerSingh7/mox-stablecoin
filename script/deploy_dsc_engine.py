from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network
from src import dsc_engine

def deploy_dsc_engine(dsc: VyperContract) -> VyperContract:
    active_network = get_active_network()

    btc_usd = active_network.manifest_named("btc_usd_price_feed")
    eth_usd = active_network.manifest_named("eth_usd_price_feed")
    weth = active_network.manifest_named("weth")
    wbtc = active_network.manifest_named("wbtc")
    price_feed=[btc_usd.address,eth_usd.address]
    tokens=[wbtc.address,weth.address]
    dsc_engine_contract = dsc_engine.deploy(tokens,price_feed,dsc)

    dsc.set_minter(dsc_engine_contract.address, True)
    dsc.transfer_ownership(dsc_engine_contract)
    print(f"DSC Engine deployed at {dsc_engine_contract.address}")
    return dsc_engine_contract

def moccasin_main()->VyperContract:
    active_network = get_active_network()
    dsc= active_network.manifest_named("decentralized_stable_coin")
    return deploy_dsc_engine(dsc)