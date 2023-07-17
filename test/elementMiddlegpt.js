function runProgram(input) {
    input = input.trim().split("\n");
    const len = Number(input[0]);
    const arr = input[1].trim().split(" ").map(Number);

    const leftMax = [];
    leftMax[0] = arr[0];
    for (let i = 1; i < len; i++) {
        leftMax[i] = Math.max(leftMax[i - 1], arr[i]);
    }

    const rightMin = [];
    rightMin[len - 1] = arr[len - 1];
    for (let i = len - 2; i >= 0; i--) {
        rightMin[i] = Math.min(rightMin[i + 1], arr[i]);
    }

    let position = -1;
    for (let i = 1; i < len - 1; i++) {
        if (leftMax[i - 1] < rightMin[i + 1]) {
            position = i;
            break;
        }
    }

    if (position === -1) {
        console.log(-1);
    } else {
        console.log(arr[position + 1]);
    }
}
