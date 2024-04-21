# import account
# import integration_helpers


# hash = account.create_contract()
# print("Hash:" + str(hash))
# address = integration_helpers.get_engine_receipts_address(hash)
# hash = account.create_account(address=address)
# integration_helpers.get_engine_receipts_address(hash)
# print("DONE")

from iroha_operations import create_new_account

# ...

# Call the function to create a new account
create_new_account()