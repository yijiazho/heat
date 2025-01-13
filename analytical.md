The 1D heat equation is
$$
\frac{\partial u}{\partial t} = k \frac{\partial^2 u}{\partial x^2}
$$
where $ u(x, t) $ is the temperature distribution, k is thermal diffusivity.

The boundary conditions we have is 
$$
u(0, t) = 200, \\ u(L, t) = 200, \\ u(x, 0) = 0
$$

In order to simplify we can have
$$
u(x, t) = v(x, t) + 200
$$

and 
$$
v(x, t) = F(x) G(t)
$$

so the partial differential equation becomes 
$$
F(x)\frac{dG(t)}{dt} =
k G (t)\frac{d^2 F(x)}{d x^2}
$$

We have
$$
\frac{G'}{G} = k\frac{F''}{F}
$$

and both sides must be a constant. The boundary conditions become

$$
F(0)G(t) = 0, \\
F(L)G(t) = 0,\\
F(x)G(0) = -200
$$

Solving this PDE with boundaries we have

$$
F(x) = \sum_{n = 1}^{\infty} A_n sin(\frac{n \pi x} {L}) 
$$

$$
G(t) = e^{- \frac{n^2 \pi^2kt}{L^2}}
$$

At t = 0 we have
$$
\sum_{n = 1}^{\infty} A_n sin(\frac{n \pi x} {L})  = -200
$$
for $ F(x) $ both sides multiply by the same factor $sin (\frac{m \pi x}{L})$, and integral from 0 to L

Use the orthogonality of sin we can have left side equals to

$$
\int_0^L \sum_{n=1}^{\infty} A_n sin(\frac{n \pi x}{L}) sin (\frac{m \pi x}{L}) dx = \frac{L}{2} A_m
$$

and right side equals to

$$
\int_0^L -200 sin(\frac{m \pi x}{L})dx = \frac{200L}{m \pi} ((-1) ^ m - 1)
$$

We have 
$$
A_m = \frac{400}{m \pi} ((-1) ^ m - 1)
$$

So the original tempeture becomes

$$
u(x, t) = 200 + \sum_{n = 1}^\infty \frac{400}{n \pi} ((-1) ^ n - 1) sin(\frac{n \pi x}{L}) e ^{- \frac{n^2 \pi^2 k t} {L ^ 2}}
$$