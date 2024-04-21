# from Crypto.Hash import keccak
import os
import sys
import binascii

import json
from iroha import Iroha, IrohaCrypto, IrohaGrpc
import integration_helpers

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required")

current_directory = os.path.dirname(os.path.abspath(__file__))
iroha_file = '../contracts/Account.json'

IROHA_HOST_ADDR = os.getenv("IROHA_HOST_ADDR", "127.0.0.1")
IROHA_PORT = os.getenv("IROHA_PORT", "50051")
ADMIN_ACCOUNT_ID = os.getenv("ADMIN_ACCOUNT_ID", "admin@test")
ADMIN_PRIVATE_KEY = os.getenv(
    "ADMIN_PRIVATE_KEY", "f101537e319568c765b2cc89698325604991dca57b9716b58016b253506cab70")


iroha = Iroha(ADMIN_ACCOUNT_ID)
net = IrohaGrpc('{}:{}'.format(IROHA_HOST_ADDR, IROHA_PORT))

node2_private_key = IrohaCrypto.private_key()
node2_public_key = IrohaCrypto.derive_public_key(
    node2_private_key).decode("utf-8")

"""Bytecode was generated using truffle from file Account.sol"""
bytecode = ('0x608060405234801561001057600080fd5b5073a6abc17819738299b3b2c1ce46d55c74f04e290c6000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550610996806100746000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c80634518f6b314610046578063bc53c0c414610076578063d4e804ab146100a6575b600080fd5b610060600480360381019061005b9190610578565b6100c4565b60405161006d9190610640565b60405180910390f35b610090600480360381019061008b9190610662565b610230565b60405161009d9190610640565b60405180910390f35b6100ae6103fa565b6040516100bb919061074a565b60405180910390f35b60606000826040516024016100d991906107ba565b6040516020818303038152906040527f4518f6b3000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19166020820180517bffffffffffffffffffffffffffffffffffffffffffffffffffffffff8381831617835250505050905060008060008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16836040516101a09190610818565b600060405180830381855af49150503d80600081146101db576040519150601f19603f3d011682016040523d82523d6000602084013e6101e0565b606091505b509150915081610225576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161021c906108a1565b60405180910390fd5b809350505050919050565b60606000848484604051602401610249939291906108c1565b6040516020818303038152906040527fbc53c0c4000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19166020820180517bffffffffffffffffffffffffffffffffffffffffffffffffffffffff8381831617835250505050905060008060008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16836040516103109190610818565b600060405180830381855af49150503d806000811461034b576040519150601f19603f3d011682016040523d82523d6000602084013e610350565b606091505b509150915081610395576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161038c906108a1565b60405180910390fd5b856040516103a39190610949565b6040518091039020876040516103b99190610949565b60405180910390207fb4086b7a9e5eac405225b6c630a4147f0a8dcb4af3583733b10db7b91ad21ffd60405160405180910390a38093505050509392505050565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000604051905090565b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b6104858261043c565b810181811067ffffffffffffffff821117156104a4576104a361044d565b5b80604052505050565b60006104b761041e565b90506104c3828261047c565b919050565b600067ffffffffffffffff8211156104e3576104e261044d565b5b6104ec8261043c565b9050602081019050919050565b82818337600083830152505050565b600061051b610516846104c8565b6104ad565b90508281526020810184848401111561053757610536610437565b5b6105428482856104f9565b509392505050565b600082601f83011261055f5761055e610432565b5b813561056f848260208601610508565b91505092915050565b60006020828403121561058e5761058d610428565b5b600082013567ffffffffffffffff8111156105ac576105ab61042d565b5b6105b88482850161054a565b91505092915050565b600081519050919050565b600082825260208201905092915050565b60005b838110156105fb5780820151818401526020810190506105e0565b60008484015250505050565b6000610612826105c1565b61061c81856105cc565b935061062c8185602086016105dd565b6106358161043c565b840191505092915050565b6000602082019050818103600083015261065a8184610607565b905092915050565b60008060006060848603121561067b5761067a610428565b5b600084013567ffffffffffffffff8111156106995761069861042d565b5b6106a58682870161054a565b935050602084013567ffffffffffffffff8111156106c6576106c561042d565b5b6106d28682870161054a565b925050604084013567ffffffffffffffff8111156106f3576106f261042d565b5b6106ff8682870161054a565b9150509250925092565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600061073482610709565b9050919050565b61074481610729565b82525050565b600060208201905061075f600083018461073b565b92915050565b600081519050919050565b600082825260208201905092915050565b600061078c82610765565b6107968185610770565b93506107a68185602086016105dd565b6107af8161043c565b840191505092915050565b600060208201905081810360008301526107d48184610781565b905092915050565b600081905092915050565b60006107f2826105c1565b6107fc81856107dc565b935061080c8185602086016105dd565b80840191505092915050565b600061082482846107e7565b915081905092915050565b7f4572726f722063616c6c696e67207365727669636520636f6e7472616374206660008201527f756e6374696f6e00000000000000000000000000000000000000000000000000602082015250565b600061088b602783610770565b91506108968261082f565b604082019050919050565b600060208201905081810360008301526108ba8161087e565b9050919050565b600060608201905081810360008301526108db8186610781565b905081810360208301526108ef8185610781565b905081810360408301526109038184610781565b9050949350505050565b600081905092915050565b600061092382610765565b61092d818561090d565b935061093d8185602086016105dd565b80840191505092915050565b60006109558284610918565b91508190509291505056fea264697066735822122003a9a7eed3573c48be57d61f92766e952fd416de65794c7b6b42a725cbfdfa0e64736f6c63430008130033')
# with open(iroha_file) as json_file:
#         data = json.load(json_file)
#         temp = data['bytecode']
#         bytecode = (temp)


