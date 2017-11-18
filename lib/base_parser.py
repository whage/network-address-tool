import subprocess

class BaseParser:
    def init_raw_data(self, command_output = None):
        self.raw_data = command_output

        if not command_output:
            self.raw_data = subprocess.getoutput([self.command])