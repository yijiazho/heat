# Project

This project is the simulation of the heat transfer in one dimension

## Getting started

### Set up virtual environment
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
```

### Install requirements
```
pip install -r requirements.txt
```

### Run application
```
pip install fastapi uvicorn
```

## Summary
I would like to write paper about the heat equation, since one dimensional static heat equation 
$$
\frac{\partial u}{\partial t} = k \frac{\partial^2 u}{\partial x^2}
$$

Can be solved numerically by substituting derivative with delta
$$
\frac{u^{n + 1}_{i} - u^{n}_{i}}{\Delta t} 
\approx 
k \frac{u^{n}_{i + 1} - 2u^{n}_{i} + u ^{n}_{i - 1}}{(\Delta x)^2}
$$
Assume 
$$
r = \frac{k \Delta t}{(\Delta x)^2}
$$

in explicit method which is not guaranteed stable
$$
u^{n + 1}_{i} = u^{n}_{i} + r (u^{n}_{i + 1} - 2 u^{n}_{i} + u^{n}_{i - 1})
$$

or in implicit method which is guaranteed to be stable
$$
-ku^{n + 1}_{i - 1} + (1 + 2k)u^{n + 1}_{i} - ku^{n + 1}_{i + 1} = u^{n}_{i}
$$

For the explicit method it is equivalent to
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

which can be solved recursively

For the implicit method it is equivalent to
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

This is a tridiagnoal system that can be solved by Thomas Algorithm, mentioned in the textbook chapter 11

Now the major probelm is that I could not find a lot of papers regarding the one-dimensional heat equation as it's too simple and far from real world problem. In order to meet the requirement of citation I have to find some paper that focus on a real world scenario, like a fuel cell model with both 3-D heat equation in both solid and fluid. However, in order to solve such problem, a simulation tool like COMSOL Multiphysics or ANSYS Fluent. So I would spend some time introducing these paper that is closer to real-world problem in my paper after doing the numercial solution of 1-D heat equation.