# Summary
I would like to write paper about the heat equation

## 1-D heat Equation
$$
\frac{\partial u}{\partial t} = k \frac{\partial^2 u}{\partial x^2}
$$

Can be solved numerically by substituting derivative with delta where
$$
\frac{\partial u}{\partial t} 
\approx
\frac{u^{n + 1}_{i} - u^{n}_{i}}{\Delta t} 
$$


### Explicit Method
In explicit method we have
$$
k \frac{\partial^2 u}{\partial x^2}
\approx
k \frac{u^{n}_{i + 1} - 2u^{n}_{i} + u ^{n}_{i - 1}}{(\Delta x)^2}
$$
So the original function becomes
$$
\frac{u^{n + 1}_{i} - u^{n}_{i}}{\Delta t} 
\approx 
k \frac{u^{n}_{i + 1} - 2u^{n}_{i} + u ^{n}_{i - 1}}{(\Delta x)^2}
$$


Assume 
$$
r = \frac{k \Delta t}{(\Delta x)^2}
$$
then we have
$$
u^{n + 1}_{i} = u^{n}_{i} + r (u^{n}_{i + 1} - 2 u^{n}_{i} + u^{n}_{i - 1})
$$



This is equivalent to 
$$
u^{n + 1} = A u^{n}
$$
where 
$$
  A =
  \left[ {\begin{array}{ccccc}
    1-2r & r & 0 & \cdots & 0 \\
    r & 1-2r & r & \cdots & 0 \\
    0 & r & 1-2r & \cdots & 0 \\
    \vdots & \vdots & \vdots & \ddots & 0 \\
    0 & 0 & 0 & r & 1-2r \\
  \end{array} } \right]
$$
and can be solved by substitution

This methods is not guaranteed to be stable, it has to follow CFL condition

### Implicit Method
In implicit method we have
$$
k \frac{\partial^2 u}{\partial x^2}
\approx
k \frac{u^{n + 1}_{i + 1} - 2u^{n + 1}_{i} + u ^{n + 1}_{i - 1}}{(\Delta x)^2}
$$
So the original function becomes
$$
\frac{u^{n + 1}_{i} - u^{n}_{i}}{\Delta t} 
\approx 
k \frac{u^{n + 1}_{i + 1} - 2u^{n + 1}_{i} + u ^{n + 1}_{i - 1}}{(\Delta x)^2}
$$

Assume 
$$
r = \frac{k \Delta t}{(\Delta x)^2}
$$
then we have
$$
-ku^{n + 1}_{i - 1} + (1 + 2k)u^{n + 1}_{i} - ku^{n + 1}_{i + 1} = u^{n}_{i}
$$


It is equivalent to
$$
Au^{n + 1} = u^{n}
$$
where 
$$
  A =
  \left[ {\begin{array}{ccccc}
    1+2r & -r & 0 & \cdots & 0 \\
    -r & 1+2r & -r & \cdots & 0 \\
    0 & -r & 1+2r & \cdots & 0 \\
    \vdots & \vdots & \vdots & \ddots & 0 \\
    0 & 0 & 0 & -r & 1+2r \\
  \end{array} } \right]
$$

This is unconditionally stable, and more computational expensive, but this specific 1-D senario can be solved with Thomas Algorithm, having the same complexity of Explicit Method


### Crank Nicolson Method

In Crank-Nicolson Method we have
$$
k \frac{\partial^2 u}{\partial x^2}
\approx
\frac{1}{2}k 
\frac{(u^{n + 1}_{i + 1} - 2u^{n + 1}_{i} + u ^{n + 1}_{i - 1}) + (u^{n}_{i + 1} - 2u^{n}_{i} + u ^{n}_{i - 1})}{(\Delta x)^2}
$$

The original function becomes
$$
\frac{u^{n + 1}_{i} - u^{n}_{i}}{\Delta t} 
\approx 
\frac{1}{2}k 
\frac{(u^{n + 1}_{i + 1} - 2u^{n + 1}_{i} + u ^{n + 1}_{i - 1}) + (u^{n}_{i + 1} - 2u^{n}_{i} + u ^{n}_{i - 1})}{(\Delta x)^2}
$$

This is equivalent to 
$$
A_1 u ^{n + 1} = A_2 u ^{n}
$$
where 
$$
  A_1 =
  \left[ {\begin{array}{ccccc}
    1+2r & -r & 0 & \cdots & 0 \\
    -r & 1+2r & -r & \cdots & 0 \\
    0 & -r & 1+2r & \cdots & 0 \\
    \vdots & \vdots & \vdots & \ddots & 0 \\
    0 & 0 & 0 & -r & 1+2r \\
  \end{array} } \right]
$$

and 
$$
  A_2 =
  \left[ {\begin{array}{ccccc}
    1-2r & r & 0 & \cdots & 0 \\
    r & 1-2r & r & \cdots & 0 \\
    0 & r & 1-2r & \cdots & 0 \\
    \vdots & \vdots & \vdots & \ddots & 0 \\
    0 & 0 & 0 & r & 1-2r \\
  \end{array} } \right]
$$

So 
$$
u ^ {n + 1} = A_2 ^ {-1} A_1 u ^{n}
$$
This is also unconditionally stable and more precise, but the time complexity is higher.

## 2-D Heat Equation
$$
\frac{\partial u}{\partial t} = k (\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2})
$$

Similarly, we can solve with similar problems

$$

$$