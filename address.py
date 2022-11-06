from bitcoinlib.wallets import Wallet

seedphrase = "<entre seed phrase>"
def wallet_recovery(seedphrase):
    wallet_name = "<entre with walletname>"
    witness_type = "segwit"
    network = "regtest"
    w = Wallet.create(
        wallet_name, 
        witness_type= witness_type, 
        keys=seedphrase, 
        network=network
    )
    WalletKeys = (w.get_keys())
    address = [i.address for i in WalletKeys]
    print(address)


wallet_recovery(seedphrase)