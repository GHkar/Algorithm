# 가사 검색 - 트라이

# 1. 트라이 자료 구조 생성
class Node(object):
    def __init__(self, key):
        self.key = key  # 현재 위치에서 가지고 있는 단어
        self.count = 0
        self.children = {}

# 초기화, 부모 노드 정보 넣기
class Trie(object):
    def __init__(self):
        self.head = Node(self)

    # 삽입
    def insert(self, string):
        current = self.head

        for char in string:
            current.count += 1
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]

    # 탐색
    def starts_with(self, prefix):
        current = self.head
        result = 0

        for char in prefix:
            if char == '?' : break
            if char in current.children: current = current.children[char]
            else : return 0

        return current.count

# 2. 단어를 받아 트라이에 데이터를 채움
def solution(words, queries):
    answer = []
    tries = {}
    reverse_tries = {}

    # 데이터 채우기
    for word in words:
        size = len(word)
        if size not in tries:
            tries[size] = Trie()
            reverse_tries[size] = Trie()

        tries[size].insert(word)
        reverse_tries[size].insert(word[::-1])

    # 3. 쿼리에 맞춰 탐색 진행
    for query in queries:
        if len(query) in tries:
            if query[0] != '?':
                trie = tries[len(query)]
                answer.append(trie.starts_with(query))
            else:
                trie = reverse_tries[len(query)]
                answer.append(trie.starts_with(query[::-1]))
        else: answer.append(0)

    return answer

# 입력
input1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
input2 = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(input1, input2))
