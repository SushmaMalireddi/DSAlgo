class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        for row in range(2,numRows+1):
            ans=1
            temp=[ans]
            for col in range(1,row):
                ans=ans*(row-col)
                ans=ans//col
                temp.append(ans)
            res.append(temp)
        return res
