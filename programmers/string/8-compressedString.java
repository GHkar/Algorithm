import java.util.ArrayList;
import java.util.List;

// 문자열 압축
public class Solution {
    // 문자열 압축 후 압축된 문자열의 길이 반환
    private int compress(String source, int length){
        StringBuilder builder = new StringBuilder();
        String last = "";
        int count = 0;

        for (String token : split(source, length)){
            // 직전에 등장한 문자열과 현재 문자열이 같다면 카운트 증가
            if (token.equals(last)) {
                count++;
            } else {
                // 새로운 토큰 등장
                if (count > 1) builder.append(count);
                builder.append(last);
                last = token;
                count = 1;
            }
        }
        if (count > 1) builder.append(count);
        builder.append(last);

        return builder.length();
    }

    // 설정된 길이만큼 문자열을 잘라 낸 token의 배열 생성
    private List<String> split(String source, int length){
        List<String> tokens = new ArrayList<>();

        // source를 startIndex부터 endIndex까지 잘라 tokens 리스트에 추가
        for (int startIndex = 0; startIndex < source.length(); startIndex += length){
            int endIndex = startIndex + length;
            if (endIndex > source.length()) endIndex = source.length();
            tokens.add(source.substring(startIndex,endIndex));
        }
        return tokens;
    }
  
    public int solution(String s){
        // 1부터 입력 문자열 s의 길이만큼 자를 문자열의 길이를 설정하며 반복
        int min  = Integer.MAX_VALUE;
        for (int length = 1; length <= s.length(); length++){
            // 문자열 압축 후 가장 짧은 길이 선택
            int compressed = compress(s, length);
            if (compressed < min){
                min = compressed;
            }
        }
        return min;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input = "aabbaccc";
        int result = answer.solution(input);

        System.out.print(result);
    }
}

