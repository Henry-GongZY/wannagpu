import pynvml
from src.gpu.gpudata import gpudata


class smidata(gpudata):
    def __init__(self):
        super(gpudata, self).__init__()
        pynvml.nvmlInit()

    def list_gpus(self):
        data = {}
        gpu_device_count = pynvml.nvmlDeviceGetCount()
        for i in range(gpu_device_count):
            data['server_ip'] = 'local'
            data['gpu_id'] = i
            device_handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            data['gpu_name'] = pynvml.nvmlDeviceGetName(device_handle)
            data['gpu_temp'] = pynvml.nvmlDeviceGetTemperature(device_handle, pynvml.NVML_TEMPERATURE_GPU)
            memory = pynvml.nvmlDeviceGetMemoryInfo(device_handle)
            data['memory_in_all'] = memory.total // (1024 * 1024)
            data['memory_in_use'] = memory.used // (1024 * 1024)
            data['gpu_usage'] = pynvml.nvmlDeviceGetUtilizationRates(device_handle).gpu
            self.update(data)
