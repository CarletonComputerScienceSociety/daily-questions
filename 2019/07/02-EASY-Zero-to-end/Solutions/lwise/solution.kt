fun IntArray.moveZeroesToEnd(): IntArray {
	return this.filter { it != 0 }.plus(this.filter { it == 0 }).toIntArray()
}