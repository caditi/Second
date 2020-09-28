import pyautogui
pyautogui.click()
distance = 200
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration = 0.5)
    distance = distance - 25
    pyautogui.dragRel(0, distance, duration = 0.5)
    pyautogui.dragRel(-distance, 0, duration = 0.5)
    distance = distance - 25
    pyautogui.dragRel(0 ,-distance, duration = 0.5)
