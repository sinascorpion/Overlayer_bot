# Overlayer Sepolia Bot

Automatic Python bot for:

https://t.me/irdropper/6675

## Features

- Auto Faucet USDC
- Auto Mint USDC+
- Auto Stake USDC+
- Auto Bridge USDC+
- Multi Wallet Support
- Multi RPC Failover
- Auto Skip Approved Tokens
- Auto Skip Faucet If Balance Exists
- 24 Hour Auto Loop
- Random Sleep Between Transactions
- RPC Auto Switch

<a href="https://nowpayments.io/embeds/donation-widget?api_key=8b06749b-45a1-43aa-983f-986d9d6f38cf">
  <img src="https://github.com/sinascorpion/Arweave-Academy/blob/main/buymeacoffe.png?raw=true" width="200" alt="Donate">
</a>

# Educational / Testnet Use Only

This repository is intended for:

- Educational purposes
- Smart contract interaction learning
- Ethereum Sepolia testnet usage only

This software is NOT intended for:

- Mainnet automation
- Financial usage
- Production trading
- Exploitation or abuse

Use at your own risk.

# No Warranty

The author is not responsible for:

- Lost funds
- Misuse
- Account bans
- Smart contract risks
- RPC failures

# Open Source Notice

Before using this software:

- Review the source code
- Use burner wallets
- Never use wallets containing real assets
---

# Requirements

- Python 3.10+
---
# Linux Ubuntu Setup

# 1. Get source
```bash
git clone https://github.com/sinascorpion/Overlayer_bot.git
cd Overlayer_bot
```

# 2. Install Python

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

---

# 3. Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

If successful:

```bash
(.venv)
```

---

# 4. Install Requirements

```bash
pip install web3 python-dotenv eth-account
```

---

# 5. Edit .env

```bash
nano .env
```

Example:

```env
PRIVATE_KEYS=PRIVATE_KEY_1,PRIVATE_KEY_2,PRIVATE_KEY_3
```

Notes:

- No spaces
- Separate with commas
- Wallet address not required
- Only private keys

Save:

```bash
CTRL + X
Y
ENTER
```

---

# 6. Run Bot

```bash
python bot.py
```

---
# Windows Setup

## 1. Install Python

Download Python:

https://www.python.org/downloads/

IMPORTANT:

During installation enable:

```txt
Add Python to PATH
```

---

## 2. Download and unzip the source: [Github link](https://github.com/sinascorpion/Overlayer_bot/archive/refs/heads/main.zip)

# Go to the folder, right-click in a free area, and open with PowerShell (In Windows 10 hold down SHIFT + Right click)

<img width="268" height="281" alt="Untitled-2021-01-05T092634 702" src="https://github.com/user-attachments/assets/052702ce-791f-41d6-aafd-1b4a37b33d08" />

---

## 3. Create Virtual Environment

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\activate
```

If successful:

```txt
(.venv)
```

---

## 4. Install Requirements

```powershell
pip install web3 python-dotenv eth-account
```

---

## 5. Create .env

Create file:

```txt
.env
```

Example:

```env
PRIVATE_KEYS=PRIVATE_KEY_1,PRIVATE_KEY_2
```

---

## 6. Run Bot

```powershell
python bot.py
```

---

# Example Logs

```txt
[TEST RPC] https://sepolia.rpc.sentio.xyz
[OK] BLOCK => 10906659

========== START CYCLE ==========

[Wallet 1] 0x123... => FAUCET
TX => 0xabc...
CONFIRMED

SLEEP 35s

[Wallet 1] 0x123... => MINT 1/20
TX => 0xdef...
CONFIRMED
```

---

# Auto Cycle

After completing:

- Faucet
- Mint
- Stake
- Bridge

The bot waits 24 hours and starts again automatically.

---

# Faucet Logic

If wallet USDC balance is greater than 2000:

```txt
FAUCET SKIPPED
```

The faucet transaction will be skipped.

---

# Approve Logic

If token is already approved:

```txt
USDC APPROVED ALREADY
```

or:

```txt
USDC+ APPROVED ALREADY
```

Approve transaction will be skipped.

---

# Stop Bot

```bash
CTRL + C
```

---

# Run Bot In Background

Install screen:

```bash
sudo apt install screen -y
```

Create session:

```bash
screen -S overlayer
```

Run bot:

```bash
python bot.py
```

Detach without stopping:

```bash
CTRL + A
D
```

Reconnect:

```bash
screen -r overlayer
```

---

# Security Warning

Never share:

- `.env`
- private keys

---

# Disclaimer

This bot is intended for Ethereum Sepolia testnet only.

Use at your own risk.

---

# Telegram channel: [https://t.me/irdropper](https://t.me/irdropper)
