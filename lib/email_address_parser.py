import re
import ipdb
class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses
    # def parse(self):
    #     list_addresses = []
    #     if "," in self.addresses:
    #         list_addresses = self.addresses.split(",")
    #     else: 
    #         list_addresses= self.addresses.split()
    #         for address in list_addresses:
    #             if "," in address:
    #                 address.replace(",", "")
    #     return sorted(list_addresses)
    def parse(self):
        pattern = r"[ ,]"
        # regex = re.compile(pattern)
        split = re.split(pattern, self.addresses)
        list_addresses =[]
        for address in split:
            pattern2 = r"^[^0-9][A-z0-9.]+@{1}[A-z.]+"
            # ipdb.set_trace()
            if address in re.findall(pattern2, address):
                # split.remove(address)
                list_addresses.append(address)
                
        return sorted(list_addresses)