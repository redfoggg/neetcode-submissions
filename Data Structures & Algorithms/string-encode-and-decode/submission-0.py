class Solution:

    __buffer_const = str(hash(100))

    def encode(self, strs: List[str]) -> str:
        return self.__buffer_const.join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split(self.__buffer_const)
