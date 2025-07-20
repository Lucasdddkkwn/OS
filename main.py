import os

target_ip = "192.168.2.1"

os.system(f"shutdown /s /m \\\\{target_ip} /t 0")
