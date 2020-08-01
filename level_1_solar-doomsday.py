def get(num):
  n=1
  while(n*n<num+1):
    n=n+1
  return n-1
def solution(area):
  ans=[]
  while(area!=0):
    sq=get(area)
    ans.append(sq*sq)
    area-=sq*sq
  return ans
