# Haust Testnet Scripts

This repository contains a collection of Python scripts designed to interact with the Haust Testnet, a blockchain test network. These scripts enable users to deploy ERC20 tokens, mint NFTs, send tokens, and perform transactions using the Haust Testnet RPC. Each script is built with the web3.py library and provides bilingual support (English and Vietnamese) for user interaction.

Faucet: [HAUST](https://faucet.haust.app/)

## Features Overview

### General Features

- **Multi-Account Support**: Reads private keys from `pvkey.txt` to perform actions across multiple accounts.
- **Colorful CLI**: Uses `colorama` for visually appealing output with colored text and borders.
- **Asynchronous Execution**: Built with `asyncio` for efficient blockchain interactions.
- **Error Handling**: Comprehensive error catching for blockchain transactions and RPC issues.
- **Bilingual Support**: Supports both Vietnamese and English output based on user selection.

### Included Scripts

1. deploytoken.py: Deploy an ERC20 token contract on the Haust Testnet.
2. mintlabkit.py: Mint the "Haust Lab Kit" NFT.
3. mintnutrition.py: Mint the "Nutrition Medium" NFT.
4. mintpetri.py: Mint the "Haust Petri Dish" NFT.
5. sendtoken.py: Send ERC20 tokens to random addresses or addresses from a file.
6. sendtx.py: Send HAUST testnet transactions to random addresses or addresses from a file.
7. main.py: A unified script to run all the above functionalities from a single interface.

## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.8+
- `pip` (Python package manager)
- **Dependencies**: Install via `pip install -r requirements.txt` (ensure `web3.py`, `colorama`, `asyncio`, and `eth-account` are included).
- **pvkey.txt**: Add private keys (one per line) for wallet automation.
- Access to the Haust Testnet RPC (https://rpc-testnet.haust.app)
- **address.txt / addressERC20.txt**: Optional files for specifying recipient addresses.

## Installation

1. **Clone this repository:**
- Open cmd or Shell, then run the command:
```sh
git clone https://github.com/thog9/Haust-testnet.git
```
```sh
cd Haust-testnet
```
2. **Install Dependencies:**
- Open cmd or Shell, then run the command:
```sh
pip install -r requirements.txt
```
3. **Prepare Input Files:**
- Open the `pvkey.txt`: Add your private keys (one per line) in the root directory.
```sh
nano pvkey.txt 
```
- Open the `address.txt`(optional): Add recipient addresses (one per line) for `sendtx.py`, `deploytoken.py`, `sendtoken.py`.
```sh
nano address.txt 
```
```sh
nano addressERC20.txt
```
```sh
nano contractERC20.txt
```
4. **Run:**
- Open cmd or Shell, then run command:
```sh
python main.py
```
- Choose a language (Vietnamese/English).

## Contact

- **Telegram**: [thog099](https://t.me/thog099)
- **Channel**: [CHANNEL](https://t.me/thogairdrops)
- **Group**: [GROUP CHAT](https://t.me/thogchats)
- **X**: [Thog](https://x.com/thog099) 
