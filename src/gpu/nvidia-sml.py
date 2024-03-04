import regex
from src.gpu.gpudata import gpudata


class smidata(gpudata):
    def __init__(self):
        super(gpudata, self).__init__()

    def add_smi(self, server: str, memory_in_use: int,
                memory_in_all: int, gpu_usage: int, gpu_id: int, gpu_temp: int,
                gpu_name: str):
        self.add(server, memory_in_use, memory_in_all, gpu_usage, gpu_id, gpu_temp)
        self.gpu_list[server + '_' + str(gpu_id)]['gpu_name'] = gpu_name
