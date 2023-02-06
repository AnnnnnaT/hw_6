# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.

data =[1.1, 1.2, 3.1, 5, 10.01]
res = []
a = [res.append(i%1) for i in data if i%1!=0 and isinstance(i,float)]
res1 = round(max(res)-min(res),2)
print(res1)
