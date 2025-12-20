import pandas as pd
import os
import numpy as np

onchain_data = pd.read_csv('eth_onchain_features.csv')
eth_price_data = pd.read_csv('ETH_dataset.csv')

# Convert the 'date' column in onchain_data to datetime format
onchain_data['date'] = pd.to_datetime(onchain_data['date'])

# Convert the 'timestamp' column in eth_price_data to datetime format
eth_price_data['timestamp'] = pd.to_datetime(eth_price_data['timestamp'])

# Merge the datasets on the 'date' in onchain and 'timestamp' in eth_price_data column
merged_data = pd.merge(eth_price_data,onchain_data, left_on='timestamp', right_on='date').drop('date', axis=1)

# merged_data.drop(['eth_burned', 'eth_issued', 'net_issuance', 'validator_rewards_eth', 'eth_issued_as_validator_rewards', 'total_fees_eth', 'avg_gas_used', 'avg_gas_limit', 'avg_gas_price_gwei', 'avg_tx_fee_eth', 'transaction_count', 'active_addresses'], axis=1, inplace=True)

merged_data.to_csv('merged_dataset.csv', index=False)


