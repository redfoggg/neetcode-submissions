class Solution:

    __BUFFER = str(hash(100))

    def encode(self, strs: List[str]) -> str:
        return self.__BUFFER.join(strs)

    def decode(self, s: str) -> List[str]:
        decoded_str = s.split(self.__BUFFER)
        if not decoded_str:
            return []
        return decoded_str
