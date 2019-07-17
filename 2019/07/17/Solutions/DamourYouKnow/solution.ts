function levelOrderTraversal(arr: (number | null)[]): number[][] {
    const levels: number[][] = [];

    let level = [buildTree(arr)];
    while(level.length > 0) {
        levels.push(level.map((n) => n.value));
        level = level.map((n) => n.children()).reduce((a, c) => [...a, ...c]);
    }

    return levels;
}


function buildTree(arr: (number | null)[]): TreeNode {
    const left = (i: number): number => (2*i)+1;
    const right = (i: number): number => 2*(i+1);
    const nodes = arr.map((n) => n ? new TreeNode(n) : null );
    for (let i = 0; right(i) < nodes.length; i++) {
        nodes[i].left = nodes[left(i)];
        nodes[i].right = nodes[right(i)];
    }
    return nodes[0];
}


class TreeNode {
    value: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(value: number) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    children(): TreeNode[] {
        return [this.left, this.right].filter((child) => child !== null);
    }
}


console.log(levelOrderTraversal([3,9,20,null,null,15,7]));