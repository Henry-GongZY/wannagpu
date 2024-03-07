import regex
import subprocess
from src.gpu.gpudata import gpudata


class gpustat2(gpudata):
    def __init__(self):
        super(gpudata, self).__init__()
        self.time_span = 120

    def list_gpus(self):
        result = subprocess.run(['cat', '/home/root/gpustat2.txt'], capture_output=True, text=True)
        output, error = result.stdout, result.stderr
        if error is None:
            # 去除最开始的标题
            output = output.replace('host          gpu temp memory_rate use_memory total_memory cur_proc\n', '')
            # 匹配并去除所有命令行颜色内容
            pattern = r"\x1b\[\d+(;\d+)?m"
            output = regex.sub(pattern, '', output)
            # 切分字符串内容
            output = output.replace('\n\n', '\n')
            pattern = r"(\n Num of Available Cards:((?:\s*\d+: \d+;)+)(\s*\[cached\] \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\n))"
            output = regex.sub(pattern, '', output)
            output = output.split('\n')
            data = {}
            for i in output:
                i = i.split()
                data['server_ip'] = i[0]
                data['gpu_id'] = i[1]
                data['gpu_temp'] = i[2]
                data['memory_in_use'] = i[4]
                data['memory_in_all'] = i[5]
                self.update(data)