def log_trade(action, timestamp, details):
    with open('trades_log.txt', 'a') as log_file:
        log_file.write(f"{timestamp}: {action} - {details}\n")

# Example usage:
action = 'Buy'
timestamp = '2023-11-14 12:30:00'
details = 'Symbol: XYZ, Quantity: 10, Price: $50.00'
log_trade(action, timestamp, details)