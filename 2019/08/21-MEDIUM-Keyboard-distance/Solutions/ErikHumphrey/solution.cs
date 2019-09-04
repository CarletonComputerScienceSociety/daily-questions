using System;

namespace daily
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(KeyDistance(char.Parse(args[0].ToUpper()), char.Parse(args[1].ToUpper())));
        }

        static int KeyDistance(char key1, char key2)
        {
            char[][] keyMap = new char[3][];

            keyMap[0] = new char[] { 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P' };
            keyMap[1] = new char[] { 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L' };
            keyMap[2] = new char[] { 'Z', 'X', 'C', 'V', 'B', 'N', 'M' };

            Tuple<int, int> keyPos1 = null, keyPos2 = null;

            for (int i = 0; i < keyMap.Length; i++)
            {
                for (int j = 0; j < keyMap[i].Length; j++)
                {
                    if (keyMap[i][j].Equals(key1))
                    {
                        keyPos1 = Tuple.Create(j, i);
                    }

                    if (keyMap[i][j].Equals(key2))
                    {
                        keyPos2 = Tuple.Create(j, i);
                    }
                }
            }

            return (int)Math.Round(Math.Sqrt(Math.Pow(keyPos2.Item1 - keyPos1.Item1, 2) + Math.Pow(keyPos2.Item2 - keyPos1.Item2, 2)));
        }
    } 
}
