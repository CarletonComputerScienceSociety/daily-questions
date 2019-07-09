function maxRun(arr){
	let set = new Array(Math.max(...arr)).fill(0);
	for(let entry in arr){ set[arr[entry]] = 1; }
	let count = 0; let max = 0; let counting = true;
	for(let entry in set){
		if(set[entry]){
			if(set[parseInt(entry)+1]){ if(!counting) counting = true; count++; }
			else{ counting = false; count = 0; }
			if(count>max) max=count;
		}
	}
	return max+1
}