import os
import binascii
from iroha import IrohaCrypto
from iroha import Iroha, IrohaGrpc
from iroha import primitive_pb2

IROHA_HOST_ADDR = os.getenv('IROHA_HOST_ADDR', '127.0.0.1')
IROHA_PORT = os.getenv('IROHA_PORT', '50051')

# print(str(private_key) + '\n' + str(public_key))
ADMIN_ACCOUNT_ID = os.getenv('ADMIN_ACCOUNT_ID', 'admin@test')
ADMIN_PRIVATE_KEY = os.getenv(
    'ADMIN_PRIVATE_KEY', 'f101537e319568c765b2cc89698325604991dca57b9716b58016b253506cab70')

if not ADMIN_PRIVATE_KEY:
    raise ValueError("ADMIN_PRIVATE_KEY environment variable is not set.")

iroha = Iroha(ADMIN_ACCOUNT_ID)
net = IrohaGrpc('{}:{}'.format(IROHA_HOST_ADDR, IROHA_PORT))

# Decorator truy vết điểm bắt đầu và kết thúc khi thực thi
def trace(func):
    def tracer(*args, **kwargs):
        name = func.__name__
        print('\tEntering "{}"'.format(name))
        result = func(*args, **kwargs)
        print('\tLeaving "{}"'.format(name))
        return result

    return tracer

# Gửi transaction và thông báo thực hiện thành công hoặc thất bại 
@trace
def send_transaction_and_print_status(transaction):
    hex_hash = binascii.hexlify(IrohaCrypto.hash(transaction))
    print('Transaction hash = {}, creator = {}'.format(
        hex_hash, transaction.payload.reduced_payload.creator_account_id))
    net.send_tx(transaction)
    for status in net.tx_status_stream(transaction):
        print(status)

# Đăng ký tài khoản người dùng
@trace
def register(account, domain, public_key):
    tx = iroha.transaction([
        iroha.command('CreateAccount', account_name=account, domain_id=domain,
                    public_key=public_key)
    ])
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    send_transaction_and_print_status(tx)

# Tạo cặp khóa public và private key ngẫu nhiên cho người dùng
def generate_key():
    private_key = IrohaCrypto.private_key()
    public_key = IrohaCrypto.derive_public_key(private_key)
    return private_key, public_key
    
# Lưu cặp khóa vào public và private key vào file account_name@domain_id
def store_key(account_name, domain_id, private_key, public_key):
    priv_file = f"key/{account_name}@{domain_id}.priv"
    pub_file = f"key/{account_name}@{domain_id}.pub"

    with open(priv_file, 'w') as file:
        file.write(private_key.decode('utf-8'))
    with open(pub_file, 'w') as file:
        file.write(public_key.decode('utf-8'))

def main():
    account_name = "dat9"
    domain_id = "test"
    private_key, public_key = generate_key()
    register(account_name, domain_id, public_key)
    store_key(account_name, domain_id, private_key, public_key)

if __name__ == "__main__":
    main()