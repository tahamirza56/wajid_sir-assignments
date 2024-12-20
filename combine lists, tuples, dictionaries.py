my_dict={"taha" : (90,100,95,),
         "arsalan": (95,100,98),
         "jibran" : (90,95,99)}
result=my_dict
print(result["taha"])
avg_score=sum(result["taha"]) / 3, sum(result["arsalan"])/3 ,sum(result["jibran"])/3
print(avg_score)
print(max(avg_score))
