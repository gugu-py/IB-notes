
variables use `UPPERCASE`
methods and fields use `lowercase`
`loop X from 0 to 99` executes 100 times ($x=[0,99]$)
`output X` prints `X`
use `end` to mark the end of code block of `if`, `loop`, `while`

bubble sort (basic):
```pseudocode
ARRAY=[...]
loop I from 0 to ARRAY.size()-1
	loop J from 1 to ARRAY.size()-1
		if ARRAY[J-1] > ARRAY[J]
			TMP=ARRAY[J-1]
			ARRAY[J-1]=ARRAY[J]
			ARRAY[J]=TMP # swap
		end if
	end loop
end loop
```

bubble sort (optimized):
``` pseudocode
ARRAY=[...]
loop I from 0 to ARRAY.size()-1
	FLAG=0
	loop J from 1 to ARRAY.size()-1-I
		if ARRAY[J-1] > ARRAY[J]
			TMP=ARRAY[J-1]
			ARRAY[J-1]=ARRAY[J]
			ARRAY[J]=TMP # swap
			FLAG=1
		end if
	end loop
	if FLAG==0
		break
	end if
end loop

```



selection sort


```pseudocode
ARRAY=[...]
loop I from 0 to ARRAY.size()-2
	MN=I
	loop J from I+1 to ARRAY.size()-1
		if ARRAY[J]<ARRAY[MN]
			MN=J
		end if
	end loop
	TMP=ARRAY[I]
	ARRAY[I]=ARRAY[MN]
	ARRAY[MN]=TMP
end loop
```

binary search: watch ==integer division== and ==boundary==

``` pseudocode
ARRAY=[...] # assume ascending
T=... # target
L=0
R=ARRAY.size()-1
MID=0
loop while L<=R
	MID=(L+R) div 2 # integer division
	if T>ARRAY[MID]
		L=MID+1
	else if T<ARRAY[MID]
		R=MID-1
	else
		break
	end if
end loop
if ARRAY[MID]==T
	output MID
else
	output -1
end if
```

Collection:

```pseudocode
GRADE = Collection()

GRADE.resetNext() // reset pointer

loop while GRADE.hasNext()
	output GRADE.getNext()
end loop
```

## common tricks

if asked for sub-program, use function

