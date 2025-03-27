import os
import sys
import asyncio
import random
from web3 import Web3
from eth_account import Account
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Constants
NETWORK_URL = "https://rpc-testnet.haust.app"
CHAIN_ID = 1523903251
EXPLORER_URL = "https://explorer-testnet.haust.app/tx/0x"
CONTRACT_ADDRESS = "0xdaF34a049EfAa3cc9ad4635D8A710Fae819aca5c"
BORDER_WIDTH = 80

CONTRACT_ABI = [
    {
        "inputs": [{"internalType": "address", "name": "initialOwner", "type": "address"}],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {"inputs": [], "name": "ERC721EnumerableForbiddenBatchMint", "type": "error"},
    {"inputs": [{"internalType": "address", "name": "sender", "type": "address"}, {"internalType": "uint256", "name": "tokenId", "type": "uint256"}, {"internalType": "address", "name": "owner", "type": "address"}], "name": "ERC721IncorrectOwner", "type": "error"},
    {"inputs": [{"internalType": "address", "name": "operator", "type": "address"}, {"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "ERC721InsufficientApproval", "type": "error"},
    {"inputs": [{"internalType": "address", "name": "approver", "type": "address"}], "name": "ERC721InvalidApprover", "type": "error"},
    {"inputs": [{"internalType": "address", "name": "operator", "type": "address"}], "name": "ERC721InvalidOperator", "type": "error"},
    {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}], "name": "ERC721InvalidOwner", "type": "error"},
    {"inputs": [{"internalType": "address", "name": "receiver", "type": "address"}], "name": "ERC721InvalidReceiver", "type": "error"},
    {"inputs": [{"internalType": "address", "name": "sender", "type": "address"}], "name": "ERC721InvalidSender", "type": "error"},
    {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "ERC721NonexistentToken", "type": "error"},
    {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "uint256", "name": "index", "type": "uint256"}], "name": "ERC721OutOfBoundsIndex", "type": "error"},
    {"inputs": [], "name": "EnforcedPause", "type": "error"},
    {"inputs": [], "name": "ExpectedPause", "type": "error"},
    {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}], "name": "OwnableInvalidOwner", "type": "error"},
    {"inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "OwnableUnauthorizedAccount", "type": "error"},
    {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "owner", "type": "address"}, {"indexed": True, "internalType": "address", "name": "approved", "type": "address"}, {"indexed": True, "internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "Approval", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "owner", "type": "address"}, {"indexed": True, "internalType": "address", "name": "operator", "type": "address"}, {"indexed": False, "internalType": "bool", "name": "approved", "type": "bool"}], "name": "ApprovalForAll", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "previousOwner", "type": "address"}, {"indexed": True, "internalType": "address", "name": "newOwner", "type": "address"}], "name": "OwnershipTransferred", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "internalType": "address", "name": "account", "type": "address"}], "name": "Paused", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "from", "type": "address"}, {"indexed": True, "internalType": "address", "name": "to", "type": "address"}, {"indexed": True, "internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "Transfer", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "internalType": "address", "name": "account", "type": "address"}], "name": "Unpaused", "type": "event"},
    {"inputs": [{"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "approve", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}], "name": "balanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "getApproved", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "user", "type": "address"}], "name": "getUserMintStatus", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "address", "name": "operator", "type": "address"}], "name": "isApprovedForAll", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "owner", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "ownerOf", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "pause", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "name": "paused", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "renounceOwnership", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "name": "safeMint", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "tokenId", "type": "uint256"}, {"internalType": "bytes", "name": "data", "type": "bytes"}], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "operator", "type": "address"}, {"internalType": "bool", "name": "approved", "type": "bool"}], "name": "setApprovalForAll", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "bytes4", "name": "interfaceId", "type": "bytes4"}], "name": "supportsInterface", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "uint256", "name": "index", "type": "uint256"}], "name": "tokenByIndex", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "uint256", "name": "index", "type": "uint256"}], "name": "tokenOfOwnerByIndex", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "tokenURI", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "totalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "transferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}], "name": "transferOwnership", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "name": "unpause", "outputs": [], "stateMutability": "nonpayable", "type": "function"}
]

