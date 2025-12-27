score = int(input("请输入成绩(0-100): "))

if score >= 90:
    print("等级: A (优秀)")
elif score >= 80:
    print("等级: B (良好)")
elif score >= 60:
    print("等级: C (及格)")
else:
    print("等级: D (不及格)")
