blockchain = []

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    else:
        return blockchain[-1]


def add_transaction(value, last_transaction):

    if last_transaction == None:
            last_transaction = [1]
    blockchain.append([last_transaction, value])

def get_transaction_value():
    return float(input('Your transaction amount please: '))


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    for block in blockchain:
            print('Outputting Block')
            print(block)

def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index+=1
            print(block[0], blockchain[block_index - 1])
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


while True:
    print('Please Choose: ')
    print('1: Add a new transaction value')
    print('2: Output blockchain values')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == 2:
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('input was invalid, please pick a value from the list')
    print('Choice registered!')
    
    if not verify_chain():
        print("invalid blockchain")
        break

print('Done!')

