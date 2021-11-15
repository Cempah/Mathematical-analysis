#!/usr/bin/env python
# coding: utf-8

# ## Практическое задание. Урок 2.

# ### 1. Представьте в виде несократимой рациональной дроби:  
# **а)0.(216);**  
# **б)1.0(01).**

# а) $0.(216)$
# 
# $d = 0.(216)$
# 
# $1000d = 216.(216)$
# 
# $1000d = 216 + 0.(216)$
# 
# $1000d = 216 + d$
# 
# $999d = 216$
# 
# $d = \frac{216}{999} = \frac{8}{37}$
# 
# $0.(216) = \frac{8}{37}$

# б) $1.0(01)$
# 
# $d = 1.0(01)$
# 
# $10d = 10.(01)$
# 
# $0.(01)$
# 
# $c = 0.(01)$
# 
# $100c = 1.(01)$
# 
# $100c = 1 + 0.(01)$
# 
# $100c = 1 + c$
# 
# $99c = 1$
# 
# $c = \frac{1}{99}$
# 
# $0.(01) = \frac{1}{99}$
# 
# $10d = 10 + 0.(01)$
# 
# $10d = 10 + \frac{1}{99}$
# 
# $10d = \frac{990 + 1}{99}$
# 
# $10d = \frac{991}{99}$
# 
# $d = \frac{991}{990}$
# 
# $1.0(01) = \frac{991}{990}$

# #### 2*. Пусть  $x=\frac{2}{21}$. Известно, что для некоторого натурального  k  число  x  записывается в  k  - ичной системе счисления как 0.(13)k=0,131313...k .  Найдите  k .

#  

# #### 3. Проверьте любым способ, является ли данные логические формулы тавтологией:  
# a) $(A∨B)→(B∨\overline A)$  
# б) $A→(A∨(\overline B∧A))$

# a) $(A∨B)→(B∨\overline A)$

# <table>
# <thead>
# <tr><th>$A$</th><th>$B$</th><th>$(A ∨ B)$</th><th>$\overline A$</th><th>$(B ∨ \overline A)$</th><th>$(A∨B)→(B∨\overline A)$</th></tr>
# </thead>
# <tbody>
#     <tr><td>$0$</td><td>$0$</td><td>$0$</td><td>$1$</td><td>$1$</td><td>$1$</td></tr>
#     <tr><td>$0$</td><td>$1$</td><td>$1$</td><td>$1$</td><td>$1$</td><td>$1$</td></tr>
#     <tr><td>$1$</td><td>$0$</td><td>$1$</td><td>$0$</td><td>$0$</td><td>$0$</td></tr>
#     <tr><td>$1$</td><td>$1$</td><td>$1$</td><td>$0$</td><td>$1$</td><td>$1$</td></tr>
# </tbody>
# </table>

# $(A∨B)→(B∨\overline A)$ - не является тавтологией

# б) $A→(A∨(\overline B∧A))$ = $A→(A∨\overline B)∧(A∨A)$ = $A→A∧(A∨\overline B)$ = $A→A$

# «Из A следует A» — закон тождества, является тавтологией

# #### 4. Сформулируйте словесно высказывания:
# 
# a) $(\overline A∨B)→\overline C$
# 
# б) $C→(A∨\overline B)$
# 
# A:  сегодня светит солнце;
# 
# B:  сегодня сыро;
# 
# C:  я поеду на дачу.

# a) $(\overline A∨B)→\overline C$  
# Если сегодня не светит солнце и сегодня сыро, то я не поеду на дачу.

# б) $C→(A∨\overline B)$  
# Если я поеду на дачу, то сегодня будет светить солнце и не будет сыро.

# #### 5. Пользуясь правилом построения противоположного высказывания, запишите утверждения, противоположные следующим:
# 
# **a) На любом курсе каждого факультета есть студенты, сдающие все экзамены на «отлично».**
# 
# **б) В любом самолете на рейсе Вашингтон-Москва присутствует хотя бы один сотрудник силовых органов, в каждой пуговице одежды которого вмонтирован микрофон.**

# a) *На любом курсе каждого факультета есть студенты, сдающие все экзамены на «отлично».*  
# На любом курсе $\forall$ факультета $\exists$ студенты, сдающие $\forall$ экзамены на «отлично».
# 
# *На любом курсе есть факультет, в котором каждый студент сдаёт хотя бы один экзамен на «отлично».*  
# На любом курсе $\exists$ факультет, в котором $\forall$ студент сдаёт $\exists$ экзамен на «отлично».

# б) *В любом самолете на рейсе Вашингтон-Москва присутствует хотя бы один сотрудник силовых органов, в каждой пуговице одежды которого вмонтирован микрофон.*  
# В любом самолете на рейсе Вашингтон-Москва присутствует $\exists$ сотрудник силовых органов, в $\forall$ пуговице одежды которого вмонтирован микрофон.
# 
# *В любом самолете на рейсе Вашингтон-Москва каждый присутствующий сотрудник силовых органов, имеет хотя бы одну пуговицу одежды в которую вмонтирован микрофон.*  
# В любом самолете на рейсе Вашингтон-Москва $\forall$ присутствующий сотрудник силовых органов, имеет $\exists$ пуговицу одежды в которую вмонтирован микрофон.

# #### 6*. Прочитайте высказывания, установите их истинность и постройте противоположное высказывание:
# 
# $$a)\,\,\, \forall x\in\mathbb{R}\,\,\,\exists X\in\mathbb{R}:\,\,\, X>x;$$
# $$б)\,\,\, \forall y\in\Bigl[0; \frac{\pi}{2}\Bigr]\,\,\,\exists \varepsilon>0:\,\,\, \sin y<\sin(y+\varepsilon);$$
# $$в)\,\,\, \forall y\in\Bigl[0; \pi\Bigr)\,\,\,\exists \varepsilon>0:\,\,\, \cos y>\cos(y+\varepsilon).$$
