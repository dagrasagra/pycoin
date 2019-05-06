from pycoin.networks.bitcoinish import create_bitcoinish_network


network = create_bitcoinish_network(
    symbol="XYC", network_name="Yamacoin", subnet_name="mainnet",
    wif_prefix_hex="80", address_prefix_hex="1c", pay_to_script_prefix_hex="4e",
    bip32_prv_prefix_hex="0488ade4", bip32_pub_prefix_hex="0488b21e", bech32_hrp="xyc",
    magic_header_hex="f1a585c0", default_port=8543,
    dns_bootstrap=[
        "dnsseed.yama-co.in"
    ])
