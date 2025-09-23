# 導入時間模組，用於我們的番茄鐘
import time
import os

# --- 基礎建構模塊：定義所有事物的「藍圖」---

class Task:
    """代表一個最小的任務節點"""
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.is_completed = False

    def complete_task(self):
        """將任務標記為完成"""
        self.is_completed = True
        print(f"\n✨ 太棒了！你點亮了任務節點：【{self.name}】")

class Unit:
    """代表一個學習單元，由多個任務組成"""
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks

    def is_unit_complete(self):
        """檢查單元內是否所有任務都已完成"""
        return all(task.is_completed for task in self.tasks)

    def display_status(self):
        """顯示單元內所有任務的狀態"""
        print(f"\n--- 單元：{self.name} ---")
        for i, task in enumerate(self.tasks):
            status_icon = "✅" if task.is_completed else "🔲"
            print(f"  {i + 1}. {status_icon} {task.name}")
        if self.is_unit_complete():
            print("🌟 這個單元已經被你完全點亮了！")

class Subject:
    """代表一個學科，也就是一張知識探索地圖"""
    def __init__(self, name, theme_icon, units):
        self.name = name
        self.theme_icon = theme_icon
        self.units = units

    def display_map(self):
        """顯示這張地圖的通關進度"""
        print(f"\n{self.theme_icon} 歡迎來到【{self.name}】的知識探索地圖 {self.theme_icon}")
        for i, unit in enumerate(self.units):
            status_icon = "🌟" if unit.is_unit_complete() else "➡️"
            print(f"  {i + 1}. {status_icon} 單元：{unit.name}")

class GrowthTracker:
    """成就殿堂：追蹤孩子的成長與徽章"""
    def __init__(self):
        self.badges = {
            "專注之星": {"earned": False, "description": "連續使用番茄鐘完成一次學習"},
            "數學大師": {"earned": False, "description": "完成所有數學單元"},
            "閱讀小能手": {"earned": False, "description": "完成國文科的第一個閱讀任務"}
        }
        self.tree_level = 0
        self.completed_tasks_count = 0

    def award_badge(self, badge_name):
        """頒發徽章"""
        if not self.badges[badge_name]["earned"]:
            self.badges[badge_name]["earned"] = True
            self.tree_level += 5 # 獲得徽章能讓成長樹大幅成長
            print(f"\n🏆🎉 恭喜！你獲得了成就徽章：【{badge_name}】！🎉🏆")
            print(f"你的成長樹因此變得更加茁壯了！🌳")

    def add_progress(self):
        """每次完成任務，都會讓成長樹緩慢長大"""
        self.completed_tasks_count += 1
        self.tree_level += 1
        print("你的成長樹又長高了一點點！")

    def display_achievements(self):
        """顯示成就殿堂的狀態"""
        print("\n--- 🌳 成就殿堂 🌳 ---")
        print(f"你的成長樹等級：Lv.{self.tree_level}")
        print("你已獲得的徽章：")
        has_badge = False
        for name, data in self.badges.items():
            if data["earned"]:
                print(f"  🏅 {name} - {data['description']}")
                has_badge = True
        if not has_badge:
            print("  ( 아직 획득한 배지가 없습니다. 계속 모험해 보세요! )") # 韓文: (目前還沒有徽章，繼續冒險吧！) - 增加趣味性的小彩蛋
        print("--------------------")

class TimePlanner:
    """魔法時間羅盤：內建番茄鐘"""
    def start_pomodoro(self):
        """啟動一個25分鐘的專注時間和5分鐘的休息時間"""
        print("\n⏳ 魔法時間羅盤已啟動！")
        print("現在開始25分鐘的專注時間，加油！")
        # 為了方便測試，這裡我們用秒來代替分鐘
        # time.sleep(25 * 60)
        time.sleep(5) # 模擬5秒的專注時間
        print("\n🔔 時間到！專注時間結束，做得很好！")
        print("現在是5分鐘的休息時間，起來走動一下，看看遠方吧！")
        # time.sleep(5 * 60)
        time.sleep(2) # 模擬2秒的休息時間
        print("🔔 休息結束，準備好開始下一次的冒險了嗎？")
        return True # 返回True表示完成了一次番茄鐘

# --- 遊戲主體：將所有模塊組合起來 ---

