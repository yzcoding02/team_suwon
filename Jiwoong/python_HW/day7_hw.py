import matplotlib.pyplot as plt
subject = ["math", "science", "english", "society","korean"]
subject2 = ["P.E", "art", "moral", "history","music"]
barcolor=["darkred","red","yellow","greenyellow","green"]
counts = [87,80, 95,97,100]
counts2 = [97, 100, 93, 89,100]
창, 내용 = plt.subplots(1,3)
내용[0].bar(subject, counts,color=barcolor)
내용[1].barh(subject, counts,color=barcolor)
내용[2].bar(subject2, counts2,color=barcolor)
plt.show()