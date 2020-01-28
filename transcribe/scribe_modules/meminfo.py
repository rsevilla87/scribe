import sys
from . import ScribeModuleBaseClass


class Meminfo(ScribeModuleBaseClass):

    def __init__(self, input_dict=None, module_name=None, host_name=None,
                 input_type=None, scribe_uuid=None):
        ScribeModuleBaseClass.__init__(self, module_name=module_name,
                                       input_dict=input_dict,
                                       host_name=host_name,
                                       input_type=input_type,
                                       scribe_uuid=scribe_uuid)
        if input_dict:
            self.value = self._parse(input_dict)

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def _parse(self, meminfo_data):
        output = {}
        meminfo_lines = meminfo_data.get("meminfo").strip().split('\n')
        if len(meminfo_lines) <= 1:
            print("Error occured in processing meminfo data")
            sys.exit(1)
        return {opt.split(":")[0].strip(): opt.split(":")[1].strip() for opt in meminfo_lines}
