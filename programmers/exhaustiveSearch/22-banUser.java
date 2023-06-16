import java.util.*;

// 불량 사용자
        public class Solution {
            // 재귀 메서드
            // 돌아가면서 밴을 먹일 수 있는 모든 경우를 조합
            private void count(int index, Set<String> banned, String[][] bans, Set<Set<String>> banSet){
                if (index == bans.length){
                    banSet.add(new HashSet<>(banned));
                    return;
                }

                for (String id : bans[index]){
                    if(banned.contains(id)) continue;
                    banned.add(id);
                    count(index + 1, banned, bans, banSet);
                    banned.remove(id);
                }
            }

            public int solution(String[] user_id, String[] banned_id){
                // 각 밴 아이디의 경우에 따라서, 맞는 아이디들을 찾음
                // 예시, fr*d* --> frodo, fradi
                //      abc1** --> abc123
                // = [frodo, fradi] [abc123]
                String[][] bans = Arrays.stream(banned_id)
                        .map(banned -> banned.replace('*','.'))
                        .map(banned -> Arrays.stream(user_id)
                                .filter(id -> id.matches(banned))
                                .toArray(String[]::new))
                        .toArray(String[][]::new);

                Set<Set<String>> banSet = new HashSet<>();
        count(0, new HashSet<>(), bans, banSet);
        return banSet.size();

    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String[] input1 = {"frodo", "fradi", "crodo", "abc123", "frodoc"};
        String[] input2 = {"fr*d*", "abc1**"};
        int result = answer.solution(input1, input2);

        System.out.print(result);
    }
}
