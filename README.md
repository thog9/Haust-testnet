# Haust BOT
Faucet: [HAUST](https://faucet.haust.app/)

## Features:

*Allow multi-threading to mint NFTs faster.

*Support multiple Wallets and Private Keys
*Automatically send transactions from multiple addresses
*Monitor and update nonce for each private key to avoid conflicts when sending transactions.
*Catch exceptions when transactions fail and handle errors related to nonce (e.g. nonce is too low).
*Provide language options (Vietnamese or English) for users.
*Display transaction status notifications (successful or failed) along with detailed information.
*Calculate and display completion time of all transactions.
*Make all transactions, notifications, etc. pretty and easy to see.

## Module:

- Python 3.7 or later
- `pip` (Python package installer)

## Installation
1. **Clone this repository:**
- Open cmd or Shell, then run the command:
```sh
git clone https://github.com/thog9/Haust-testnet.git
```
``sh
cd Haust-testnet
```
2. **Install Module:**
- Open cmd or Shell, then run the command:
```sh
pip install -r requirements.txt
```
3. **Config:**
- Open the `bot.py` file and make sure to replace `private_key` with your valid private key.:
```sh
nano key.txt
```
4. **Run:**
- Open cmd or Shell, then run command:
```sh
python bot.py
```