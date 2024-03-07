import time
import subprocess
import paramiko
from src.utils.validation import is_valid_ip


class gpudata:
    def __init__(self):
        self.gpu_list = {}
        self.ssh_connector_pool = {}

    def list_gpus(self):
        pass

    def update(self, data: dict):
        """
        server_ip: str
        memory_in_use: int
        memory_in_all: int
        gpu_usage: int
        gpu_id: int
        gpu_temp: int
        """
        data['gpu_id'] = data['server_ip'] + '_' + str(data['gpu_id'])
        data['memory_left'] = data['memory_in_all'] - data['memory_in_use']
        self.gpu_list[data['gpu_id']] = data

    def sort(self):
        self.gpu_list = {k: v for k, v in sorted(self.gpu_list.items(), key=lambda item: item[1]['memory_left'])}

    def mask(self, memory: int):
        self.gpu_list = {k: v for k, v in self.gpu_list.items() if v['memory_left'] >= memory}

    def run(self, memory: int, script: str, need_new_ssh_connection=False):
        self.mask(memory)
        self.sort()
        if self.gpu_list:
            server_ip, gpu_id = self.gpu_list[next(iter(self.gpu_list))]['gpu_id'].split('_')
            if is_valid_ip(server_ip) and need_new_ssh_connection:
                if server_ip not in self.ssh_connector_pool:
                    self.ssh_connector_pool[server_ip] = paramiko.SSHClient()
                    self.ssh_connector_pool[server_ip].set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    self.ssh_connector_pool[server_ip].connect(server_ip, username='114514', password='password')
                stdin, stdout, stderr = self.ssh_connector_pool[server_ip].exec_command(script)
            elif server_ip == 'local':
                result = subprocess.run(script.split(' '), capture_output=True, text=True)
            else:
                assert "Error server ip!"

    def scan(self):
        self.list_gpus()
        while True:
            self.run(10, "123")
