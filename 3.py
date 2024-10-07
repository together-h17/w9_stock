import yfinance as yf
from gtts import gTTS
import pygame
import time
import os
import uuid

# 初始化 Pygame Mixer
pygame.mixer.init()

# 設置股票代碼和名稱
stocks = {
    '2330.TW': '台積電',
    '2317.TW': '鴻海',
    '2454.TW': '聯發科',
    # 可以在這裡添加更多股票代碼和名稱的映射
}

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    todays_data = stock.history(period='1d')
    if not todays_data.empty:
        current_price = todays_data['Close'][0]
        previous_close = todays_data['Open'][0]  # 使用開盤價作為前一天收盤價的近似值
        change = current_price - previous_close
        change_percent = (change / previous_close) * 100
        return current_price, change, change_percent
    else:
        return None, None, None  # 处理无数据的情况

def text_to_speech(text, lang='zh'):
    tts = gTTS(text=text, lang=lang)
    # 使用唯一的文件名
    filename = f"stock_{uuid.uuid4()}.mp3"
    tts.save(filename)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # 等待音樂播放結束
        time.sleep(0.1)
    # 删除文件以避免占用问题
    pygame.mixer.music.unload()
    os.remove(filename)

while True:
    for symbol, name in stocks.items():
        price, change, change_percent = get_stock_data(symbol)
        if price is not None:
            text = f"目前{name}的價格是{price:.2f}新台幣，漲幅為{change:.2f}新台幣，百分比為{change_percent:.2f}%"
            text_to_speech(text)
        else:
            print(f"未能获取到{symbol}的股票信息。")
    time.sleep(60)  # 每分鐘更新一次