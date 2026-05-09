## Differentiation

inflexion(inflection) point at $x=k$ satisfies:
1. $f''(k)=0$ or $f''(k) \text{ does not exist}$
2. sign changes around $f''(k)$

```prompt
give examples of f''(a)=:
1. 0, and around it sign changes
2. does not exist, and sign changes
3. 0, and around it sign does not change
4. does not exist, and sign does not change

use python to draw diagrams and label them. draw f(x), f'(x), and f''(x) in one plot
```

concave:
1. up (like a cup): $f''(x)>0$
2. down (a cap): $f''(x)<0$

## Integration

workflow:
1. Do I need to simplify it? Is it a fraction with larger power underneath? -> partial fraction and go to the top
2. is it in my formula booklet? check both integral and differentiation(in reverse)
3. do I need to apply chain rule/substitution? $\int f(g(x))\\ g'(x) dx$
4. is it the product of two functions? -> reverse product rule
5. give up

seeing $cos^2(x)$ or $sin^2(x)$, use double angle law to reduce power

==reverse product rule== $u$ priority:
1. log
2. inverse trig
3. $x^n$
4. trig
5. $e^x$

if asked to substitute something as $u$, express everything in $u$ would be much easier sometimes

## Euler Method

given step length $h$, $f(x_0)=y_0$, and expression $f'(x)$ or $\frac{dy}{dx}$, calculate $x_n,y_n$

1. in calculator, define function: `g(x,y):=x^2+y^2` as the derivative of $f(x)$ and step `h:=0.1`
2. spreadsheet:

| x       | y        | $\Delta$      |
| ------- | -------- | ------------- |
| $x_0$   | $y_0$    | `=g(a1,b1)*h` |
| `=a1+h` | `=b1+c1` | `=g(a2,b2)*h` |
| ...     | ...      | ...           |

## Differential Equation

1. try seperate variable to 2 sides and integrate two sides
2. partial fraction
3. if in homogeneous form
	1. identify: use $v=\frac{x}{y}$, verify that the equation can be written as $\frac{dy}{dx}=f(v)$
	2. write $v=\frac{x}{y}$ as $y=vx$, then $\frac{dy}{dx}=\frac{dv}{dx}x+v$
	3. then solve $\frac{dy}{dx}=\frac{dv}{dx}x+v=f(v)$, and substitute $\frac{x}{y}$ back
4. else, use integrating factor $I(x)$;
	1. in integrating of $I(x)$, no need to apply the constant (they cancel out on both sides with division)
	2. simplify $I(x)$ and apply the factor; you should be able to use reverse product rule with $\frac{dy}{dx}$, so that
	3. the original $\frac{dy}{dx}+P(x)y=Q(x)$ became something like $\frac{d}{dx}(f(x)y)=g(x)$
	4. integrate $dx(g(x))$ at right, then done: $f(x)y=h(x)+C$
	5. simplify: $y=\frac{h(x)+C}{f(x)}$

## Maclaurin Series

尽量使用基本公式
但是maclaurin series不能composite。例如我对$e^{fx}$的e展开，然后再对fx展开，大概率出问题。此时老老实实微分吧