# Language dictionary
LANG = {
    'vi': {
        'title': 'MINT HAUST LAB KIT NFT - HAUST TESTNET',
        'info': 'Thông tin',
        'found': 'Tìm thấy',
        'wallets': 'ví',
        'processing_wallet': 'XỬ LÝ VÍ',
        'checking_balance': 'Kiểm tra số dư...',
        'insufficient_balance': 'Số dư không đủ',
        'preparing_tx': 'Chuẩn bị giao dịch...',
        'sending_tx': 'Đang gửi giao dịch...',
        'success': 'Mint Haust Lab Kit NFT thành công!',
        'failure': 'Mint thất bại',
        'address': 'Địa chỉ',
        'gas': 'Gas',
        'block': 'Khối',
        'balance': 'Số dư HAUST',
        'pausing': 'Tạm nghỉ',
        'completed': 'HOÀN THÀNH: {successful}/{total} GIAO DỊCH THÀNH CÔNG',
        'error': 'Lỗi',
        'connect_success': 'Thành công: Đã kết nối mạng Haust Testnet',
        'connect_error': 'Không thể kết nối RPC',
        'pvkey_not_found': 'File pvkey.txt không tồn tại',
        'pvkey_empty': 'Không tìm thấy private key hợp lệ',
        'pvkey_error': 'Đọc pvkey.txt thất bại',
        'invalid_key': 'không hợp lệ, bỏ qua',
        'warning_line': 'Cảnh báo: Dòng',
    },
    'en': {
        'title': 'MINT HAUST LAB KIT NFT - HAUST TESTNET',
        'info': 'Info',
        'found': 'Found',
        'wallets': 'wallets',
        'processing_wallet': 'PROCESSING WALLET',
        'checking_balance': 'Checking balance...',
        'insufficient_balance': 'Insufficient balance',
        'preparing_tx': 'Preparing transaction...',
        'sending_tx': 'Sending transaction...',
        'success': 'Successfully minted Haust Lab Kit NFT!',
        'failure': 'Mint failed',
        'address': 'Address',
        'gas': 'Gas',
        'block': 'Block',
        'balance': 'HAUST Balance',
        'pausing': 'Pausing',
        'completed': 'COMPLETED: {successful}/{total} TRANSACTIONS SUCCESSFUL',
        'error': 'Error',
        'connect_success': 'Success: Connected to Haust Testnet',
        'connect_error': 'Failed to connect to RPC',
        'pvkey_not_found': 'pvkey.txt file not found',
        'pvkey_empty': 'No valid private keys found',
        'pvkey_error': 'Failed to read pvkey.txt',
        'invalid_key': 'is invalid, skipped',
        'warning_line': 'Warning: Line',
    }
}

# Styled border
def print_border(text: str, color=Fore.CYAN, width=BORDER_WIDTH):
    text = text.strip()
    if len(text) > width - 4:
        text = text[:width - 7] + "..."
    padded_text = f" {text} ".center(width - 2)
    print(f"{color}┌{'─' * (width - 2)}┐{Style.RESET_ALL}")
    print(f"{color}│{padded_text}│{Style.RESET_ALL}")
    print(f"{color}└{'─' * (width - 2)}┘{Style.RESET_ALL}")

# Separator
def print_separator(color=Fore.MAGENTA):
    print(f"{color}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")

# Validate private key
def is_valid_private_key(key: str) -> bool:
    key = key.strip()
    if not key.startswith('0x'):
        key = '0x' + key
    try:
        bytes.fromhex(key.replace('0x', ''))
        return len(key) == 66
    except ValueError:
        return False

