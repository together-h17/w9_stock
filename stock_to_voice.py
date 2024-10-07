import twstock
from gtts import gTTS
import pygame
import time
import os
import uuid

# 初始化 Pygame Mixer
pygame.mixer.init()

# 設置股票代碼和名稱，可以繼續加
stocks = {
    '3105': '穩懋',
    '2330': '台積電',
    '2317': '鴻海',
    '2454': '聯發科'
    
}

#取得及時股票資訊
def get_stock_data(symbol):
    stock = twstock.realtime.get(symbol)
    if stock is not None:
        current_price = float(stock['realtime']['best_bid_price'][0])   #用五檔最高買入價代替
        if(current_price == 0):
            current_price = float(stock['realtime']['high'])            #漲停直接取最高價
        yesterday_price = float(twstock.Stock(symbol).price[-1])
        change = current_price - yesterday_price
        change_percent = (change / yesterday_price) * 100
        return current_price, change, change_percent
    else:
        return None, None, None  

#文字轉語音
def text_to_speech(text, lang='zh'):
    tts = gTTS(text=text, lang=lang)
    filename = f"stock_{uuid.uuid4()}.mp3" #uuid是隨機生成的唯一識別編碼
    tts.save(filename)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # 等待音檔播放結束
        time.sleep(0.1)
    # 刪除檔案避免文件占用
    pygame.mixer.music.unload()
    os.remove(filename)

while True:
    for symbol, name in stocks.items():
        price, change, change_percent = get_stock_data(symbol)
        if price is not None:
            text = f"目前{name}的價格是{price:.2f}塊，漲幅為{change:.2f}塊，百分比{change_percent:.2f}%"
            text_to_speech(text)
        else:
            print(f"未能獲取到{name}的股票信息。")
    time.sleep(60)  # 每分鐘更新一次
