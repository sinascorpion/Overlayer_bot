# =========================================================
# OVERLAYER SEPOLIA BOT
# =========================================================

import os
import time
import random

from datetime import datetime

from web3 import Web3
from dotenv import load_dotenv
from eth_account import Account

# =========================================================
# BANNER
# =========================================================

print("""

==================================================
            OVERLAYER SEPOLIA BOT
==================================================

 Developed By IRDropper

 Telegram:
 https://t.me/irdropper

 Multi Wallet | Auto Bridge | Auto Mint

==================================================

""")

# =========================================================
# ENV
# =========================================================

load_dotenv()

PRIVATE_KEYS = os.getenv("PRIVATE_KEYS").split(",")

# =========================================================
# SETTINGS
# =========================================================

CHAIN_ID = 11155111

FAUCET_LIMIT = 5000

TARGET_TX_MIN = 50
TARGET_TX_MAX = 55

CYCLE_SLEEP_MIN = 22 * 60 * 60
CYCLE_SLEEP_MAX = 28 * 60 * 60

# =========================================================
# RPCS
# =========================================================

RPCS = [

    "https://sepolia.rpc.sentio.xyz",
    "https://rpc.sepolia.ethpandaops.io",
    "https://ethereum-sepolia-public.nodies.app",
    "https://eth-sepolia.api.onfinality.io/public",
    "https://sepolia.drpc.org",
    "https://0xrpc.io/sep",
    "https://api.zan.top/eth-sepolia",
    "https://1rpc.io/sepolia",
    "https://ethereum-sepolia-rpc.publicnode.com",
    "https://gateway.tenderly.co/public/sepolia",
    "https://sepolia.gateway.tenderly.co"

]

# =========================================================
# CONTRACTS
# =========================================================

USDC = Web3.to_checksum_address(
    "0x94a9D9AC8a22534E3FaCa9F4e7F2E2cf85d5E4C8"
)

USDT = Web3.to_checksum_address(
    "0xaa8E23Fb1079EA71E0A56F48A2aA51851D8433D0"
)

USDC_PLUS = Web3.to_checksum_address(
    "0xE815718D44694ec4637CB775C468d87f6e15B538"
)

USDT_PLUS = Web3.to_checksum_address(
    "0xe20534a32f9162488a90026f268a74fbe28d272d"
)

USDC_STAKING = Web3.to_checksum_address(
    "0x753937137Eb92871A6F3517514d4f1Ee860e3FDF"
)

USDT_STAKING = Web3.to_checksum_address(
    "0x079a4Bf1Cbd0E4ce15391340cB46efA6396aBc82"
)

FAUCET = Web3.to_checksum_address(
    "0xC959483DBa39aa9E78757139af0e9a2EDEb3f42D"
)

# =========================================================
# ABI
# =========================================================

