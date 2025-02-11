import random
import time
import os
import asyncio
from web3 import Web3
from eth_account import Account
from colorama import Fore, Style, init
import sys

# Khởi tạo colorama
init(autoreset=True)

# Cấu hình mạng
network_url = "https://rpc-testnet.haust.app"
chain_id = 1523903251
explorer_url = "https://explorer-testnet.haust.app/tx/0x"  # URL cơ sở cho explorer

# Constants for NFT minting
CONTRACT_ADDRESS_1 = "0x6B3f185C4c9246c52acE736CA23170801D636c8E"  # NFT1
CONTRACT_ADDRESS_2 = "0x28e50a3632961dA179b2Afca4675714ea22E7BB7"  # NFT2
CONTRACT_ABI_1 = [

    {
        "inputs": [
            {
                "internalType": "address",
                "name": "initialOwner",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "ERC721EnumerableForbiddenBatchMint",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "ERC721IncorrectOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "ERC721InsufficientApproval",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "approver",
                "type": "address"
            }
        ],
        "name": "ERC721InvalidApprover",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            }
        ],
        "name": "ERC721InvalidOperator",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "ERC721InvalidOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "receiver",
                "type": "address"
            }
        ],
        "name": "ERC721InvalidReceiver",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address"
            }
        ],
        "name": "ERC721InvalidSender",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "ERC721NonexistentToken",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "ERC721OutOfBoundsIndex",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "EnforcedPause",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ExpectedPause",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "OwnableInvalidOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "OwnableUnauthorizedAccount",
        "type": "error"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "approved",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "approved",
                "type": "bool"
            }
        ],
        "name": "ApprovalForAll",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "Paused",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "Unpaused",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "getApproved",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "getUserMintStatus",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            }
        ],
        "name": "isApprovedForAll",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "ownerOf",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "pause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "paused",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "safeMint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "approved",
                "type": "bool"
            }
        ],
        "name": "setApprovalForAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes4",
                "name": "interfaceId",
                "type": "bytes4"
            }
        ],
        "name": "supportsInterface",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "tokenByIndex",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "tokenOfOwnerByIndex",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "tokenURI",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "unpause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
    
]

CONTRACT_ABI_2 = [
    
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "initialOwner",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "ERC721EnumerableForbiddenBatchMint",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "ERC721IncorrectOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "ERC721InsufficientApproval",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "approver",
                "type": "address"
            }
        ],
        "name": "ERC721InvalidApprover",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            }
        ],
        "name": "ERC721InvalidOperator",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "ERC721InvalidOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "receiver",
                "type": "address"
            }
        ],
        "name": "ERC721InvalidReceiver",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address"
            }
        ],
        "name": "ERC721InvalidSender",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "ERC721NonexistentToken",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "ERC721OutOfBoundsIndex",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "EnforcedPause",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ExpectedPause",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "OwnableInvalidOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "OwnableUnauthorizedAccount",
        "type": "error"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "approved",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "approved",
                "type": "bool"
            }
        ],
        "name": "ApprovalForAll",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "Paused",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "Unpaused",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "getApproved",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "getUserMintStatus",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            }
        ],
        "name": "isApprovedForAll",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "ownerOf",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "pause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "paused",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "safeMint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "approved",
                "type": "bool"
            }
        ],
        "name": "setApprovalForAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes4",
                "name": "interfaceId",
                "type": "bytes4"
            }
        ],
        "name": "supportsInterface",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "tokenByIndex",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "tokenOfOwnerByIndex",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "tokenURI",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "unpause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

MAX_CONCURRENT = 1

# Hàm đọc private key từ file key.txt
def read_private_key():
    try:
        with open('pvkey.txt', 'r') as file:
            private_keys = []
            for line in file:
                trimmed_key = line.strip()
                if len(trimmed_key) in [64, 66]: 
                    private_keys.append(trimmed_key)
            if not private_keys:
                raise ValueError("Không tìm thấy private key hợp lệ trong file.")
            return private_keys
    except FileNotFoundError:
        print(Fore.RED + "Lỗi: Không tìm thấy file key.txt!")
        sys.exit(1)  
    except Exception as e:
        print(Fore.RED + f"Lỗi khi đọc file key.txt: {str(e)}")
        sys.exit(1)

