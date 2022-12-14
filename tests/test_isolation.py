import pytest


@pytest.fixture(scope="module", autouse=True)
def token(ERC20_Token_Sample, accounts):
    print(f'deploy '*3)
    t = accounts[0].deploy(ERC20_Token_Sample)
    yield t


@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass


def test_transfer(token, accounts):
    balance_before = token.balanceOf(accounts[0])
    token.transfer(accounts[1], 100, {'from': accounts[0]})
    assert balance_before - token.balanceOf(accounts[0]) == 100


def test_transfer2(token, accounts):
    balance_before = token.balanceOf(accounts[0])
    token.transfer(accounts[1], 100, {'from': accounts[0]})
    assert balance_before - token.balanceOf(accounts[0]) == 100


def test_transfer3(token, accounts):
    balance_before = token.balanceOf(accounts[0])
    token.transfer(accounts[1], 100, {'from': accounts[0]})
    assert balance_before - token.balanceOf(accounts[0]) == 100


def test_chain_reverted(token, accounts):
    assert token.balanceOf(accounts[0]) == 100_000_000_000 * 10**18
