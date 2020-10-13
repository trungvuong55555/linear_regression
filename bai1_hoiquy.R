library(tidyverse)
library(ggplot2)
library(caret)

#tao du lieu
x<- c(4.862,5.244,5.128,5.052,5.298,5.410,5.234,5.608)
y <-c(160,175,192,195,238,240,252,282)
data <- data.frame(x,y)

#mot so thong so ve du lieu
summary(data)

#dung ham lm() cho hoi quy tuyen tinh

linear <- lm(y~x,data=data)
linear$coefficients

#visualization

data %>% ggplot(aes(x=x,y=y))+
  geom_point(aes(color= 'red'))+
  labs(title = 'su lien quan giua nang xuat lua mi va mat do gieo trong',x = 'Nang suatlua mi(kg/ha)',y='Matdotrong(no./m2)')+
  geom_smooth(method = "lm")
  
  
  
