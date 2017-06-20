#演算法筆記
===========

## while v.s. for (2017/06/15)

在大部分的情況下，while和for相差無異，大部分為了方便都會用for，可是善加利用while會使演算法速度飛升！
- for loop的大小在設定好之後就固定，但是wihle loop的condition可以在每一次迭代中調整。
- for在skip case的時候只能一個一個skip，但是若只用while配合上index可以一次skip掉多個cases
- 在許多搜索情況下，可以設定兩個index(init, end)，自兩個搜索端點開始搜尋，並配合兩者之間的condition，動態增減index。

## bitwise is WAY better (2017/06/16)
在一般情況下，若非題目由明確指示，不太會有人發神經用bitwise的方式來解題。今天頗ㄏ的遇到了一題(136-single-number)。
首先我們要了解XOR的好，才能善用它的特性。所有(整數 XOR 0) = 整數，而且(整數 XOR 整數) = 0，挖咧幹你老師咧，這樣這題根本比烙賽還快(最近梅雨季，腸胃有點不好)！
- bitwise manupulation is way better if you know its properties
- interger XOR 0 = interger; interger XOR integer = 0 -> intergerA XOR integerB XOR intgerA = (integerA XOR integerA) XOR integerB = integerB