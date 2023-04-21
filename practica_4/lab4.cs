using System;
using System.IO;
using System.Text;

using Newtonsoft.Json;
using System.Diagnostics;

namespace lab4
{
    class Program
    {
        static void Main(string[] args)
        {
            mx mx = getFile();
            float m = mx.m1.GetLength(0);
            float n = mx.m2.GetLength(0);
            float k = mx.m2.GetLength(1);
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            for (int c = 0; c < mx.repeat; c++)
            {
                for (int u = 0; u < m; u++)
                {
                    for (int o = 0; o < k; o++)
                    {
                        for (int p = 0; p < n; p++)
                        {
                            _ = mx.m1[u, p] * mx.m2[p, o];
                        }
                    }
                }
            }

            stopwatch.Stop();
            TimeSpan interval = TimeSpan.FromMilliseconds(stopwatch.ElapsedMilliseconds);
            Console.WriteLine(interval.Seconds + "." + interval.Milliseconds);
            setFile(interval);
        }
        static public mx getFile()
        {
            mx mx = new mx();
            using (StreamReader fs = new StreamReader("generator.json"))
            {

                JsonSerializer serializer = new JsonSerializer();
                mx = (mx)serializer.Deserialize(fs, typeof(mx));
                return mx;
            }
        }
        static public void setFile(TimeSpan interval)
        {
            using (StreamWriter streamWriter = new StreamWriter("statsCSharp.csv", true, Encoding.GetEncoding("windows-1251")))
            {
                streamWriter.WriteLine($"{interval.Milliseconds}");
            }
        }

        [Serializable]
        public class mx
        {
            public float[,] m1 = new float[,] { };
            public float[,] m2 = new float[,] { };
            public float alpha = 1;
            public float beta = 1;
            public float repeat = 0;
        }
    }
}
