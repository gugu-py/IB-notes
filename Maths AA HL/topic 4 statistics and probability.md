## concepts

### statitics

box whisker

![[_resources/Pasted image 20260320093710.png]]

left skew/right skew:
1. 哪里腿长(first compare whisker, then compareMed-Q1 or Q3-Med)
2. =哪里skew; above is left skew


$$
Y = aX + b \quad \Rightarrow \quad \mathrm{Var}(Y) = a^2 \mathrm{Var}(X)
$$

### Probability

if $A$ and $B$ are independent, $P(A) \times P(B) = P(A \cap B)$

### Distribution

#### Normal Distribution

empirical rule: 68, 95, 99.7

![[_resources/Pasted image 20260409101750.png]]


## 敌人图鉴

### permutation and combination

分堆问题：

9 items divide into two groups of 4 and 5: 9C4

8 items divide into two equal group: 8C4 / 2!

9 items divide into 3 equal groups: 9C3 \* 6C3 / 3!

9 items divide into 3 groups: 2, 2, 5: 9C2 \* 7C2 / 2!

捆绑法

插9 items divide into 3 groups: 2, 2, 5: 9C2 \* 9C2 / 2! is this correct?板法

正难则反：total cases - complementary cases

### probability

$\Sigma{P(x)}=1$ and $P(x)$ always has range $[0,1]$

draw cards without replacement, 抽一张分子和分母减一张

probability density function:
- ask for probability over interval: integration

### Statistics GDC

one-variable (with frequency)
1. spreadsheet
2. frequency(f) and x as variable names of columns
3. enter data
4. menu -> statistics -> stat calculation -> one variable
5. x1 list: x; frequency list: f

two-variable:
- $r>0$ positive relationship; $r<0$ negative relationship
- $y=a_1 x+b_1$ can only used to predict $y$; $x=a_2 y+b_2$ vice versa; both pass through $(\bar{x},\bar{y})$

### normal distribution

z-score: transform a given normal distribution to the standard form, so that $P(X>x_\text{original value}) = P(Z > z_\text{position in standard form})$

已知分布和标准分布，求约束条件下的概率：用标准分布公式表示约束，注意$X~N(\mu, \sigma^2)$第二个参数是方差而非标准差 

例子：
![[_resources/Pasted image 20260215151203.png]]

#### GDC

normal CDF: get possibility(area) from boundary

inverse normal CDF: get right boundary from possibility(area), and assume left boundary is $- \infty$ 

### Binomial Distribution

#### GDC

binomial PDF: get probability of exact $n$ successes from $k$ total trials and success probability

binomial CDF: get cumulative probability of at most $n$ success from $k$ total trials and success probability

reversed binomial: get the $n$ successes from cumulative success probability, total trial number, single success probability

reversed binomial N: get the number of total trials from success number and success probability that is larger than the cumulative probability