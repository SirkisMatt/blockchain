# Initializing our (empty) blockchain list
MINING_REWARD = 10

genesis_block = {
        'previous_hash': '',
        'index': 0,
        'transactions': []
    }
blockchain = [genesis_block]
open_transactions = []
owner = 'Matt'
participants = {'Matt'}

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(particpant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == particpant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == particpant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == particpant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    else:
        return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


# This function accepts two arguments.
# One required one (value) and one optional one ()last_transaction)
# The optional one is optional because it has a defait value => [1]
def add_transaction(recipient, sender=owner, amount=1.0):
    """
    Arguments:
        :sender: The sender of the coins.
        :recipient: The Recipient of the coins.
        :amount: The amount of coins sent with the transaction (default = 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    # copied_transactions = 
    open_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    for block in blockchain:
            print('Outputting Block')
            print(block)

def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True

waiting_for_input = True


while waiting_for_input:
    print('Please Choose: ')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output blockchain values')
    print('4: Output participants')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
                print('Addded transaction!')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_choice == 2:
        if mine_block():
            open_transactions = []
    elif user_choice == 3:
        print_blockchain_elements()
    elif user_choice == 4:
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{
                    'sender': 'Billy',
                    'recipient': 'Matt',
                    'amount': 100
                }]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('input was invalid, please pick a value from the list')
    print('Choice registered!')
    if not verify_chain():
        print("invalid blockchain")
        break
    print(get_balance('Matt'))
print('Done!')