# Kết nối đến mạng Sonic Testnet
private_keys = read_private_key()  
web3 = Web3(Web3.HTTPProvider(network_url))

# Kiểm tra kết nối
if not web3.is_connected():
    raise Exception("Không thể kết nối đến mạng")

# Hàm hiển thị banner
def _banner():
    print(r"""


██╗  ██╗ █████╗ ██╗   ██╗███████╗████████╗    ████████╗███████╗███████╗████████╗███╗   ██╗███████╗████████╗
██║  ██║██╔══██╗██║   ██║██╔════╝╚══██╔══╝    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝████╗  ██║██╔════╝╚══██╔══╝
███████║███████║██║   ██║███████╗   ██║          ██║   █████╗  ███████╗   ██║   ██╔██╗ ██║█████╗     ██║   
██╔══██║██╔══██║██║   ██║╚════██║   ██║          ██║   ██╔══╝  ╚════██║   ██║   ██║╚██╗██║██╔══╝     ██║   
██║  ██║██║  ██║╚██████╔╝███████║   ██║          ██║   ███████╗███████║   ██║   ██║ ╚████║███████╗   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝          ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝   ╚═╝   
                                                                                                           

    """)
    print(Fore.GREEN + Style.BRIGHT + "HAUST TESTNET")
    print(Fore.RED + Style.BRIGHT + "Liên hệ: https://t.me/thog099")
    print(Fore.BLUE + Style.BRIGHT + "Replit: Thog")
    print("")

# Hàm xóa màn hình
def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Lựa chọn ngôn ngữ
def select_language():
    while True:
        print()
        print(Fore.YELLOW + "Chọn ngôn ngữ:")
        print(Fore.CYAN + "1. Tiếng Việt")
        print(Fore.CYAN + "2. English")
        choice = input(Fore.GREEN + "Nhập lựa chọn (1/2): ")

        if choice == '1':
            return 'vi'
        elif choice == '2':
            return 'en'
        else:
            print(Fore.RED + "Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")
            print()

