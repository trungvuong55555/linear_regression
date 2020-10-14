import matplotlib.pyplot as plt
import numpy as np

#kieu phuong trinh y=w0+w1*x (1)
#w =[w0 w1]
#yeu cau bai toan la tim w0 va w1

# nhap du lieu dau vao
x = np.array([4.862,5.244,5.128,5.052,5.298,5.410,5.234,5.608],dtype=float).T #'.T' la ma tran chuyen vi
y= np.array([160,175,192,195,238,240,252,282],dtype=float).T

#ve do thi voi du lieu ban dau

plt.plot(x,y)
plt.axis([min(x),max(x),min(y),max(y)])
plt.xlabel('Nangsuatluami(kg/ha)')
plt.ylabel('Matdotrong(no./m2)')
plt.show()

#tao mot kieu du lieu x moi goi la xbar, tuc la them mot vector hang [1] vao dau vector x
#xbar*w=y(2)

one = np.ones((x.shape[0], 1)) # tao mot vecto doc co gia tri bang 1
xbar= np.column_stack((one,x))

#de tim duoc w toi uu thi w la nghiem dao ham cua loss fuction ptr(2)

a = (xbar.T).dot(xbar)
b= (xbar.T).dot(y)

dinhthuc_a=np.linalg.det(a) # ham tinh dinh thuc cua ma tran

if dinhthuc_a.all()==0:
    w=(np.linalg.pinv(a)).dot(b) #ham nay la ma tran gia nghich dao
else:
    w = (np.linalg.inv(a)).dot(b) # ham nay la ma tran nghich dao

w0 = w[0]
w1 = w[1]

print('w0= ',w0)
print('w1= ',w1)

#ve lai do thi voi 2 gia tri tim duoc

x0= np.linspace(min(x),max(x),1000)
y0=w0+w1*x0

plt.plot(x,y)
plt.plot(x0,y0)
plt.axis([min(x),max(x),min(y),max(y)])
plt.xlabel('Nangsuatluami(kg/ha)')
plt.ylabel('Matdotrong(no./m2)')
plt.show()

#bay h check ket qua bang cach dung ham co san trong thu vien scikit-learn

from sklearn import datasets, linear_model

regr = linear_model.LinearRegression(fit_intercept=False) #chon False de tinh w0
regr.fit(xbar, y)

print('ket qua cua ham co san tinh duoc: ',regr.coef_)
print('ket qua code tay tinh duoc: ',w)