# Load private keys
def load_private_keys(file_path: str = "pvkey.txt", language: str = 'en') -> list:
    try:
        if not os.path.exists(file_path):
            print(f"{Fore.RED}  ✖ {LANG[language]['pvkey_not_found']}{Style.RESET_ALL}")
            sys.exit(1)
        valid_keys = []
        with open(file_path, 'r') as f:
            for i, line in enumerate(f, 1):
                key = line.strip()
                if key and not key.startswith('#'):
                    if is_valid_private_key(key):
                        if not key.startswith('0x'):
                            key = '0x' + key
                        valid_keys.append((i, key))
                    else:
                        print(f"{Fore.YELLOW}  ⚠ {LANG[language]['warning_line']} {i} {LANG[language]['invalid_key']}: {key}{Style.RESET_ALL}")
        if not valid_keys:
            print(f"{Fore.RED}  ✖ {LANG[language]['pvkey_empty']}{Style.RESET_ALL}")
            sys.exit(1)
        return valid_keys
    except Exception as e:
        print(f"{Fore.RED}  ✖ {LANG[language]['pvkey_error']}: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)

# Connect to Web3
def connect_web3(language: str = 'en'):
    w3 = Web3(Web3.HTTPProvider(NETWORK_URL))
    if not w3.is_connected():
        print(f"{Fore.RED}  ✖ {LANG[language]['connect_error']}{Style.RESET_ALL}")
        sys.exit(1)
    print(f"{Fore.GREEN}  ✔ {LANG[language]['connect_success']} │ Chain ID: {w3.eth.chain_id}{Style.RESET_ALL}")
    return w3

# Mint NFT
async def mint_nft(w3, private_key, wallet_index, language: str = 'en'):
    account = Account.from_key(private_key)
    sender_address = account.address
    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

    try:
        print(f"{Fore.CYAN}  > {LANG[language]['checking_balance']}{Style.RESET_ALL}")
        eth_balance = float(w3.from_wei(w3.eth.get_balance(sender_address), 'ether'))
        if eth_balance < 0.001:
            print(f"{Fore.RED}  ✖ {LANG[language]['insufficient_balance']}: {eth_balance:.4f} HAUST < 0.001 HAUST{Style.RESET_ALL}")
            return False

        print(f"{Fore.CYAN}  > {LANG[language]['preparing_tx']}{Style.RESET_ALL}")
        nonce = w3.eth.get_transaction_count(sender_address)
        tx_params = contract.functions.safeMint().build_transaction({
            'nonce': nonce,
            'from': sender_address,
            'chainId': CHAIN_ID,
            'gas': 400000,
            'gasPrice': w3.to_wei(20, 'gwei')
        })

        print(f"{Fore.CYAN}  > {LANG[language]['sending_tx']}{Style.RESET_ALL}")
        signed_tx = w3.eth.account.sign_transaction(tx_params, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        tx_link = f"{EXPLORER_URL}{tx_hash.hex()}"

        receipt = await asyncio.get_event_loop().run_in_executor(None, lambda: w3.eth.wait_for_transaction_receipt(tx_hash, timeout=180))

        if receipt.status == 1:
            print(f"{Fore.GREEN}  ✔ {LANG[language]['success']} │ Tx: {tx_link}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}    {LANG[language]['address']:<12}: {sender_address}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}    {LANG[language]['block']:<12}: {receipt['blockNumber']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}    {LANG[language]['gas']:<12}: {receipt['gasUsed']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}    {LANG[language]['balance']:<12}: {eth_balance:.4f} HAUST{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}  ✖ {LANG[language]['failure']} │ Tx: {tx_link}{Style.RESET_ALL}")
            return False
    except Exception as e:
        print(f"{Fore.RED}  ✖ {LANG[language]['failure']}: {str(e)}{Style.RESET_ALL}")
        return False

# Main function
async def run_mintlabkit(language: str = 'en'):
    print()
    print_border(LANG[language]['title'], Fore.CYAN)
    print()

    private_keys = load_private_keys('pvkey.txt', language)
    print(f"{Fore.YELLOW}  ℹ {LANG[language]['info']}: {LANG[language]['found']} {len(private_keys)} {LANG[language]['wallets']}{Style.RESET_ALL}")
    print()

    w3 = connect_web3(language)
    print()

    successful_mints = 0
    total_mints = len(private_keys)

    random.shuffle(private_keys)
    for i, (profile_num, private_key) in enumerate(private_keys, 1):
        print_border(f"{LANG[language]['processing_wallet']} {profile_num} ({i}/{len(private_keys)})", Fore.MAGENTA)
        print()

        if await mint_nft(w3, private_key, profile_num, language):
            successful_mints += 1

        if i < len(private_keys):
            delay = random.uniform(10, 30)
            print(f"{Fore.YELLOW}  ℹ {LANG[language]['pausing']} {delay:.2f} {'giây' if language == 'vi' else 'seconds'}{Style.RESET_ALL}")
            await asyncio.sleep(delay)
        print_separator()

    print()
    print_border(f"{LANG[language]['completed'].format(successful=successful_mints, total=total_mints)}", Fore.GREEN)
    print()

if __name__ == "__main__":
    asyncio.run(run_mintlabkit('en'))
