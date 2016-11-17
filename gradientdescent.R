# Data for Analysis
# Credit : some parts of this code are directly borrowed from R-blogger (am too lazy :-))
set.seed(100)
x <- rnorm(1000, 0, 1)
y <- x + rnorm(1000)+1


# Loss Function 
LF <- function(X, y, theta) {
  sum( (X %*% theta - y)^2 ) / (2*length(y))
}


# Define learning rate and iteration limit
alpha <- 0.01
num_iters <- 1000

# Save history
LF_history <- double(num_iters)
theta_history <- list(num_iters)

# initialize coefficients
theta <- matrix(c(0,0), nrow=2)

# add a column of 1's for the intercept coefficient
X <- cbind(1, matrix(x))

# gradient descent
for (i in 1:num_iters) {
  error <- (X %*% theta - y)
  delta <- t(X) %*% error / length(y)
  theta <- theta - alpha * delta
  LF_history[i] <- LF(X, y, theta)
  theta_history[[i]] <- theta
}

# Print the final value of m & c
print(theta)


# 3D Plot (Loss Function, m, c) 
m<-seq(-100, 100, 5)
c<-seq(-100, 100, 5)
Y2<-sum(y^2)
X2<-sum(x^2)
XY<-sum(x*y)
X<-sum(x)
Y<-sum(y)
loss<-Y2+X2*m^2+c^2*length(y)+2*XY*m+2*Y*c-2*X*m*c
f <- function(m, c) {Y2+X2*m^2+c^2*length(y)+2*XY*m+2*Y*c-2*X*m*c}
z <- outer(m, c, f)
persp(m, c, z, phi = 30, theta = 30,col = "orange",xlab = "m (Slope of the Line)",ylab = "c (Intercept on the Y-axis)",zlab = "Loss Function")


# 2D Heat map (Loss Function, m, c) 
m<-seq(-100, 100, .5)
c<-seq(-100, 100, .5)
Y2<-sum(y^2)
X2<-sum(x^2)
XY<-sum(x*y)
X<-sum(x)
Y<-sum(y)
loss<-Y2+X2*m^2+c^2*length(y)+2*XY*m+2*Y*c-2*X*m*c
f <- function(m, c) {Y2+X2*m^2+c^2*length(y)+2*XY*m+2*Y*c-2*X*m*c}
z <- outer(m, c, f)
image(m,c,z,xlab = "m (Slope of the Line)",ylab = "c (Intercept on the Y-axis)",main="Loss Function Vs (m & c)")
par(new=TRUE)
contour(m,c,z, xaxt='n', yaxt='n',lwd = 2)
abline(h=1,col="blue")
abline(v=1,col="blue")