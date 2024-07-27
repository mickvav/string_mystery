# String concatenation mystery

A very simple problem seems to be O(n^2) in golang, but O(n) in python. Why?

![image](plot.png)

Let's dig and see

How?

Let's use black-box solution - just dig cpython source code _history_.



```
git clone https://github.com/python/cpython.git
cd cpython

mkdir ../target

target=$(cd ../target; pwd)
./configure --target=$target --enable-optimizations
make -j 4 python
./python ../main.py 
10 1.5735626220703125e-05
100 7.796287536621094e-05
1000 0.0009021759033203125
10000 0.00934290885925293
100000 0.09724044799804688
1000000 0.9724068641662598
git log | grep -B 2 2019 + | head -n 3
commit d0c92e81aa2171228a23cb2bed36f7dab975257d
Author: Batuhan Taşkaya <47358913+isidentical@users.noreply.github.com>
Date:   Tue Dec 31 05:31:52 2019 +0300
git checkout d0c92e81aa2171228a23cb2bed36f7dab975257d
./configure --target=$target --enable-optimizations
make -j 4 python

./python ../main.py
10 1.52587890625e-05
100 9.274482727050781e-05
1000 0.001028299331665039
10000 0.011281967163085938
100000 0.11533236503601074
1000000 1.1466484069824219
```
So, in 2019 optimisation _was already there_.


git log | grep -B 2 '2010 +' | head -n 3
commit 8dff4bada79d3662f8c799ea4572d51a2f8eed0a
Author: Raymond Hettinger <python@rcn.com>
Date:   Fri Dec 31 23:23:06 2010 +0000
git clean -f
git checkout 8dff4bada79d3662f8c799ea4572d51a2f8eed0a 
