from monitor.collector import SystemCollector

def main():
    collector = SystemCollector()
    print("开始采集系统信息...")
    data = collector.get_system_snapshot()
    for key, value in data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()