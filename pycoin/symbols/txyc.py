from pycoin.networks.bitcoinish import create_bitcoinish_network


network = create_bitcoinish_network(
    symbol="TXYC", network_name="Yamacoin", subnet_name="testnet",
    wif_prefix_hex="ef", address_prefix_hex="57", pay_to_script_prefix_hex="8c",
    bip32_prv_prefix_hex="04358394", bip32_pub_prefix_hex="043587cf", bech32_hrp="txyc",
    magic_header_hex="f1a587c1", default_port=18543,
    dns_bootstrap=[
        "dnsseed.testnet.yama-co.in"
    ])
