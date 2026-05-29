class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniorCitizens = 0
        
        for d in details:
            if int(d[11:13]) > 60:
                seniorCitizens += 1
        
        return seniorCitizens

        