# Tin nhắn dựa trên ngôn ngữ
def get_messages(language):
    messages_dict = {
        "vi": {  # Thông điệp tiếng Việt
            "menu": "Chọn menu:",
            'send_transaction': "Gửi TX ngẫu nhiên",
            'mint_nft': "Mint NFT (Nutrition Medium NFT & Haust Petri Dish)",
            'exit': "Thoát",
            'success': Fore.GREEN + "Giao dịch thành công! Liên kết: {}" + Style.RESET_ALL,
            'failure': Fore.RED + "Giao dịch thất bại. Liên kết: {}" + Style.RESET_ALL,
            'sender': "Địa chỉ người gửi: {}",
            'receiver': "Địa chỉ người nhận: {}",
            'amount': "Số lượng HAUST đã gửi: {} HAUST",
            'gas': "Gas đã sử dụng: {}",
            'block': "Số khối: {}",
            'balance': "Số dư hiện tại: {} HAUST",
            'total': "Tổng giao dịch thành công: {}",
            'amount_prompt': "Nhập số lượng HAUST muốn gửi (mặc định 0.000001, tối đa 0.0001): ",
            'tx_menu': "Chọn một giao dịch.",
            'mint_menu': "Bắt đầu quá trình mint NFT.",
            'exit_menu': "Thoát khỏi hệ thống.",
            'wallet_info': "Minting from wallet: {} (Attempt {})",
            'minting_nft': "Minting from {} NFT contract ({}):",
            'transaction_sent': "Giao dịch đã được gửi. Đang chờ xác nhận (NFT{})...",
            'nft_minted': "NFT đã được mint! TX Hash: {}",
            'explorer_link': "🔗 Liên kết Explorer: {}",
            'retrying_error': "Lỗi khi mint cho ví {}... {}. Đang thử lại lần {}...",
            'skipped': "🚫 Bỏ qua {} sau 3 lần thử không thành công.",
            'mint_query': "Bạn có muốn mint NFT Haust Petri Dish (PetriDish) không? (y/n): ",
            'mint_yes': "Bạn đã chọn mint NFT Haust Petri Dish (PetriDish).",
            'mint_no': "Bạn đã chọn không mint NFT Haust Petri Dish (PetriDish).",
            'invalid_input': "Đầu vào không hợp lệ. Vui lòng nhập 'có' hoặc 'không'.",
            'all_transactions_processed': Fore.YELLOW + "Tất cả giao dịch đã được xử lý!" + Style.RESET_ALL
        },
        "en": {  # Thông điệp tiếng Anh
            'menu': "Choose a menu:",
            'send_transaction': "Send Transaction Random",
            'mint_nft': "Mint NFT (Nutrition Medium NFT & Haust Petri Dish)",
            'exit': "Exit",
            'success': Fore.GREEN + "Transaction successful! Link: {}" + Style.RESET_ALL,
            'failure': Fore.RED + "Transaction failed. Link: {}" + Style.RESET_ALL,
            'sender': "Sender address: {}",
            'receiver': "Receiver address: {}",
            'amount': "Amount HAUST sent: {} HAUST",
            'gas': "Gas used: {}",
            'block': "Block number: {}",
            'balance': "Current balance: {} HAUST",
            'total': "Total successful: {}",
            'amount_prompt': "Enter the amount of HAUST to send (default 0.000001, maximum 0.0001): ",
            'tx_menu': "Choose a transaction.",
            'mint_menu': "Starting the NFT minting process.",
            'exit_menu': "Exiting the system.",
            'wallet_info': "Minting from wallet: {} (Attempt {})",
            'minting_nft': "Minting from {} NFT contract ({}):",
            'transaction_sent': "Transaction sent. Waiting for confirmation (NFT{})...",
            'nft_minted': "NFT minted! TX Hash: {}",
            'explorer_link': "🔗 Explorer Link: {}",
            'retrying_error': "Error minting for wallet {}... {}. Retrying attempt {}...",
            'skipped': "🚫 Skipping {} after 3 failed attempts.",
            'mint_query': "Do you want to mint NFT Haust Petri Dish (PetriDish) as well? (y/n): ",
            'mint_yes': "You have chosen to mint NFT Haust Petri Dish (PetriDish).",
            'mint_no': "You have chosen not to mint NFT Haust Petri Dish (PetriDish).",
            'invalid_input': "Invalid input. Please enter 'yes' or 'no'.",
            'all_transactions_processed': Fore.YELLOW + "All transactions processed!" + Style.RESET_ALL
        }
    }
    return messages_dict.get(language, messages_dict["vi"])  # Mặc định là tiếng Việt

# Lựa chọn số lượng token
def select_amount(language):
    messages = get_messages(language)
    while True:
        try:
            amount = float(input(Fore.GREEN + messages['amount_prompt']) or 0.000001)
            if 0 < amount <= 0.0001:
                return amount
            else:
                print(Fore.RED + "Số lượng không hợp lệ. Số lượng phải lớn hơn 0 và không quá 0.0001.")
        except ValueError:
            print(Fore.RED + "Dữ liệu không hợp lệ. Vui lòng nhập số.")

# Hàm gửi giao dịch
def send_transaction(private_key, to_address, amount):
    account = Account.from_key(private_key)
    sender_address = account.address

    # Tạo giao dịch
    nonce = web3.eth.get_transaction_count(sender_address) 
    tx = {
        'nonce': nonce,
        'to': Web3.to_checksum_address(to_address),  
        'value': web3.to_wei(amount, 'ether'),  
        'gas': 21000,  
        'gasPrice': web3.eth.gas_price,
        'chainId': chain_id
    }

    # Ký giao dịch
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)

    # Gửi giao dịch
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

    # Chờ giao dịch được đưa vào khối
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    return tx_hash.hex(), tx_receipt, amount

