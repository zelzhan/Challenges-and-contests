class Solution:
    def defangIPaddr(self, address: str) -> str:
        addresses = address.split(".")
        
        res = addresses.pop(0)
        for i, address in enumerate(addresses):
            if i == len(addresses):
                break
            res += "[.]" + address

        return res
