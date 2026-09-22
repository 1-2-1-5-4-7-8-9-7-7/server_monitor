import psutil
import time

class SystemCollector:
    def __init__(self):
        pass

    def get_system_snapshot(self):
        """采集系统当前快照，返回字典"""
        snapshot = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "cpu":{
            "percent": psutil.cpu_percent(interval=1),
            "cores": psutil.cpu_count(),
            "load_avg": psutil.getloadavg() if hasattr(psutil, 'getloadavg') else None,
        },
            "memory":{
            "total_gb": round(psutil.virtual_memory().total / 1024**3, 1),
            "used_gb": round(psutil.virtual_memory().used / 1024**3, 1),
            "percent": psutil.virtual_memory().percent,
        },
            "disk":{
            "total_gb": round(psutil.disk_usage('/').total / 1024**3, 1),
            "used_gb": round(psutil.disk_usage('/').used / 1024**3, 1),
            "percent": psutil.disk_usage('/').percent,
        },
            "network":{
            "bytes_sent_mb": round(psutil.net_io_counters().bytes_sent / 1024**2, 1),
            "bytes_recv_mb": round(psutil.net_io_counters().bytes_recv / 1024**2, 1),
        }
    }
        return snapshot