function spiralTraversalIV(N, arr) {
    let bag = "";
    let count = 0;
    let up = 0;
    let left = 0;
    let right = N - 1;
    let down = N - 1;

    while (count < N * N) {
        for (let i = left; i <= right; i++) {
            bag += arr[up][i] + " ";
            count++;
        }
        up++;

        for (let i = up; i <= down; i++) {
            bag += arr[i][right] + " ";
            count++;
        }
        right--;

        if (up <= down) {
            for (let i = right; i >= left; i--) {
                bag += arr[down][i] + " ";
                count++;
            }
            down--;
        }

        if (left <= right) {
            for (let i = down; i >= up; i--) {
                bag += arr[i][left] + " ";
                count++;
            }
            left++;
        }
    }

    console.log(bag.trim());
};

const runProgram = (input) => {
    input = input.trim().split("\n");
    const tc = Number(input[0]);
    let line = 1;

    for (let i = 0; i < tc; i++) {
        const N = Number(input[line++]);
        const arr = [];

        for (let j = 0; j < N; j++) {
            arr.push(input[line++].trim().split(" ").map(Number));
        }

        spiralTraversalIV(N, arr);
    }
};

if (!process.env.USERNAME) {
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
