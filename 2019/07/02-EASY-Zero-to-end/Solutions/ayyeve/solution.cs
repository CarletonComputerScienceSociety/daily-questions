public static int[] sortZeros(int[] array) {
    int counter = 0;
    int max = Array.FindAll(array, x => x==0).Length;
    for (int i = 0; i < array.Length; i++) {
        while (array[i] == 0 && counter < max) {
            array = shiftToEnd(array, i);
            counter ++;
        }
        counter = 0;
    }
    return array;
}
private static int[] shiftToEnd(int[] array, int index) {
    int numAtIndex = array[index];
    for (int i = index; i < array.Length - 1; i++) {
        array[i] = array[i+1];
    }
    array[array.Length - 1] = numAtIndex;
    return array;
}
