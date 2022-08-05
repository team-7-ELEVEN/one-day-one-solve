package study;

// 체스판 포기
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class B_1018 {

	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		String[] arr = in.readLine().split(" ");
		int M = Integer.parseInt(arr[0]);
		int N = Integer.parseInt(arr[1]);
		
		String[][] arr2 = new String[N][M];
		
		for(int i = 0 ; i <	M;i++) {
			arr2[i] = in.readLine().split("");
		}
		
		List<Integer> result = new ArrayList<>();
		
		for(int i =0; i < (N-7); i++) {
			for(int j = 0; j< (M-7) ; j++) {
				int b_err = 0;
				int w_err = 0;
				for(int y = 0; y < 8; y++) {
					for(int x = 0; x < 8 ;x++) {
						
						if((x+y)%2==0) {
							//시작이 b 일때
							if(arr2[y][x].equals("W")) {
								b_err++;
							}
							// 시작이 w 일때
							else {
								w_err++;
							}
							
						}
						else {
							if(arr2[y][x].equals("B")) {
								b_err++;
							}
							else {
								w_err++;
							}
						}
						
						
						
					}
				}
				result.add(Math.min(b_err,w_err));
			}
		}
		System.out.println(Collections.min(result));

	}

}
