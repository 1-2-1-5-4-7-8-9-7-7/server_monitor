# Server Monitor / 进程管理脚本

这是一个用于 Linux 进程管理的 Shell 脚本集合，适合学习和日常服务器维护使用。

## 📁 文件说明

- `proc_mgr.sh`：按用户名查找进程，并支持交互式优雅终止（先 SIGTERM，后 SIGKILL）。
- `.gitignore`：忽略日志文件、系统缓存等不需要追踪的文件。

## 🚀 使用方法
	./proc_mgr.sh <用户名>
	
### 进程管理脚本


## 🛠️ 功能特性

- ✅ 按用户精确查找进程（pgrep -U）
- ✅ 交互式确认，防止误杀
- ✅ 先发送 SIGTERM 优雅终止，超时后再 SIGKILL 强制杀死
- ✅ 清晰的进程列表展示

## 📚 学习笔记

本仓库也记录了学习 Linux 命令行和 Shell 脚本的过程：
- 进程查看：ps, top, pgrep, pkill
- 信号管理：kill, kill -9, SIGTERM, SIGKILL
- 作业控制：bg, fg, jobs, Ctrl+Z
- 版本控制：Git 基础操作
- 代码编写过程的一些记录：（1）test语句[]内部指令应该与[]用空格隔开，老是忘记
			  （2）shell脚本的if判别逻辑，和python里的有点区别，不是纯布尔逻辑，就比如说“pgrep”的返回值，找到对象了返回“0”，视作成功。


## ⚠️ 注意事项

- 脚本需要 root 权限才能终止其他用户的进程。
- 强制杀死进程（SIGKILL）可能导致数据丢失，请谨慎使用。
