#演算法筆記
===========

## while v.s. for (2017/06/16)

在大部分的情況下，while和for相差無異，大部分為了方便都會用for，可是善加利用while會使演算法速度飛升！
- for loop的大小在設定好之後就固定，但是wihle loop的condition可以在每一次迭代中調整。
- for在skip case的時候只能一個一個skip，但是若只用while配合上index可以一次skip掉多個cases
- 在許多搜索情況下，可以設定兩個index(init, end)，自兩個搜索端點開始搜尋，並配合兩者之間的condition，動態增減index。

