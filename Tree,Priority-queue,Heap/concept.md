# 비선형구조와 트리
## 그래프   
✔️ 정점(vertex)과 간선(edge)으로 이루어져 있는 자료구조   
- *정점* - 자료, 상태 등 뭔가를 담고 있음, 노드라고도 표현
- *간선* - 정점 간의 관계를 나타냄
  - 방향이 있을 수도, 없을 수도 있음
  - 방향이 있는 그래프를 유향 그래프
- 어떤 정점에서 간선을 통해 다른 정점으로 이동할 수 있음
- *경로* - 어떤 정점에서 다른 정점으로 이동하기 위해 거치는 모든 정점
- *사이클* - 처음 시작한 정점으로 다시 돌아오는 경로

## 트리   
✔️ 그래프의 특수한 형태 중 하나   
- 간선들은 모두 방향성을 가짐
- 어떤 정점을 가리키는 정점의 개수는 최대 1개
- 어떤 정점에서 다른 정점으로 이동할 수 있는 경로는 1개
- 사이클을 갖지 않음
- *루트 노드* - 다른 어떠한 정점도 가리키지 않는 정점
- *깊이* - 루트 노드로부터의 거리
- *리프 노드* - 가리키는 정점이 없는 노드

### 이진트리   
✔️ 각 정점들이 자식 노드를 최대 2개까지만 갖는 트리   
- *포화 이진 트리*
  - 리프 노드를 제외한 모든 정점이 항상 자신을 2개씩 갖고 있으면서 모든 리프 노드의 깊이가 동일한 트리
  - 높이를 h라고 할 때, 정점의 개수는 항상 2^h - 1 개
- *완전 이진 트리*
  - 마지막 깊이를 제이하고 모든 정점이 완전히 채워져 있으며, 마지막 깊이의 정점들은 가능한 한 왼쪽에 있는 트리   
  - 높이를 h라고 할 때, 정점의 개수는 2^h-1개 이상 2^h - 1개 이하
- *정 이진 트리*
  - 리프 노드를 제외한 모든 노드들이 두 개의 자식 노드를 갖고 있는 이진 트리
  - 모든 정점은 0개 또는 2개의 자식 노드를 가짐

# 트리의 표현 방법
## 이진트리
```py
class TreeNode:
  def __init__(self):
    self.left = None  # 왼쪽 자식
    self.right = None # 오른쪽 자식
```

## 완전 이진 트리   
✔️ 배열을 이용하여 간단하게 구형 가능   
- 어떤 정점의 번호가 n이면 왼쪽 자식은 2n, 오른쪽 자식은 2n + 1
- 인덱스 0은 사용하지 않음

# 트리 순회하기   
✔️ 트리의 모든 노드를 방문하는 순서   

## 깊이 우선 탐색(DFS)      
✔️ 재귀 호출을 사용하는 알고리즘   
- 기존 트리에서 하위의 트리 구조를 서브 트리
- 정점을 언제 방문하는지에 따라 순서가 달라짐

1. *전위 순회* - 루트 방문 -> 왼쪽 서브 트리 순회 -> 오른쪽 서브 트리 순회   
![image](https://user-images.githubusercontent.com/48720589/161880527-8a2e5abe-a014-453d-a161-fb9e5faae9dd.png)   

2. *중위 순회* - 왼족 서브 트리 순회 -> 루트 방문 -> 오른쪽 서브 트리 순회   
![image](https://user-images.githubusercontent.com/48720589/161880555-1abe00c4-8ecd-4415-ba01-fe3ea0419705.png)   

3. *후위 순회* - 왼쪽 서브 트리 순회 -> 오른쪽 서브 트리 순회 -> 루트 방문      
![image](https://user-images.githubusercontent.com/48720589/161880594-52aa3996-933c-46bd-9698-7fa2a6b4c4ea.png)   

## 너비 우선 탐색(BFS)   
✔️ 큐 자료구조를 이용하여 구현   
- 현재 정점과 이웃한 정점일수록 먼저 방문해야 하므로 큐를 이용   
![image](https://user-images.githubusercontent.com/48720589/161880842-340ec869-7f72-4cf8-bec4-0a766069ba1a.png)   



