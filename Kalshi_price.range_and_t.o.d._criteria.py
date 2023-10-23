# Kalshi create order (buy) criteria
# Add to API client script

# check if trading is active on the exchange
exchange_client.get_exchange_status()
if 'true' in ['trading_active']:  # or something like this

# fetch market data (get request)
market_data = exchange_client.get_market(parameters) # input parameter args

# set 'last executed price' range to target
# 1st condition
if market_data['last_price'] > low.number and < high.number:
    # Pick range of day with less volatility
    # Avoid beginning and end of day
    #2nd condition
    if time_of_day >= 12 pm (Central Time) and <= 2 pm (Central Time):  # in between 12 and 2 pm
        # create order with buy criteria
        create_order(parameters)


# Example: if holding QQQ and the price of daily "down" contract is between 60 and 80 cents between the hours of 12-2 pm, buy "down" contract to hedge, but if the price of daily "up" contract is between these amounts (or a different range you want to set), then buy "up" contract to supplement gains of underlying (QQQ)

# If wanting to practice in demo, you would probably have to switch between production (to get price data) and demo (to buy "test" contracts).

# Next, what if the criteria is met and then the market changes its mind (as it so often does)

# Set sell criteria in case of reversal
