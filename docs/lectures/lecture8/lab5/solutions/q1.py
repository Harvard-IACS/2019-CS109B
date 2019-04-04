**solution**
```
-2-2-2 = -6 top left corner<br>
$n'$ = $(n - f + 2*0)/s + 1$<br>
n'=output size, n=input size, f=kernel size, p=padding, s=stride<br>
n' = (6-3)/1 + 1 = 4<br>
```
model.add(Conv2D(2, (3, 3), input_shape=(6, 6, 3), activation='relu'))


