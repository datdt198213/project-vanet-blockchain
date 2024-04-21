#!/usr/bin/env python3
#
# Copyright Soramitsu Co., Ltd. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
#


# Here are Iroha dependencies.
# Python library generally consists of 3 parts:
# Iroha, IrohaCrypto and IrohaGrpc which we need to import:
import os
import binascii
from iroha import IrohaCrypto
from iroha import Iroha, IrohaGrpc
from iroha import primitive_pb2

# The following line is actually about the permissions
# you might be using for the transaction.
# You can find all the permissions here: 
# https://iroha.readthedocs.io/en/main/develop/api/permissions.html
from iroha.primitive_pb2 import can_set_my_account_detail
import sys

if sys.version_info[0] < 3:
    raise Exception('Python 3 or a more recent version is required.')

# environment and admin account information:
IROHA_HOST_ADDR = os.getenv('IROHA_HOST_ADDR', '127.0.0.1')
IROHA_PORT = os.getenv('IROHA_PORT', '50051')
ADMIN_ACCOUNT_ID = os.getenv('ADMIN_ACCOUNT_ID', 'admin@test')
ADMIN_PRIVATE_KEY = os.getenv(
    'ADMIN_PRIVATE_KEY', 'f101537e319568c765b2cc89698325604991dca57b9716b58016b253506cab70')

# create user key

user_private_key = IrohaCrypto.private_key()
user_public_key = IrohaCrypto.derive_public_key(user_private_key)
# print(str(user_private_key) + '\n' + str(user_public_key))
iroha = Iroha(ADMIN_ACCOUNT_ID)
net = IrohaGrpc('{}:{}'.format(IROHA_HOST_ADDR, IROHA_PORT))


def trace(func):
    """
    A decorator for tracing methods' begin/end execution points
    """

    def tracer(*args, **kwargs):
        name = func.__name__
        print('\tEntering "{}"'.format(name))
        result = func(*args, **kwargs)
        print('\tLeaving "{}"'.format(name))
        return result

    return tracer

#  define the commands:
@trace
def send_transaction_and_print_status(transaction):
    hex_hash = binascii.hexlify(IrohaCrypto.hash(transaction))
    print('Transaction hash = {}, creator = {}'.format(
        hex_hash, transaction.payload.reduced_payload.creator_account_id))
    net.send_tx(transaction)
    for status in net.tx_status_stream(transaction):
        print(status)

# For example, below we define a transaction made of 2 commands:
# CreateDomain and CreateAsset.
# Each of Iroha commands has its own set of parameters and there are many commands.
# You can check out all of them here:
# https://iroha.readthedocs.io/en/main/develop/api/commands.html
@trace
def create_asset(asset_name, domain_id, precision):
    tx = iroha.transaction([
        iroha.command('CreateAsset',
                    asset_name=asset_name,
                    domain_id=domain_id, precision=precision)
    ])
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    send_transaction_and_print_status(tx)

@trace 
def add_asset_quantity(asset_id, amount):
    tx = iroha.transaction([
        iroha.command('AddAssetQuantity', asset_id = asset_id, amount = amount)
    ])
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    send_transaction_and_print_status(tx)

@trace
def create_domain_and_asset():
    """
    Create domain 'domain' and asset 'coin#domain' with precision 2
    """
    commands = [
        iroha.command('CreateDomain', domain_id='domain', default_role='user'),
        iroha.command('CreateAsset', asset_name='coin',
                      domain_id='domain', precision=2)
    ]
# And sign the transaction using the keys from earlier:
    tx = IrohaCrypto.sign_transaction(
        iroha.transaction(commands), ADMIN_PRIVATE_KEY)
    send_transaction_and_print_status(tx)
# You can define queries 
# (https://iroha.readthedocs.io/en/main/develop/api/queries.html) 
# the same way.

@trace
def add_coin_to_admin():
    """
    Add 1000.00 units of 'coin#domain' to 'admin@test'
    """
    tx = iroha.transaction([
        iroha.command('AddAssetQuantity',
                      asset_id='coin#domain', amount='1000.00')
    ])
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    send_transaction_and_print_status(tx)


@trace
def create_account(account, domain):
    """
    Create account 'userone@domain'
    """
    tx = iroha.transaction([
        iroha.command('CreateAccount', account_name=account, domain_id=domain,
                    public_key=user_public_key)
    ])
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    send_transaction_and_print_status(tx)


@trace
def transfer_asset_from_admin_to_user(dest_account_id, asset_id, amount, description):
    """
    Transfer 2.00 'coin#domain' from 'admin@test' to 'userone@domain'
    """
    tx = iroha.transaction([
        iroha.command('TransferAsset', src_account_id='admin@test', dest_account_id=dest_account_id,
                      asset_id=asset_id, description=description, amount=amount)
    ])
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    send_transaction_and_print_status(tx)


