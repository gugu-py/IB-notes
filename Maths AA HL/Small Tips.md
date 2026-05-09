## Number & Algebra

![[RV prac/Maths/_resources/Pasted image 20240827154321.png]]

For this kind of task, you only need to represent things(sum, a certain term, etc.) using `r`(common ratio). Then solve the equation of `r`.

-----

![[RV prac/Maths/_resources/Pasted image 20240831093509.png]]

It is `after n years`, not `the n-th year`. In that way, the formula should be $x^n$, not $x^{n-1}$.

---

![[RV prac/Maths/_resources/Pasted image 20240920141504.png]]

$log$ or $ln$ on both side to get the indices.

## Trig

for $a \times sin(x)+b \times cos(x)$ to be written as $R \times sin(x+c)$, $R$ can be found by $\sqrt{a^2+b^2}$ 

### An example for solving $arctan$ related equation

The equation given involves an expression of the form 
$$\tan(\arcsin x).$$
In order to solve for $x$, one of the key steps shown in the solution is to rewrite
$$\tan(\arcsin x)$$ 
as 
$$\frac{\sin(\arcsin x)}{\cos(\arcsin x)}.$$
From there, we use $\sin(\arcsin x) = x$ and $\cos(\arcsin x) = \pm \sqrt{1 - x^2}$ to express everything purely in terms of $x$. This approach makes it straightforward to isolate $x$ and solve the resulting algebraic equation.

---

**Why We Write $\tan(\arcsin x)$ as $\frac{\sin(\arcsin x)}{\cos(\arcsin x)}$ Instead of Using $\arctan$ Directly**

1. **Directly Relating to $x$**

   - By definition, $\arcsin x$ is the angle $\theta$ in the range $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ for which $\sin \theta = x$.
   - Hence, $\sin(\arcsin x) = x$ and $\cos(\arcsin x) = \pm \sqrt{1 - x^2}$.
   - Rewriting 
   $$\tan(\arcsin x) = \frac{\sin(\arcsin x)}{\cos(\arcsin x)}$$ 
   gives an expression directly in terms of $x$. This makes the equation purely algebraic in $x$, which is much more straightforward to solve.

2. **Avoiding Domain/Range Complications**

   - If we tried to “apply $\arctan$” on both sides or use an identity like $\arctan(\tan(\arcsin x))$, we would run into potential domain-range issues.
   - $\arcsin x$ takes values in $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$, while $\arctan$ has its own principal range $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$. Even though these intervals overlap, confusion can arise if one tries to cancel $\arctan$ and $\tan$ without carefully tracking signs and quadrants.
   - Writing 
   $$\tan(\arcsin x) = \frac{x}{\sqrt{1 - x^2}}$$ 
   sidesteps these complications by keeping the equation entirely in real-algebraic form.

3. **Clear Path to an Algebraic Equation**

   - Once 
   $$\tan(\arcsin x) = \frac{x}{\sqrt{1 - x^2}},$$ 
   the rest of the steps (isolating $x$, squaring, etc.) become a straightforward exercise in algebra.
   - This method also allows us to keep track of the necessary domain restrictions (like $|x|\le 1$ from the definition of $\arcsin$, and sign choices for $\cos(\arcsin x)$).

In short, rewriting 
$$\tan(\arcsin x)$$ 
in terms of sine and cosine (and then in terms of $x$) is the cleanest, most direct way to solve the equation without running into tricky domain/range problems that arise from trying to apply inverse functions in the wrong order.

## Calculus

条件洞察：know what information and situation is provided, especially when only one integral and differentiation is provided
符号抽象

concave-up: $f''(x)>0$
concave-down: $f''(x)<0$

### 易错

积分内的系数不要忘记: $\int a \times f(x) dx$
不要看错带指数的括号：$(2x)^3 \ne 2x^3$
M series的公式divide by factorio 不要忘记


### Integration

reverse chain rule

$$
\int f'(x)g'(f(x)) dx = g(f(x))+c
$$

### M series

> Just expand. If composite function, expand outer layer, then expand inner layer. When see function capable of transformation, use transformation first, and then expand. 

![[_resources/Pasted image 20250917230101.png]]

use $\frac{\text{M series}}{x^3}$, see it is undetermined form. Use L'Hopital. Ignore all other terms except the one with the same power as $x^3$, apply L'Hopital rule 指数 times, you get result very fast

![[_resources/Pasted image 20250924151732.png]]

Brutal Force, first expand the $\cos(...)$, make $\ln(1+x)$ as $x$, and then expand the $\ln(1+x)$ term into M series, then expand. Fuck.

### Inverse Trig Integration

![[_resources/Pasted image 20250922000630.png]]

enhance this flow and read [method](https://www.revisionvillage.com/ib-math/analysis-and-approaches-hl/boot-camps/calculus/integration/mixed-quotients/) again

## Complex Number

$$
z_1=r_1cis(\theta_1)
$$

$$
z_1z_2=r_1r_2\times cis(\theta_1+\theta_2)
$$

$$
\frac{z_1}{z_2}=\frac{r_1}{r_2} \times cis(\theta_1-\theta_2)
$$

$$
cis(\theta_1)\times cis(\theta_2)=cis(\theta_1+\theta_2)
$$
if the equation has complex number as 系数, then the complex solutions do not come in conjugate pairs
