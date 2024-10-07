import twstock

stock_now = twstock.realtime.get('2330')    # 擷取當前台積電股票資訊
stocks = twstock.realtime.get(['2330', '2337', '2409'])  # 擷取當前三檔資訊

best_bid_price = stock_now['realtime']['best_bid_price'][0]
print(stock_now)
print(best_bid_price)

stock_yesterday = twstock.Stock('2330').price[-2]
print(stock_yesterday)

# =============================================================================
# {'timestamp': 1718173800.0,
#  'info': {'code': '2330',
#   'channel': '2330.tw',
#   'name': '台積電',
#   'fullname': '台灣積體電路製造股份有限公司',
#   'time': '2024-06-12 14:30:00'},
#  'realtime': {'latest_trade_price': '909.0000',
#   'trade_volume': '6031',
#   'accumulate_trade_volume': '47989',
#   'best_bid_price': ['909.0000',
#    '908.0000',
#    '907.0000',
#    '906.0000',
#    '905.0000'],
#   'best_bid_volume': ['41', '299', '363', '321', '474'],
#   'best_ask_price': ['910.0000',
#    '911.0000',
#    '912.0000',
#    '913.0000',
#    '914.0000'],
#   'best_ask_volume': ['58', '63', '497', '184', '486'],
#   'open': '888.0000',
#   'high': '914.0000',
#   'low': '888.0000'},
#  'success': True}
# =============================================================================
