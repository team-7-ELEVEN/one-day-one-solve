import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int r,c;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int N=Integer.parseInt(st.nextToken());
        r=Integer.parseInt(st.nextToken());
        c=Integer.parseInt(st.nextToken());

        int cnt=0;
        int idx_r=(int)Math.pow(2, N)/2-1;
        int idx_c=(int)Math.pow(2, N)/2-1;
        int size=(int)Math.pow(2,N);

        while(size>=1) {
            if(r<=idx_r && c>idx_c) {
                cnt+=(size/2*size/2);
                idx_r-=size/4;
                idx_c+=size/4;
            }else if(r>idx_r && c<=idx_c) {
                cnt+=(size/2*size/2)*2;
                idx_r+=size/4;
                idx_c-=size/4;
            }else if(r>idx_r && c>idx_c) {
                cnt+=(size/2*size/2)*3;
                idx_r+=size/4;
                idx_c+=size/4;
            }else if(r<=idx_r && c<=idx_c){
                idx_r-=size/4;
                idx_c-=size/4;
            }

            size=size/2;
        }

        System.out.println(cnt);
    }

}