@integration_helpers.trace
def create_contract():
    tx = iroha.transaction(
        [iroha.command("CallEngine", caller=ADMIN_ACCOUNT_ID, input=bytecode)])
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    net.send_tx(tx)
    hex_hash = binascii.hexlify(IrohaCrypto.hash(tx))
    for status in net.tx_status_stream(tx):
        print(status)
    return hex_hash


@integration_helpers.trace
def create_account(address):
    # b"createAccount(string,string,string)": is a byte string
    params = integration_helpers.get_first_four_bytes_of_keccak(
        b"createAccount(string,string,string)")
    no_of_param = 3  # number of params be added to 'params' variable
    for x in range(no_of_param):
        params = params + \
            integration_helpers.left_padded_address_of_param(x, no_of_param)

    # Adding 3 params including information of an account
    # source account id
    params = params + integration_helpers.argument_encoding("test")
    params = params + \
        integration_helpers.argument_encoding("burrow")  # domain id
    params = params + \
        integration_helpers.argument_encoding(node2_public_key)  # public key

    tx = iroha.transaction(
        [iroha.command("CallEngine", caller=ADMIN_ACCOUNT_ID, callee=address, input=params)])

    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    response = net.send_tx(tx)
    print("Response: " + response)
    for status in net.tx_status_stream(tx):
        print("Status: " + status)
    hex_hash = binascii.hexlify(IrohaCrypto.hash(tx))
    return hex_hash


@integration_helpers.trace
def get_account(address):
    params = integration_helpers.get_first_four_bytes_of_keccak(
        b"getAccount(string)")
    no_of_params = 1  # Number of params be added to 'params' variable
    for x in (no_of_params):
        params = params + \
            integration_helpers.left_padded_address_of_param(x, no_of_params)
    params = params + \
        integration_helpers.argument_encoding("test@burrow")  # account id

    tx = iroha.transaction(
        [iroha.command("CallEngine", caller=ADMIN_ACCOUNT_ID, callee=address, input=params)])

    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    response = net.send_tx(tx)
    print("Response: " + response)
    for status in net.tx_status_stream(tx):
        print(status)
    hex_hash = binascii.hexlify(IrohaCrypto.hahs(tx))
    return hex_hash


