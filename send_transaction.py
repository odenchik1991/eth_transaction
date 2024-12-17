
from web3 import Web3

# Connect to Ethereum Testnet (Goerli or Sepolia)
infura_url = "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected
if web3.isConnected():
    print("Connected to Ethereum Testnet!")
else:
    print("Failed to connect.")
    exit()

# Sender details (replace with your test wallet details)
sender_address = "YOUR_WALLET_ADDRESS"
private_key = "YOUR_PRIVATE_KEY"

# Recipient address
recipient_address = input("Enter recipient Ethereum wallet address: ")

# Get transaction nonce
nonce = web3.eth.getTransactionCount(sender_address)

# Create a transaction
tx = {
    'nonce': nonce,
    'to': recipient_address,
    'value': web3.toWei(0.01, 'ether'),
    'gas': 21000,
    'gasPrice': web3.toWei('50', 'gwei'),
    'chainId': 5  # Goerli Testnet chain ID
}

# Sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key)

# Send the transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(f"Transaction sent! TX Hash: {web3.toHex(tx_hash)}")
