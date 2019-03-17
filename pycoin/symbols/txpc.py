from pycoin.networks.bitcoinish import create_bitcoinish_network


network = create_bitcoinish_network(
    symbol="TXPC", network_name="XPChain", subnet_name="testnet",
    wif_prefix_hex="ef", address_prefix_hex="8a", pay_to_script_prefix_hex="58",
    bip32_prv_prefix_hex="04358394", bip32_pub_prefix_hex="043587cf", bech32_hrp="txpc",
    magic_header_hex="fc87bbc1", default_port=18798,
    dns_bootstrap=[
        "seed1.xpchain.io", "seed2.xpchain.io", "seed3.xpchain.io"
    ])
