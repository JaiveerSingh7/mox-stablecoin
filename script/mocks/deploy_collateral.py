from moccasin.boa_tools import VyperContract
from src.mocks import mock_token
def deploy_collateral() -> VyperContract:
    print("Deploying token...")
    return mock_token.deploy()

def moccasin_main():
    return deploy_collateral()