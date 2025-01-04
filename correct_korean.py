import time
import keyboard 
import pyperclip
from hanspell import spell_checker

def correct_korean_text():
    # 드래그된 텍스트 복사 (macOS: command + c)
    keyboard.send('command+c')
    time.sleep(0.1)  # 복사 완료 대기
    original_text = pyperclip.paste()
    print(original_text)

    # 한글 맞춤법 교정
    result = spell_checker.check(original_text)
    corrected_text = result.checked
    print(corrected_text)

    # 교정된 텍스트 붙여넣기 (macOS: command + v)
    pyperclip.copy(corrected_text)
    keyboard.send('command+v')
    
    
    
    
def test(): 
    print("test")
    
# Command + `를 누르면 교정 함수 실행``
keyboard.add_hotkey('command+`', correct_korean_text)
print('Hello World')
# 단축키 입력을 계속해서 대기
keyboard.wait()