@trace
def userone_grants_to_admin_set_account_detail_permission():
    """
    Make admin@test able to set detail to userone@domain
    """
    tx = iroha.transaction([
        iroha.command('GrantPermission', account_id='admin@test',
                      permission=can_set_my_account_detail)
    ], creator_account='datdang@test')
   
    send_transaction_and_print_status(tx)


@trace
def set_age_to_userone():
    """
    Set age to userone@domain by admin@test
    """
    tx = iroha.transaction([
        iroha.command('SetAccountDetail',
                      account_id='userone@domain', key='age', value='18')
    ])
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    send_transaction_and_print_status(tx)


@trace
def get_coin_info():
    """
    Get asset info for coin#domain
    :return:
    """
    query = iroha.query('GetAssetInfo', asset_id='coin#domain')
    IrohaCrypto.sign_query(query, ADMIN_PRIVATE_KEY)

    response = net.send_query(query)
    data = response.asset_response.asset
    print('Asset id = {}, precision = {}'.format(data.asset_id, data.precision))


@trace
def get_account_assets(account_id):
    """
    List all the assets of userone@domain
    """
    query = iroha.query('GetAccountAssets', account_id=account_id)
    IrohaCrypto.sign_query(query, ADMIN_PRIVATE_KEY)

    response = net.send_query(query)
    data = response.account_assets_response.account_assets
    for asset in data:
        print('Asset id = {}, balance = {}'.format(
            asset.asset_id, asset.balance))


@trace
def get_userone_details():
    """
    Get all the kv-storage entries for userone@domain
    """
    query = iroha.query('GetAccountDetail', account_id='userone@domain')
    IrohaCrypto.sign_query(query, ADMIN_PRIVATE_KEY)

    response = net.send_query(query)
    data = response.account_detail_response
    print('Account id = {}, details = {}'.format('userone@domain', data.detail))

def transfer_asset_tx(src_account_id, dest_account_id, asset_id, amount, src_private_key):
    tx = iroha.transaction([
        iroha.command('TransferAsset',
            src_account_id=src_account_id,
            dest_account_id=dest_account_id,
            asset_id=asset_id,
            amount=amount,
            description='transfer ' + amount +  ' ' + asset_id + ' from '  + src_account_id + ' to ' + dest_account_id)
    ], creator_account=src_account_id) 
    IrohaCrypto.sign_transaction(tx,src_private_key)
    send_transaction_and_print_status(tx)

def get_account_public_key(account_id, private_key):
    query = iroha.query('GetSignatories', account_id=account_id)
    IrohaCrypto.sign_query(query, private_key)
    response = net.send_query(query)
    # data = response.account_detail_response
    # print('Account id = {}, details = {}'.format('userone@domain', data.detail))
    # 
    # print(response.signatories_response.keys)
    # if('86d63055eb04ed2753e767940ccb16b638acd94b3c7ea81ea677b7a77b80d352' ==str(response.signatories_response.keys[0])): 
    #     print('==')
    return response.signatories_response.keys[0]
def get_acc_tx(account_id):
    query = iroha.query('GetAccountTransactions', creator_account='admin@test', account_id=account_id, page_size=10)
    IrohaCrypto.sign_query(query, ADMIN_PRIVATE_KEY)
    response = net.send_query(query)
    print(response)
# Let's run the commands defined previously:
# create_account('dattm2', 'test')
# transfer_asset_tx('dattm1', 'dattm2', 'money#test', '10', 'c0db6e3e7af8677dda81b7c89cbec94b05c1516bc7d881fd142bf9747b2e425f')
# transfer_asset_tx('test@test', 'dattm2@test', 'money#test', '10', '7e00405ece477bb6dd9b03a78eee4e708afc2f5bcdce399573a5958942f4a390')

#get_account_assets()

# get_account_assets('dattm2@test')

# create_asset('ruby','test',0)
# add_asset_quantity('ruby#test', '50')
# get_account_assets('admin@test')
# transfer_asset_from_admin_to_user('dattm1@test', 'ruby#test','20', 'transfer 20 ruby from admin to dattm1')

# transfer_asset_tx('dattm1@test', 'dattm2@test', 'ruby#test', '10', 'c0db6e3e7af8677dda81b7c89cbec94b05c1516bc7d881fd142bf9747b2e425f')
# get_account_assets('dattm1@test')
# get_account_assets('dattm2@test')
print(get_acc_tx('admin@test'))
print('done')