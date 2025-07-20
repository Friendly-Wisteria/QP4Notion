from pyperclip import copy,paste
from pyautogui import press,keyDown,keyUp,hotkey
import platform

def paste_as_quote():
    """
    Notion上の引用マークをつけた形でペーストする
    想定環境
    * macOS or Windows
    * 日本語キーボード
    動作時は英数入力モードにすること
    """
    pf = platform.platform() # 動作中のOSの取得
    quote_text = paste() # クリップボードの内容を取得

    # Shift + 2を再現
    keyDown('shift')
    press('2')
    keyUp('shift')
    press('space') # スペースキーの入力を再現
    # 引用内容をペースト
    copy(quote_text)
    if 'macOS' in pf:
        hotkey('command', 'v') # command + Vを再現
    elif 'Windows' in pf:
        hotkey('ctrl', 'v') # ctrl + Vを再現
    else:
        raise Exception('この環境ではサポートしていません')
if __name__ == '__main__':
    paste_as_quote()