# Địa chỉ ngẫu nhiên với checksum
def get_random_address():
    random_address = '0x' + ''.join(random.choices('0123456789abcdef', k=40))
    return Web3.to_checksum_address(random_address)

# Hàm mint NFT
async def mint_nfts(private_key, mint_nft_1, language, attempt=1):
    messages = get_messages(language)  
    wallet = Account.from_key(private_key).address

    print(Fore.MAGENTA + "\n=====================***=====================")
    print(Fore.MAGENTA + messages['wallet_info'].format(wallet, attempt))
    print(Fore.MAGENTA + "=====================***=====================")
    print(Fore.GREEN + "\n")
    
    gas_limit = 400000
    gas_price = Web3.to_wei(20, 'gwei')

    try:
        # Mint NFT đầu tiên
        if mint_nft_1:
            contract_1 = web3.eth.contract(address=CONTRACT_ADDRESS_1, abi=CONTRACT_ABI_1)
            print(Fore.CYAN + messages['minting_nft'].format("Haust Petri Dish (PetriDish)", CONTRACT_ADDRESS_1))
            print(Fore.GREEN + "\n")
            tx1 = contract_1.functions.safeMint().build_transaction({
                'from': wallet, 'gas': gas_limit, 'gasPrice': gas_price, 'nonce': web3.eth.get_transaction_count(wallet)
            })
            signed_tx1 = web3.eth.account.sign_transaction(tx1, private_key)
            tx_hash1 = web3.eth.send_raw_transaction(signed_tx1.raw_transaction)
            print(Fore.YELLOW + messages['transaction_sent'].format(1))
            print(Fore.GREEN + "\n")
            receipt1 = web3.eth.wait_for_transaction_receipt(tx_hash1)
            print(Fore.GREEN + messages['nft_minted'].format(receipt1.transactionHash.hex()))
            print(Fore.BLUE + messages['explorer_link'].format(explorer_url + receipt1.transactionHash.hex()))
        else:
            print(Fore.RED + messages['mint_no'])

        # Mint NFT thứ hai
        print(Fore.GREEN + "\n\n*****************")
        contract_2 = web3.eth.contract(address=CONTRACT_ADDRESS_2, abi=CONTRACT_ABI_2)
        print(Fore.CYAN + messages['minting_nft'].format("Nutrition Medium NFT (NutritionMedium)", CONTRACT_ADDRESS_2))
        print(Fore.GREEN + "\n")
        tx2 = contract_2.functions.safeMint().build_transaction({
            'from': wallet, 'gas': gas_limit, 'gasPrice': gas_price, 'nonce': web3.eth.get_transaction_count(wallet)
        })
        signed_tx2 = web3.eth.account.sign_transaction(tx2, private_key)
        tx_hash2 = web3.eth.send_raw_transaction(signed_tx2.raw_transaction)
        print(Fore.YELLOW + messages['transaction_sent'].format(2))
        print(Fore.GREEN + "\n")
        receipt2 = web3.eth.wait_for_transaction_receipt(tx_hash2)
        print(Fore.GREEN + messages['nft_minted'].format(receipt2.transactionHash.hex()))
        print(Fore.BLUE + messages['explorer_link'].format(explorer_url + receipt2.transactionHash.hex()))

    except Exception as e:
        print(Fore.RED + messages['retrying_error'].format(private_key[:6], str(e), attempt))
        if attempt < 3:
            return await mint_nfts(private_key, mint_nft_1, language, attempt + 1)
        else:
            print(Fore.RED + messages['skipped'].format(private_key[:6]))

async def process_keys(mint_nft_1, language):
    private_keys = read_private_key()  
    print(Fore.YELLOW + f"\n🔹 Found {len(private_keys)} private keys. Processing with {MAX_CONCURRENT} concurrent threads.")

    index = 0
    while index < len(private_keys):
        batch = private_keys[index:index + MAX_CONCURRENT]
        await asyncio.gather(*(mint_nfts(key, mint_nft_1, language) for key in batch))
        index += MAX_CONCURRENT

    messages = get_messages(language)
    print(Fore.YELLOW + "\n" + messages["all_transactions_processed"])

