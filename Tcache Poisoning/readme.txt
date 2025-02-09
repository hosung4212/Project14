이거 어려움 일단 tcache는 LIFO라서 나중에 들어온게 맨 처음 나간다. 그럼 이 청크는 free가 됐을 때 다음에 사용할 청크의 위치를 next pointer로 갖게 되는데 이건 그 next pointer를 조작하는 방식이다.

일단 nextpointer 다음에 tcache라는 글자가 적히는데 이걸 조작하면 free를 두번 할 수 있다. 이 tcache라는 글자의 무결성을 검증하면서 tcahce 자체의 더블 프리를 막기 때문이다.
그럼 edit을 이용해서 tcache라는 글자를 조작하고 내가 원하는 주소를 도출해낸다. 
여기서는 stdout pointer를 이용하는데 원래 오프셋은 맨 끝자리는 같기 때문에 LSB만 오프셋에서 따와서 원래 stdout pointer에 들어있는 값을 출력해낼 수 있다. 
 
