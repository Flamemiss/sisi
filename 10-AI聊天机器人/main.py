"""
AI聊天机器人 - 命令行版
"""
from chatbot import ChatBot, ROLES

def print_help():
    """打印帮助信息"""
    print("""
命令说明：
  /help     - 显示帮助
  /clear    - 清空对话历史
  /role     - 切换角色
  /history  - 查看对话历史
  /quit     - 退出程序
""")

def print_roles():
    """打印可用角色"""
    print("\n可用角色：")
    for name, desc in ROLES.items():
        print(f"  {name}: {desc[:30]}...")
    print()

def main():
    print("="*50)
    print("      🤖 AI聊天机器人")
    print("="*50)
    print("输入 /help 查看命令，/quit 退出\n")
    
    # 创建机器人
    bot = ChatBot(ROLES["default"])
    current_role = "default"
    
    while True:
        try:
            user_input = input("你: ").strip()
        except KeyboardInterrupt:
            print("\n再见！")
            break
        
        if not user_input:
            continue
        
        # 处理命令
        if user_input.startswith('/'):
            cmd = user_input.lower()
            
            if cmd == '/quit' or cmd == '/exit':
                print("再见！")
                break
            
            elif cmd == '/help':
                print_help()
            
            elif cmd == '/clear':
                bot.clear_history()
                print("对话历史已清空\n")
            
            elif cmd == '/role':
                print_roles()
                role_name = input("选择角色: ").strip()
                if role_name in ROLES:
                    bot.set_system_prompt(ROLES[role_name])
                    bot.clear_history()
                    current_role = role_name
                    print(f"已切换到角色: {role_name}\n")
                else:
                    print("角色不存在\n")
            
            elif cmd == '/history':
                history = bot.get_history()
                print("\n对话历史：")
                for msg in history:
                    role = msg["role"]
                    content = msg["content"][:50] + "..." if len(msg["content"]) > 50 else msg["content"]
                    print(f"  [{role}]: {content}")
                print()
            
            else:
                print("未知命令，输入 /help 查看帮助\n")
            
            continue
        
        # 发送消息
        print("AI: ", end="", flush=True)
        response = bot.chat(user_input)
        print(response)
        print()

if __name__ == "__main__":
    main()
