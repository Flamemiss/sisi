# reminder.py
"""
简单的定时提醒工具
"""
import time
from datetime import datetime, timedelta

def countdown_timer(seconds, message="时间到！"):
    """倒计时提醒"""
    print(f"倒计时开始: {seconds} 秒")
    print(f"提醒内容: {message}\n")
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\r剩余时间: {timer}", end="", flush=True)
        time.sleep(1)
        seconds -= 1
    
    print(f"\n\n{'='*30}")
    print(f"⏰ {message}")
    print(f"{'='*30}")
    
    # Windows系统蜂鸣声
    try:
        import winsound
        winsound.Beep(1000, 500)  # 频率1000Hz，持续500ms
    except:
        print('\a')  # 通用蜂鸣

def time_reminder(target_time, message="时间到！"):
    """定时提醒（指定时间）"""
    # 解析目标时间
    if isinstance(target_time, str):
        target = datetime.strptime(target_time, "%H:%M")
        target = target.replace(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day
        )
    else:
        target = target_time
    
    now = datetime.now()
    
    if target < now:
        print("目标时间已过！")
        return
    
    wait_seconds = (target - now).total_seconds()
    print(f"将在 {target.strftime('%H:%M:%S')} 提醒你")
    print(f"还需等待 {int(wait_seconds)} 秒")
    
    countdown_timer(int(wait_seconds), message)

# 使用示例
if __name__ == "__main__":
    print("=== 定时提醒工具 ===")
    print("1. 倒计时（分钟）")
    print("2. 指定时间")
    
    choice = input("\n选择模式 (1/2): ")
    
    if choice == "1":
        minutes = int(input("倒计时分钟数: "))
        message = input("提醒内容: ") or "时间到！"
        countdown_timer(minutes * 60, message)
    
    elif choice == "2":
        time_str = input("目标时间 (格式 HH:MM): ")
        message = input("提醒内容: ") or "时间到！"
        time_reminder(time_str, message)
