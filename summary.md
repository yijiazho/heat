# Project Title
The numerical solution of 1-D and 2-D heat equation

# Statement
This project aim to compare some common numerical solutions to solve 1-D and 2-D heat equation with proper boundary conditions, covering Explicit method, implicit method and Crank-Nicolson method.

# Solution

## 1-D heat Equation
$$
\frac{\partial u}{\partial t} = k \frac{\partial^2 u}{\partial x^2}
$$

Can be solved numerically by substituting derivative with delta where
$$
\frac{\partial u}{\partial t} 
=
\frac{u^{n + 1}_{i} - u^{n}_{i}}{\Delta t} 
$$


### Explicit Method
In the explicit method, we approximate the time derivative as
$$
k \frac{\partial^2 u}{\partial x^2}
=
k \frac{u^{n}_{i + 1} - 2u^{n}_{i} + u ^{n}_{i - 1}}{(\Delta x)^2}
$$
So the original function becomes
$$
\frac{u^{n + 1}_{i} - u^{n}_{i}}{\Delta t} 
=
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

This methods is not guaranteed to be stable, it has to follow **CFL condition** 
$$r 
\leq \frac{1}{2}
$$ 
This limits the time step $ \Delta t $ based on $ \Delta x $

### Implicit Method
In implicit method we have
$$
k \frac{\partial^2 u}{\partial x^2}
=
k \frac{u^{n + 1}_{i + 1} - 2u^{n + 1}_{i} + u ^{n + 1}_{i - 1}}{(\Delta x)^2}
$$
So the original function becomes
$$
\frac{u^{n + 1}_{i} - u^{n}_{i}}{\Delta t} 
=
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
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & 0 & -r & 1+2r \\
  \end{array} } \right]
$$

This is unconditionally stable, and more computational expensive, but this specific 1-D senario can be solved with Thomas Algorithm, having the same complexity of Explicit Method


### Crank Nicolson Method

The Crank-Nicolson method is a semi-implicit scheme that averages the explicit and implicit methods, leading to second-order accuracy in both time and space. The heat equation is discretized as:
$$
k \frac{\partial^2 u}{\partial x^2}
=
\frac{1}{2}k 
\frac{(u^{n + 1}_{i + 1} - 2u^{n + 1}_{i} + u ^{n + 1}_{i - 1}) + (u^{n}_{i + 1} - 2u^{n}_{i} + u ^{n}_{i - 1})}{(\Delta x)^2}
$$

The original function becomes
$$
\frac{u^{n + 1}_{i} - u^{n}_{i}}{\Delta t} 
=
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
u ^ {n + 1} = A_1 ^ {-1} A_2 u ^{n}
$$
This is also unconditionally stable and more precise, but the time complexity is higher.

### Summary of 1-D Methods
- **Explicit Method**: Simple but conditionally stable, requiring small time steps to maintain stability.
- **Implicit Method**: Unconditionally stable, simple because we can use Thomas Algorithm to sovle.
- **Crank-Nicolson Method**: Unconditionally stable and more accurate than the implicit method, but computationally more expensive.

## 2-D Heat Equation
$$
\frac{\partial u}{\partial t} = k (\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2})
$$

Similarly, we can solve with different strategies


### Explicit Method
In the explicit method, we approximate the time derivative using a forward difference and the spatial derivatives using central differences.
$$
\frac{\partial u}{\partial t} = \frac{u_{i,j}^{n+1} - u_{i,j}^n}{\Delta t}
$$
and the second-order spatial derivatives:
$$
\frac{\partial^2 u}{\partial x^2} = \frac{u_{i+1,j}^n - 2 u_{i,j}^n + u_{i-1,j}^n}{(\Delta x)^2}
$$
$$
\frac{\partial^2 u}{\partial y^2} = \frac{u_{i,j+1}^n - 2 u_{i,j}^n + u_{i,j-1}^n}{(\Delta y)^2}
$$

Thus, the heat equation becomes:
$$
\frac{u_{i,j}^{n+1} - u_{i,j}^n}{\Delta t} = k \left( \frac{u_{i+1,j}^n - 2 u_{i,j}^n + u_{i-1,j}^n}{(\Delta x)^2} + \frac{u_{i,j+1}^n - 2 u_{i,j}^n + u_{i,j-1}^n}{(\Delta y)^2} \right)
$$

Rearranging we have
$$
u_{i,j}^{n+1} = u_{i,j}^n + r_x (u_{i+1,j}^n - 2 u_{i,j}^n + u_{i-1,j}^n) + r_y (u_{i,j+1}^n - 2 u_{i,j}^n + u_{i,j-1}^n)
$$
where
$$
r_x = \frac{k \Delta t}{(\Delta x)^2}, \quad r_y = \frac{k \Delta t}{(\Delta y)^2}
$$

This method is straightforward to implement, but to maintain stability, it must satisfy the **CFL condition**:
$$
r_x + r_y \leq \frac{1}{2}
$$

### Implicit Method
In the implicit method, the equation becomes:
$$
\frac{u_{i,j}^{n+1} - u_{i,j}^n}{\Delta t} = k \left( \frac{u_{i+1,j}^{n+1} - 2 u_{i,j}^{n+1} + u_{i-1,j}^{n+1}}{(\Delta x)^2} + \frac{u_{i,j+1}^{n+1} - 2 u_{i,j}^{n+1} + u_{i,j-1}^{n+1}}{(\Delta y)^2} \right)
$$

This can be rearranged to form a linear system:
$$
u_{i,j}^n = u_{i,j}^{n+1} - r_x (u_{i+1,j}^{n+1} - 2 u_{i,j}^{n+1} + u_{i-1,j}^{n+1}) - r_y (u_{i,j+1}^{n+1} - 2 u_{i,j}^{n+1} + u_{i,j-1}^{n+1})
$$

We can solve this linear system by mapping a 2D pair of indicies, $ i, j $, into one index, $ jN_{x} + i $, where each row only have 5 non-zero elements: one diagonal element and four neighbours. The size of new matrix is $ N_{x} N_{y} $.

This results in a sparse system of linear equations that can be solved at each time step. The implicit method is **unconditionally stable**. However, solving this linear system is computationally expensive than explicit method.

### Crank-Nicolson Method
We have

$$
\begin{aligned}
\frac{u_{i,j}^{n+1} - u_{i,j}^n}{\Delta t} = \frac{k}{2} \Bigg( &\frac{u_{i+1,j}^{n+1} - 2 u_{i,j}^{n+1} + u_{i-1,j}^{n+1}}{(\Delta x)^2} + \frac{u_{i,j+1}^{n+1} - 2 u_{i,j}^{n+1} + u_{i,j-1}^{n+1}}{(\Delta y)^2} \\
&+ \frac{u_{i+1,j}^n - 2 u_{i,j}^n + u_{i-1,j}^n}{(\Delta x)^2} + \frac{u_{i,j+1}^n - 2 u_{i,j}^n + u_{i,j-1}^n}{(\Delta y)^2} \Bigg)
\end{aligned}
$$

Similarly, we can also map this into a sparse matrix with size $ N_{x} N_{y} $ This can be written in matrix form:
$$
A_1 u^{n+1} = A_2 u^n
$$
This system is more accurate and unconditionally stable. However, it's even more **computational expensive** than the implicit method.

### Summary of 2-D Methods
- **Explicit Method**: Simple but conditionally stable, requiring small time steps to maintain stability.
- **Implicit Method**: Unconditionally stable, but requires solving a linear system at each time step.
- **Crank-Nicolson Method**: Unconditionally stable and more accurate than the implicit method, but computationally more expensive.