class LearningAdventureApp:
    """學習冒險家養成計畫 主程式"""
    def __init__(self):
        # 初始化數據
        self.setup_subjects()
        self.tracker = GrowthTracker()
        self.planner = TimePlanner()

    def setup_subjects(self):
        """在這裡建立所有學科、單元和任務的內容"""
        # 國文
        literature_t1 = Task("閱讀〈背影〉", "細讀課文，感受父子之情")
        literature_t2 = Task("完成習作P.20-22", "練習修辭和文意理解")
        literature_u1 = Unit("第一單元：親情", [literature_t1, literature_t2])
        self.literature = Subject("國文", "📚", [literature_u1])

        # 數學
        math_t1 = Task("理解畢氏定理", "觀看教學影片")
        math_t2 = Task("完成習題5-1", "練習勾股定理的計算")
        math_u1 = Unit("第五單元：畢氏定理", [math_t1, math_t2])
        self.math = Subject("數學", "📐", [math_u1])

        self.subjects = {"1": self.literature, "2": self.math}

    def display_dashboard(self):
        """顯示冒險家總部的主頁面"""
        print("\n--- 🚀 冒險家總部 (Dashboard) 🚀 ---")
        total_tasks = 0
        completed_tasks = 0
        for subject in self.subjects.values():
            for unit in subject.units:
                total_tasks += len(unit.tasks)
                completed_tasks += sum(1 for task in unit.tasks if task.is_completed)
        
        progress = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        print(f"本週任務總進度：[{'#' * int(progress / 10)}{' ' * (10 - int(progress / 10))}] {progress:.1f}%")

        print("\n--- 各學科探索進度 ---")
        for key, subject in self.subjects.items():
            print(f"  {key}. {subject.theme_icon} {subject.name}")
        print("---------------------------------")

    def interact_with_map(self):
        """與知識探索地圖互動的流程"""
        # 1. 選擇學科
        self.display_dashboard()
        choice = input("請輸入想探索的學科編號：")
        if choice not in self.subjects:
            print("無效的選擇！")
            return

        subject = self.subjects[choice]
        
        while True:
            # 2. 顯示地圖並選擇單元
            subject.display_map()
            unit_choice = input("\n請輸入想進入的單元編號 (輸入 'b' 返回總部): ")
            if unit_choice.lower() == 'b':
                break
            
            try:
                unit = subject.units[int(unit_choice) - 1]
            except (ValueError, IndexError):
                print("無效的單元選擇！")
                continue

            # 3. 顯示單元任務並選擇完成
            unit.display_status()
            task_choice = input("請選擇已完成的任務編號 (輸入 'b' 返回地圖): ")
            if task_choice.lower() == 'b':
                continue

            try:
                task = unit.tasks[int(task_choice) - 1]
                if not task.is_completed:
                    task.complete_task()
                    self.tracker.add_progress() # 成長樹成長
                    # 檢查是否能觸發徽章
                    if subject.name == "國文" and task.name.startswith("閱讀"):
                         self.tracker.award_badge("閱讀小能手")
                else:
                    print("這個任務你已經完成了喔！")
                
                # 檢查數學單元是否全部完成
                if subject.name == "數學" and all(u.is_unit_complete() for u in subject.units):
                    self.tracker.award_badge("數學大師")

            except (ValueError, IndexError):
                print("無效的任務選擇！")

    def run(self):
        """主程式迴圈"""
        print("="*40)
        print("      歡迎來到【學習冒險家養成計畫】！")
        print("="*40)
        while True:
            print("\n--- 你現在在「冒險家總部」---")
            print("1. 查看儀表板 (Dashboard)")
            print("2. 進入知識探索地圖 (Learning Map)")
            print("3. 使用魔法時間羅盤 (Time Planner)")
            print("4. 查看成就殿堂 (Growth Tracker)")
            print("5. 結束今天的冒險 (Exit)")
            choice = input("請選擇你的下一步行動：")

            if choice == "1":
                self.display_dashboard()
            elif choice == "2":
                self.interact_with_map()
            elif choice == "3":
                if self.planner.start_pomodoro():
                    self.tracker.award_badge("專注之星")
            elif choice == "4":
                self.tracker.display_achievements()
            elif choice == "5":
                print("\n今天的冒M冒險辛苦了，好好休息，期待你明天的表現！")
                break
            else:
                print("\n無效的指令，請重新選擇。")
            
            input("\n(請按 Enter 鍵繼續...)")
            # 清除螢幕，讓介面更乾淨
            os.system('cls' if os.name == 'nt' else 'clear')


# --- 啟動遊戲 ---
if __name__ == "__main__":
    app = LearningAdventureApp()
    app.run()
