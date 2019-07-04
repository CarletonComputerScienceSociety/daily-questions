kernels = [
[-1, 0],
[0, 1],
[1, 0],
[0, -1]]

function wordSearch(matrix, word){

	for(let i in matrix) for(let j in matrix[i]) if(matrix[i][j] == word[0]) if(dfs(matrix, word, 0, [parseInt(j), parseInt(i)])) return true
	return false

}

function dfs(matrix, word, index, point){

	let x = point[0]
	let y = point[1]

	for (let k in kernels){
		xMod = x+kernels[k][0]
		yMod = y+kernels[k][1]
		if(matrix[xMod] == undefined || matrix[xMod][yMod] == undefined) continue
		if(index+1 < word.length){ if(word[index+1] == matrix[xMod][yMod]) return dfs(matrix, word, index+1, [xMod, yMod]) }
		else return true

	}

	return false

}