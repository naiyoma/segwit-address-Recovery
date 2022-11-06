from bitcoinlib.wallets import Wallet

seedphrase = "torch spy holiday thunder useless atom blanket fragile canyon industry hawk faith slender tray horse mobile dash modify close purchase rely expand country armor"
def wallet_recovery(seedphrase):
    wallet_name = "ttttt"
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