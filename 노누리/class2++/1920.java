import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(st.nextToken());
        int[] arr=new int[N];

        st=new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        st=new StringTokenizer(br.readLine());
        int M=Integer.parseInt(st.nextToken());

        st=new StringTokenizer(br.readLine());
        for(int i=0;i<M;i++) {
            int num=Integer.parseInt(st.nextToken());
            if(Arrays.binarySearch(arr,num)>=0) {
                sb.append("1\n");
            }else {
                sb.append("0\n");
            }
        }

        /*
        * for(int i=0;i<M;i++){
            int num=Integer.parseInt(st.nextToken());
            int left=0;
            int right=N-1;
            int mid=(left+right)/2;
            while(left<=right) {
            	mid=(left+right)/2;

            	if(num<arr[mid]) {
            		right=mid-1;
            	}else if(num>arr[mid]){
            		left=mid+1;
            	}else {
            		break;
            	}
            }
            if(arr[mid]==num) {
            	sb.append("1\n");
            }else {
            	sb.append("0\n");
            }
        }
        * */

        System.out.println(sb);
    }

}