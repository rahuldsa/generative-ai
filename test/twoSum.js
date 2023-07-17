function twosum(n, m, arr) {
    let left = 0;
    let right = n - 1;
    while (left < right) {
        let sum = arr[left] + arr[right];
        if (sum === m) {
            console.log(left, right);
            return;
        } else if (sum > m) {
            right--;
        } else {
            left++;
        }
    }
    console.log(-1, -1);
}
function runProgram(input) {
    input = input.trim().split("\n");
    let tc = Number(input[0]);
    let k = 1;
    for (let i = 0; i < tc; i++) {
        let [n, m] = input[k++].trim().split(" ").map(Number);
        let arr = input[k++].trim().split(" ").map(Number);
        twosum(n, m, arr);
    }
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