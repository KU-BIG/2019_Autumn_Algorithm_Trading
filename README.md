# 2019_Autumn_Algorithm_Trading

## References
[파이썬으로 배우는 알고리즘 트레이딩](https://wikidocs.net/book/110)

머신러닝을 통한 알고리즘 트레이딩 시스템 개발  

알고리즘 트레이딩 1, 2, 3

딥러닝/강화학습 주식투자

## Solve Windows Dependency

[docker의 ubuntu container에 ssh로 접속하기](https://chanhy63.tistory.com/11)

### 예상 해결방법
- Windows에 필요 api 설치
- Windows에서 C:\를 마운트하여 Ubuntu Container 실행 (Docker)
- 해당 Ubuntu Container에서 ssh server를 열고, 외부에서 접속
- Ubuntu가 돌고있지만, Windows가 깔린 C:\를 접근할수 있는 환경 완성..?

**->이렇게 했을때 컨테이너속의 python3이 api를 제대로 활용할수 있는지 확인 필요**