ERC20_ABI = [

    {
        "constant": False,
        "inputs": [
            {"name": "spender", "type": "address"},
            {"name": "amount", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    },

    {
        "constant": False,
        "inputs": [
            {"name": "to", "type": "address"},
            {"name": "amount", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    }
]

FAUCET_ABI = [

    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "mint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

PLUS_ABI = ERC20_ABI + [

    {
        "inputs": [
            {
                "components": [
                    {"internalType": "address","name": "benefactor","type": "address"},
                    {"internalType": "address","name": "beneficiary","type": "address"},
                    {"internalType": "address","name": "collateral","type": "address"},
                    {"internalType": "uint256","name": "collateralAmount","type": "uint256"},
                    {"internalType": "uint256","name": "minUsdAmount","type": "uint256"}
                ],
                "internalType": "struct MintOrder",
                "name": "order_",
                "type": "tuple"
            }
        ],
        "name": "mint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },

    {
        "inputs": [

            {
                "components": [

                    {"internalType": "uint32","name": "dstEid","type": "uint32"},
                    {"internalType": "bytes32","name": "to","type": "bytes32"},
                    {"internalType": "uint256","name": "amountLD","type": "uint256"},
                    {"internalType": "uint256","name": "minAmountLD","type": "uint256"},
                    {"internalType": "bytes","name": "extraOptions","type": "bytes"},
                    {"internalType": "bytes","name": "composeMsg","type": "bytes"},
                    {"internalType": "bytes","name": "oftCmd","type": "bytes"}

                ],
                "internalType": "struct SendParam",
                "name": "_sendParam",
                "type": "tuple"
            },

            {
                "components": [

                    {"internalType": "uint256","name": "nativeFee","type": "uint256"},
                    {"internalType": "uint256","name": "lzTokenFee","type": "uint256"}

                ],
                "internalType": "struct MessagingFee",
                "name": "_fee",
                "type": "tuple"
            },

            {
                "internalType": "address",
                "name": "_refundAddress",
                "type": "address"
            }

        ],
        "name": "send",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]

STAKING_ABI = [

    {
        "inputs": [
            {"internalType": "uint256","name": "assets","type": "uint256"},
            {"internalType": "address","name": "receiver","type": "address"}
        ],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# =========================================================
# RPC
# =========================================================

def get_working_w3():

    for rpc in RPCS:

        try:

            print(f"[TEST RPC] {rpc}")

            w3 = Web3(
                Web3.HTTPProvider(
                    rpc,
                    request_kwargs={
                        "timeout": 30
                    }
                )
            )

            block = w3.eth.block_number

            print(f"[RPC OK] BLOCK {block}")

            return w3

        except Exception:

            print(f"[RPC FAILED] {rpc}")

    raise Exception("NO WORKING RPC")

w3 = get_working_w3()

# =========================================================
# CONTRACTS
# =========================================================

usdc = w3.eth.contract(address=USDC, abi=ERC20_ABI)
usdt = w3.eth.contract(address=USDT, abi=ERC20_ABI)

usdc_plus = w3.eth.contract(address=USDC_PLUS, abi=PLUS_ABI)
usdt_plus = w3.eth.contract(address=USDT_PLUS, abi=PLUS_ABI)

usdc_staking = w3.eth.contract(address=USDC_STAKING, abi=STAKING_ABI)
usdt_staking = w3.eth.contract(address=USDT_STAKING, abi=STAKING_ABI)

faucet = w3.eth.contract(address=FAUCET, abi=FAUCET_ABI)

# =========================================================
# WALLETS
# =========================================================

WALLETS = []

for index, pk in enumerate(PRIVATE_KEYS):

    pk = pk.strip()

    account = Account.from_key(pk)

    WALLETS.append({

        "id": index + 1,
        "private_key": pk,
        "address": account.address

    })

# =========================================================
# GLOBAL TX COUNTER
# =========================================================

CURRENT_TX = 0
TARGET_TX = 0

# =========================================================
# HELPERS
# =========================================================

def add_tx():

    global CURRENT_TX

    CURRENT_TX += 1

    print(
        f"[TX COUNT] "
        f"{CURRENT_TX}/{TARGET_TX}"
    )

def log(wallet, text):

    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] "
        f"[Wallet {wallet['id']}] "
        f"{wallet['address']} => {text}"
    )

def random_sleep():

    sec = random.randint(18, 70)

    for i in range(sec, 0, -1):

        print(
            f"\rWAITING NEXT ACTION {i}s ",
            end="",
            flush=True
        )

        time.sleep(1)

    print("\n")

def get_balance(token, wallet):

    try:

        selector = "0x70a08231"

        data = (
            selector
            + wallet["address"][2:].rjust(64, "0")
        )

        result = w3.eth.call({
            "to": token.address,
            "data": data
        })

        return int.from_bytes(result, "big")

    except:
        return 0

# =========================================================
# ALLOWANCE CHECK
# =========================================================

def has_allowance(
    token_contract,
    owner,
    spender
):

    selector = "0xdd62ed3e"

    data = (
        selector
        + owner[2:].rjust(64, "0")
        + spender[2:].rjust(64, "0")
    )

    result = w3.eth.call({
        "to": token_contract.address,
        "data": data
    })

    allowance = int.from_bytes(
        result,
        "big"
    )

    return allowance > 10**30

# =========================================================
# TX
# =========================================================

def send_tx(tx, wallet, action="UNKNOWN"):

    global w3

    try:

        nonce = w3.eth.get_transaction_count(
            wallet["address"]
        )

        latest = w3.eth.get_block("latest")

        base_fee = latest.get(
            "baseFeePerGas",
            w3.to_wei(1, "gwei")
        )

        priority = w3.to_wei(
            random.uniform(0.1, 0.25),
            "gwei"
        )

        max_fee = int(base_fee * 2 + priority)

        tx.update({

            "from": wallet["address"],
            "nonce": nonce,
            "chainId": CHAIN_ID,
            "gas": random.randint(300000, 850000),
            "maxFeePerGas": max_fee,
            "maxPriorityFeePerGas": int(priority),
            "type": 2

        })

        signed = w3.eth.account.sign_transaction(
            tx,
            wallet["private_key"]
        )

        tx_hash = w3.eth.send_raw_transaction(
            signed.rawTransaction
        )

        tx_hex = tx_hash.hex()

        print(f"[TX SENT] {action}")
        print(f"[TX HASH] {tx_hex}")

        receipt = w3.eth.wait_for_transaction_receipt(
            tx_hash,
            timeout=180
        )

        if receipt["status"] == 1:

            print(f"[SUCCESS] {action}\n")

            add_tx()

            return True

        print(f"[FAILED] {action}\n")

        return False

    except Exception as e:

        print(f"[TX ERROR] {action} => {e}")

        try:
            w3 = get_working_w3()
        except:
            pass

        return False

# =========================================================
# RANDOMS
# =========================================================

def large_random():
    return round(random.uniform(1000, 1500), 2)

def small_random():
    return round(random.uniform(1, 8), 2)

def big_random():
    return round(random.uniform(400, 500), 2)

# =========================================================
# BALANCE CHECK
# =========================================================

def ensure_plus_balance(

    wallet,
    plus_contract,
    collateral_token,
    token_contract,
    needed_amount,
    mint_text

):

    balance = get_balance(
        token_contract,
        wallet
    ) / 1e18

    if balance >= needed_amount:

        return True

    needed = round(
        needed_amount - balance + random.uniform(50, 150),
        2
    )

    print(
        f"[AUTO MINT NEEDED] "
        f"{mint_text} => {needed}"
    )

    ok = mint_plus(

        wallet,
        plus_contract,
        collateral_token,
        needed,
        f"AUTO {mint_text}"

    )

    if ok:
        random_sleep()

    return ok

# =========================================================
# ACTIONS
# =========================================================

def faucet_token(wallet, token_address, token_name):

    token_contract = usdc if token_name == "USDC" else usdt

    balance = get_balance(token_contract, wallet) / 1_000_000

    print(f"{token_name} BALANCE => {balance}")

    if balance >= FAUCET_LIMIT:

        log(wallet, f"{token_name} SKIP")

        return False

    action = f"FAUCET {token_name}"

    log(wallet, action)

    amount = 10000 * 10**6

    tx = faucet.functions.mint(

        token_address,
        wallet["address"],
        amount

    ).build_transaction({

        "from": wallet["address"]

    })

    return send_tx(tx, wallet, action)

def approve(
    token_contract,
    spender,
    wallet,
    text
):

    already = has_allowance(

        token_contract,
        wallet["address"],
        spender

    )

    if already:

        log(
            wallet,
            f"{text} SKIPPED"
        )

        return False

    log(wallet, text)

    tx = token_contract.functions.approve(

        spender,
        2**256 - 1

    ).build_transaction({

        "from": wallet["address"]

    })

    return send_tx(
        tx,
        wallet,
        text
    )

def mint_plus(
    wallet,
    plus_contract,
    collateral_token,
    amount,
    text
):

    action = f"{text} {amount}"

    log(wallet, action)

    collateral_amount = int(amount * 1_000_000)

    min_usd = Web3.to_wei(amount, "ether")

    order = (

        wallet["address"],
        wallet["address"],
        collateral_token,
        collateral_amount,
        min_usd

    )

    tx = plus_contract.functions.mint(order).build_transaction({

        "from": wallet["address"]

    })

    return send_tx(tx, wallet, action)

def stake(
    wallet,
    staking_contract,
    amount,
    text
):

    action = f"{text} {amount}"

    log(wallet, action)

    wei_amount = Web3.to_wei(amount, "ether")

    tx = staking_contract.functions.deposit(

        wei_amount,
        wallet["address"]

    ).build_transaction({

        "from": wallet["address"]

    })

    return send_tx(tx, wallet, action)

def bridge(
    wallet,
    plus_contract,
    amount,
    text
):

    action = f"{text} {amount}"

    log(wallet, action)

    wei_amount = Web3.to_wei(amount, "ether")

    receiver = (
        "0x"
        + wallet["address"][2:].rjust(64, "0")
    )

    extra_options = bytes.fromhex(
        "000301001101000000000000000000000000000186A0"
    )

    send_param = (

        40245,
        receiver,
        wei_amount,
        wei_amount,
        extra_options,
        b"",
        b""

    )

    fee = (
        Web3.to_wei(0.00011, "ether"),
        0
    )

    tx = plus_contract.functions.send(

        send_param,
        fee,
        wallet["address"]

    ).build_transaction({

        "from": wallet["address"],
        "value": fee[0]

    })

    return send_tx(tx, wallet, action)

def transfer_token(
    token_contract,
    sender_wallet,
    receiver_wallet,
    amount,
    text
):

    action = (
        f"{text} {amount} "
        f"-> Wallet {receiver_wallet['id']}"
    )

    log(sender_wallet, action)

    wei_amount = Web3.to_wei(amount, "ether")

    tx = token_contract.functions.transfer(

        receiver_wallet["address"],
        wei_amount

    ).build_transaction({

        "from": sender_wallet["address"]

    })

    return send_tx(tx, sender_wallet, action)

# =========================================================
# MAIN
# =========================================================

def run_cycle():

    global CURRENT_TX
    global TARGET_TX

    CURRENT_TX = 0

    TARGET_TX = random.randint(
        TARGET_TX_MIN,
        TARGET_TX_MAX
    )

    print(
        f"\n[TARGET TX] {TARGET_TX}\n"
    )

    random.shuffle(WALLETS)

    print("\n========== START CYCLE ==========\n")

    # =====================================================
    # FAUCET
    # =====================================================

    for wallet in WALLETS:

        faucet_token(wallet, USDC, "USDC")
        faucet_token(wallet, USDT, "USDT")

    # =====================================================
    # APPROVE
    # =====================================================

    for wallet in WALLETS:

        approve(
            usdc,
            USDC_PLUS,
            wallet,
            "APPROVE USDC"
        )

        approve(
            usdt,
            USDT_PLUS,
            wallet,
            "APPROVE USDT"
        )

        approve(
            usdc_plus,
            USDC_STAKING,
            wallet,
            "APPROVE USDC+"
        )

        approve(
            usdt_plus,
            USDT_STAKING,
            wallet,
            "APPROVE USDT+"
        )

    # =====================================================
    # LARGE MINTS
    # =====================================================

    wallet = random.choice(WALLETS)

    mint_plus(
        wallet,
        usdc_plus,
        USDC,
        large_random(),
        "BIG MINT USDC+"
    )

    random_sleep()

    mint_plus(
        wallet,
        usdt_plus,
        USDT,
        large_random(),
        "BIG MINT USDT+"
    )

    random_sleep()

    # =====================================================
    # RANDOM ACTIVITY
    # =====================================================

    while CURRENT_TX < TARGET_TX - 4:

        action_type = random.choice([
            "stake",
            "bridge"
        ])

        wallet = random.choice(WALLETS)

        token_type = random.choice([
            "usdc",
            "usdt"
        ])

        if action_type == "stake":

            amount = small_random()

            if token_type == "usdc":

                ensure_plus_balance(

                    wallet,
                    usdc_plus,
                    USDC,
                    usdc_plus,
                    amount,
                    "MINT USDC+"

                )

                ok = stake(
                    wallet,
                    usdc_staking,
                    amount,
                    "STAKE USDC+"
                )

            else:

                ensure_plus_balance(

                    wallet,
                    usdt_plus,
                    USDT,
                    usdt_plus,
                    amount,
                    "MINT USDT+"

                )

                ok = stake(
                    wallet,
                    usdt_staking,
                    amount,
                    "STAKE USDT+"
                )

        else:

            amount = small_random()

            if token_type == "usdc":

                ensure_plus_balance(

                    wallet,
                    usdc_plus,
                    USDC,
                    usdc_plus,
                    amount,
                    "MINT USDC+"

                )

                ok = bridge(
                    wallet,
                    usdc_plus,
                    amount,
                    "BRIDGE USDC+"
                )

            else:

                ensure_plus_balance(

                    wallet,
                    usdt_plus,
                    USDT,
                    usdt_plus,
                    amount,
                    "MINT USDT+"

                )

                ok = bridge(
                    wallet,
                    usdt_plus,
                    amount,
                    "BRIDGE USDT+"
                )

        if ok:
            random_sleep()

    # =====================================================
    # LARGE ACTIVITIES
    # =====================================================

    wallet = random.choice(WALLETS)

    amount = big_random()

    ensure_plus_balance(

        wallet,
        usdc_plus,
        USDC,
        usdc_plus,
        amount,
        "MINT USDC+"

    )

    stake(
        wallet,
        usdc_staking,
        amount,
        "BIG STAKE USDC+"
    )

    random_sleep()

    amount = big_random()

    ensure_plus_balance(

        wallet,
        usdt_plus,
        USDT,
        usdt_plus,
        amount,
        "MINT USDT+"

    )

    bridge(
        wallet,
        usdt_plus,
        amount,
        "BIG BRIDGE USDT+"
    )

    random_sleep()

    # =====================================================
    # TRANSFERS
    # =====================================================

    if len(WALLETS) >= 2:

        sender = WALLETS[0]
        receiver = WALLETS[1]

        amount = big_random()

        ensure_plus_balance(

            sender,
            usdc_plus,
            USDC,
            usdc_plus,
            amount,
            "MINT USDC+"

        )

        transfer_token(
            usdc_plus,
            sender,
            receiver,
            amount,
            "SEND USDC+"
        )

        random_sleep()

        transfer_token(
            usdc_plus,
            receiver,
            sender,
            amount,
            "RETURN USDC+"
        )

        random_sleep()

    print("\n========== CYCLE COMPLETE ==========\n")

# =========================================================
# LOOP
# =========================================================

def run_forever():

    while True:

        try:

            run_cycle()

        except Exception as e:

            print(f"[FATAL ERROR] {e}")

        sleep_time = random.randint(
            CYCLE_SLEEP_MIN,
            CYCLE_SLEEP_MAX
        )

        print(
            f"\nNEXT CYCLE IN "
            f"{round(sleep_time / 3600, 2)} HOURS\n"
        )

        time.sleep(sleep_time)

# =========================================================

if __name__ == "__main__":

    run_forever()
