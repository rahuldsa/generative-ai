let Print = (matx, N) => {
    let bag = "",
        c = 0;
    let up = 0;
    let left = 0;
    let right = N - 1;
    let d = N - 1;

    while (c < N * N) {
        for (let i = d; i >= up; i--) {
            bag += matx[i][right] + " ";
            c++;
        }
        right--;
        for (let i = right; i >= left; i--) {
            bag += matx[up][i] + " ";
            c++;
        }
        up++;
        for (let i = up; i <= d; i++) {
            bag += matx[i][left] + " ";
            c++;
        }
        left++;
        for (let i = left; i <= right; i++) {
            bag += matx[d][i] + " ";
            c++;
        }
        d--;
    }
    console.log(bag);
};

let runProgram = (input) => {
    input = input.trim().split("\n");
    let tc = input[0];
    let line = 1;
    for (let i = 0; i < tc; i++) {
        let N = input[line].trim(),
            matx = [];
        line++;
        for (let i = 0; i < N; i++) {
            matx.push(input[line].trim().split(" ").map(Number));
            line++;
        }

        Print(matx, N);
    }
};

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