from pycoin.networks.bitcoinish import create_bitcoinish_network


network = create_bitcoinish_network(
    symbol="XPC", network_name="XPChain", subnet_name="mainnet",
    wif_prefix_hex="80", address_prefix_hex="4c", pay_to_script_prefix_hex="1c",
    bip32_prv_prefix_hex="0488ade4", bip32_pub_prefix_hex="0488b21e", bech32_hrp="xpc",
    magic_header_hex="fc87bac0", default_port=8798,
    dns_bootstrap=[
        "seed1.xpchain.io", "seed2.xpchain.io", "seed3.xpchain.io"
    ])
