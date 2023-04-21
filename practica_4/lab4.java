package lab4;
import java.io.*;
import java.nio.file.StandardOpenOption;

import com.opencsv.CSVWriter;
import com.google.gson.Gson;


public class Main {
    public static void main(String[] args) {
        mx mx = getFile();

        float m = mx.m1.length;
        float n = mx.m2.length;
        float k = mx.m2[1].length;

        long time = System.currentTimeMillis();
        for (int c = 0; c < mx.repeat; c++)
        {
            for(int u = 0; u < m; u++)
            {
                for(int o = 0; o < k; o++)
                {
                    for(int p = 0; p < n; p++)
                    {
                        float v = mx.m1[u][p] * mx.m2[p][o];
                    }
                }
            }
        }
        var elapsedTime = System.currentTimeMillis() - time;

        String[] str =new String[] {Float.toString(elapsedTime)};

        try (CSVWriter writer = new CSVWriter(new FileWriter("src/lab4/statsJava.csv",true))) {
            writer.writeNext(str);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    public static mx getFile(){
        Gson gson = new Gson();
        BufferedReader br = null;
        mx mx;
        try {
            br = new BufferedReader(new FileReader("src/lab4/generator.json"));
            mx = gson.fromJson(br, mx.class);

        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        return mx;
    }

}