async def main(language):
    messages = get_messages(language)
    while True:
        mint_nft_1_input = input(Fore.GREEN + messages['mint_query']).strip().lower()
        if mint_nft_1_input in ['có', 'yes', 'y']:
            print(Fore.GREEN + messages['mint_yes'])
            mint_nft_1 = True
            break
        elif mint_nft_1_input in ['không', 'no', 'n']:
            print(Fore.RED + messages['mint_no'])
            mint_nft_1 = False
            break
        else:
            print(Fore.RED + messages['invalid_input'])
    
    await process_keys(mint_nft_1, language)

# Hàm chính
def menu():
    _clear()
    _banner()
    language = select_language()
    messages = get_messages(language)

    while True:
        _clear()
        _banner()  
        print(Fore.YELLOW + messages['menu'])  
        print(Fore.CYAN + "1. " + messages['send_transaction'])  
        print(Fore.CYAN + "2. " + messages['mint_nft'])  
        print(Fore.CYAN + "3. " + messages['exit']) 
        
        choice = input(Fore.GREEN + "Nhập lựa chọn (1/2/3): ")

        if choice == '1':
            _clear()
            _banner()
            print(Fore.YELLOW + messages['tx_menu'])
            amount = select_amount(language)
            count = 0
            for private_key in private_keys:
                to_address = get_random_address()
                try:
                    tx_hash, tx_receipt, sent_amount = send_transaction(private_key, to_address, amount)

                    tx_link = explorer_url + tx_hash  
                    formatted_amount = f"{sent_amount:.6f}"

                    if tx_receipt['status'] == 1:
                        current_balance = web3.eth.get_balance(Web3.to_checksum_address(Account.from_key(private_key).address))
                        formatted_balance = f"{web3.from_wei(current_balance, 'ether'):.6f}"
                        print(Fore.GREEN + messages['success'].format(Fore.GREEN + tx_link + Style.RESET_ALL))
                        print(Fore.YELLOW + messages['sender'].format(Account.from_key(private_key).address))
                        print(Fore.YELLOW + messages['receiver'].format(to_address))
                        print(Fore.YELLOW + messages['amount'].format(formatted_amount))
                        print(Fore.YELLOW + messages['gas'].format(tx_receipt['gasUsed']))
                        print(Fore.YELLOW + messages['block'].format(tx_receipt['blockNumber']))
                        print(Fore.YELLOW + messages['balance'].format(formatted_balance))
                        count += 1
                    else:
                        print(Fore.RED + messages['failure'].format(Fore.RED + tx_link + Style.RESET_ALL))
                        print(Fore.YELLOW + messages['sender'].format(Account.from_key(private_key).address))
                        print(Fore.YELLOW + messages['receiver'].format(to_address))
                        print(Fore.YELLOW + messages['amount'].format(formatted_amount))
                        print(Fore.YELLOW + messages['gas'].format(tx_receipt['gasUsed']))
                        print(Fore.YELLOW + messages['block'].format(tx_receipt['blockNumber']))
                except Exception as e:
                    print(Fore.RED + f"Lỗi khi gửi giao dịch với private key {private_key}: {str(e)}")

            print(Fore.YELLOW + f"Tổng giao dịch thành công: {count}")
            input(Fore.GREEN + "Nhấn Enter để tiếp tục...")
        elif choice == '2':
            _clear()
            _banner()
            print(Fore.YELLOW + messages['mint_menu'])
            asyncio.run(main(language))  # Gọi hàm mint với biến language
            input(Fore.GREEN + "Nhấn Enter để tiếp tục...")
        elif choice == '3':
            print(Fore.RED + messages['exit_menu'])
            break

if __name__ == "__main__":
    menu()
