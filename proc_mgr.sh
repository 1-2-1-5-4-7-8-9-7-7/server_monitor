#!/bin/bash
#功能：杀掉指定用户的所有进程（需确认）


if [ -z "$1" ]; then
	echo "用法：$0 <用户名>"
	echo "示例：$0 lxt"
	exit 1
fi

USERNAME=$1
echo "正在查找用户 $USERNAME 的进程..."
PIDS=$(pgrep -U "$USERNAME")

if [ -z "$PIDS" ]; then
	echo "未找到该用户的任何进程"
	exit 0
fi


echo "找到以下进程："
pgrep -l -U "$USERNAME"
echo "---------------------------"
read -p "确认要终止以上所有进程吗？(y/N)" CONFIRM


if [ "$CONFIRM" = "y" ] || [ "$CONFIRM" = "Y" ]; then
	kill $PIDS
	echo "已发送终止信号。"
	#检查是否成功
	sleep 1
	if pgrep -U "$USERNAME" > /dev/null; then
		echo "部分进程仍在运行，尝试强制杀死..."
		kill -9 $PIDS
	fi
else
	echo "操作已取消。"
fi
