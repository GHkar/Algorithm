import java.util.Arrays;

// 행렬의 곱셈
public class Solution {
  
    public int[][] solution(int[][] arr1, int[][] arr2){
        int[][] arr = new int[arr1.length][arr2[0].length];
        // 행렬 곱셈
        for (int i = 0; i < arr.length; i++){
            for(int j = 0; j < arr[i].length; j++){
                // arr[i][j]의 값 구하기
                arr[i][j] = 0;
                for (int k = 0; k < arr1[i].length; k++){
                    arr[i][j] += arr1[i][k] * arr2[k][j];
                }
            }
        }
        return arr;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int[][] input1 =  {{1, 4}, {3, 2}, {4, 1}};
        int[][] input2 =  {{3, 3}, {3, 3}};
        int[][] result = answer.solution(input1, input2);

        System.out.print(Arrays.deepToString(result));
    }
}

