def check_market_status(change_percent):
    if change_percent > 1:
        return "Market is strongly UP 📈"
    elif change_percent < -1:
        return "Market is strongly DOWN 📉"
    else:
        return "Market is relatively flat"

status = check_market_status(2.1)
print(status)
