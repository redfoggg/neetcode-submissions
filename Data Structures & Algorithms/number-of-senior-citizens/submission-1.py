class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniorCitizens = 0
        
        for d in details:
            age = f"{d[11]}{d[12]}"
            if int(age) > 60:
                seniorCitizens += 1
        
        return seniorCitizens

        