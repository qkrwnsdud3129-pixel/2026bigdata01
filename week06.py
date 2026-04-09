#배열의구조와정보를파악할때사용합니다.(arr가배열일때)
#arr.shape:배열의크기(예:(3,4)는3행4열)
#arr.ndim:차원수(1차원,2차원등)
#arr.dtype:요소의데이터타입(int64,float64등)
#arr.size:전체요소의개수

#1.메모리관련속성
#arr.itemsize:각요소(Element)하나가차지하는바이트(byte)수입니다.
#arr.nbytes:배열전체가차지하는총바이트수입니다.(itemsize*size와같습니다.)
#arr.strides:다음요소나다음행으로이동하기위해메모리상에서몇바이트를건너뛰어야하는지나타내는튜플입니다.
#2.데이터표현속성
#arr.T:배열의전치(Transpose)된결과입니다.(행과열을바꿈)
#arr.flat:다차원배열을1차원으로펼친상태의반복자(Iterator)입니다.
#arr.real/arr.imag:복소수배열일경우각각실수부와허수부를반환합니다.
#3.기타상태확인
#arr.flags:배열의메모리배치방식(C-style인지Fortran-style인지),쓰기가능여부등을보여줍니다.
#arr.base:이배열이다른배열의뷰(View)인지,아니면독자적인데이터를가진객체인지확인해줍니다. (메모리 절약을

import numpy as np

#array01 = np.random.random((2,3,3))
array01 = np.random.random((4,2))
print(array01)
print(array01.shape, array01.dtype, array01.ndim, array01.size)
print(array01.T)