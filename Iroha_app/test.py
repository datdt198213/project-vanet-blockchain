import commons
from iroha import primitive_pb2
from iroha import Iroha, IrohaCrypto, IrohaGrpc
admin = commons.new_user('admin@first')
alice = commons.new_user('alice@second')
iroha = Iroha(admin['id'])
 

 
@commons.hex
def genesis_tx():
    test_permissions = [primitive_pb2.can_get_all_accounts]
    genesis_commands = commons.genesis_block(admin, alice, test_permissions, multidomain=True)
    tx = iroha.transaction(genesis_commands)
    IrohaCrypto.sign_transaction(tx, admin['key'])
    return tx


@commons.hex
def account_query():
    query = iroha.query('GetAccount', creator_account=alice['id'], account_id=admin['id'])
    IrohaCrypto.sign_query(query, alice['key'])
    return query