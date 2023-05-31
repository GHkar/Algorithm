// 문자열 내 p와 y의 개수
public class Solution {

    public boolean solution(String s){
        // 문자열을 모두 소문자로 변환
        s = s.toLowerCase();

        // p의 개수 세기
        // 문자열에 등장하는 모든 "p"를 빈 문자열 ""로 치환
        // 원본 문자열과 변환된 문자열의 길이 차이가 p의 개수
        int ps = s.length() - s.replace("p", "").length();
        int ys = s.length() - s.replace("y", "").length();

        return ps == ys;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input = "pPoooyY";
        boolean result = answer.solution(input);

        System.out.print(result);
    }
}

/*
int ps = 0;
int ys = 0;

for (char c : s.toCharArray()) {
    switch (c) {
        case 'p', 'P' -> ps++;
        case 'y', 'Y' -> ys++;
    }
}
return ps == ys;
 */

