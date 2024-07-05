from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import keyboard
import threading
from playsound import playsound, PlaysoundException
import os



# Biến cờ để kiểm tra trạng thái dừng và tạm dừng của script
stop_script = False
pause_script = False
play_sound = True  # Biến cờ để kiểm soát việc phát âm thanh

# Hàm để kiểm tra phím nhấn trong một luồng riêng
def check_for_input():
    global stop_script, pause_script, play_sound
    while True:
        if keyboard.is_pressed('q'):
            stop_script = True
            print("Script đã được dừng bởi người dùng.")
            break
        elif keyboard.is_pressed('p'):
            pause_script = True
            print("Script đã được tạm dừng.")
        elif keyboard.is_pressed('r'):
            pause_script = False
            print("Script tiếp tục chạy.")
        elif keyboard.is_pressed('s'):
            play_sound = not play_sound
            status = "bật" if play_sound else "tắt"
            print(f"Phát âm thanh đã được {status}.")
        time.sleep(0.1)

# Hàm chính để thực hiện các thao tác click
def auto_click(driver, button1_selector, button2_selector, button3_selector):
    global stop_script, pause_script
    wait = WebDriverWait(driver, 10)
    button1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button1_selector)))

    print("Nhấn 'q' để dừng script, 'p' để tạm dừng, 'r' để tiếp tục, 's' để bật/tắt âm thanh.")

    while not stop_script:
        # Nếu script đang tạm dừng, đợi cho đến khi người dùng nhấn 'r' để tiếp tục
        while pause_script and not stop_script:
            time.sleep(0.1)
        
        # Click vào nút button đầu tiên
        button1.click()

        # Thời gian chờ cho dialog xuất hiện
        time.sleep(1)  # Điều chỉnh thời gian chờ nếu cần thiết

        try:
            # Đợi cho đến khi dialog xuất hiện và nút bên trong dialog có thể click được (với thời gian chờ tối đa 3 giây)
            button2 = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, button2_selector))
            )
            # Click vào nút bên trong dialog
            button2.click()
            if play_sound:
                try:
                    # Sử dụng đường dẫn tương đối cho tệp âm thanh
                    current_dir = os.path.dirname(__file__)
                    sound_path = os.path.join(current_dir, 'ting.mp3')
                    playsound(sound_path)
                except PlaysoundException as e:
                    print(f"Lỗi phát âm thanh: {e}")

        except:
            # Nếu button2 không tồn tại trong vòng 3 giây, tìm và click button3
            button3 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, button3_selector))
            )
            button3.click()

        # Đợi cho dialog biến mất (có thể đợi bằng cách tìm một element không tồn tại)
        #wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, dialog_selector)))

        # Nghỉ một khoảng thời gian
        time.sleep(5)  # Thay đổi thời gian nghỉ nếu cần

# Bắt đầu luồng kiểm tra phím nhấn
input_thread = threading.Thread(target=check_for_input)
input_thread.start()


try:
    # Yêu cầu người dùng nhập các CSS selector
    url = input("Nhập URL của trang web: ")
    button1_selector = input("Nhập CSS selector của button đầu tiên: ")
    button2_selector = input("Nhập CSS selector của button ok : ")
    button3_selector = input("Nhập CSS selector của button cancel: ")
    #dialog_selector = input("Nhập CSS selector của dialog nếu có: ")

    # Khởi tạo trình duyệt (ở đây dùng Chrome)
    #os.path.join(os.path.dirname + "chromedriver-win64\\chromedriver.exe")
    current_dir = os.path.dirname(__file__)
    chromedriver_path = os.path.join(current_dir, "chromedriver-win64", "chromedriver.exe")
    driver = webdriver.Chrome(executable_path=chromedriver_path)

    # Mở trang web của bạn
    driver.get(url)

    # Gọi hàm auto_click với các selector động
    auto_click(
        driver,
        button1_selector,
        button2_selector,
        button3_selector,
        
    )

finally:
    # Đóng trình duyệt khi hoàn thành (hoặc nếu có lỗi)
    driver.quit()


# # Bắt đầu luồng kiểm tra phím nhấn
# stop_thread = threading.Thread(target=check_for_input)
# stop_thread.start()

# # Khởi tạo trình duyệt (ở đây dùng Chrome)
# driver = webdriver.Chrome(executable_path="E:\\Practice\\ui\\CRM\\chromedriver-win64\\chromedriver.exe")

# try:
#     # Mở trang web của bạn
#     driver.get('http://127.0.0.1:5500/index.html')

#     # Đợi cho đến khi nút button đầu tiên có thể click được
#     wait = WebDriverWait(driver, 10)

#     # tiến hành login accout ở đây

#     button1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div:nth-child(2) > div > div > button.btn-main')))
#     print("Nhấn 'q' để dừng script.")

#     while not stop_script:

#         if keyboard.is_pressed('q'):
#             print("Script đã được dừng bởi người dùng.")
#             break
#         # Click vào nút button đầu tiên
#         button1.click()

#         # Thời gian chờ cho dialog xuất hiện
#         time.sleep(1)  # Điều chỉnh thời gian chờ nếu cần thiết

#         try:
#             # Đợi cho đến khi dialog xuất hiện và nút bên trong dialog có thể click được (với thời gian chờ tối đa 3 giây)
#             button2 = WebDriverWait(driver, 3).until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.dialog.open > div > div.dialog-btn > button.btn.btn-ok'))
#             )
#             # Click vào nút bên trong dialog
#             button2.click()
#         except:
#             # Nếu button2 không tồn tại trong vòng 3 giây, tìm và click button3
#             button3 = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.dialog.open > div > div.dialog-btn > button.btn.btn-cancel'))
#             )
#             button3.click()

        

#         # Nghỉ một khoảng thời gian
#         time.sleep(5)  # Thay đổi thời gian nghỉ nếu cần

# finally:
#     # Đóng trình duyệt khi hoàn thành (hoặc nếu có lỗi)
#     driver.quit()
