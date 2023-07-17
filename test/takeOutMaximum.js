function runProgram(input) {
    let input = input.trim().split("\n");
    let out = input[0].trim().split(" ");
    let n = Number(out[0]);
    let k = Number(out[1]);
    let arr = input[1].trim().split(" ").map(Number);
    maxSum(arr, n, k);
}
function maxSum(arr, n, k) {
    let sum = 0;
    for (let i = 0; i < k; i++) {
        sum += arr[i];
    }
    let maxSum = sum;
    for (let i = k; i < n; i++) {
        sum += arr[i] - arr[i - k];
        maxSum = Math.max(maxSum, sum);
    }
    console.log(maxSum);
}
if (process.env.USERNAME === "") {
    runProgram(``);
} else {
    process.stdin.resume();
    process.stdin.setEncoding("ascii");
    let read = "";
    process.stdin.on("data", function (input) {
        read += input;
    });
    process.stdin.on("end", function () {
        read = read.replace(/\n$/, "");
        read = read.replace(/\n$/, "");
        runProgram(read);
    });
    process.on("SIGINT", function () {
        read = read.replace(/\n$/, "");
        runProgram(read);
        process.exit(0);
    });
}