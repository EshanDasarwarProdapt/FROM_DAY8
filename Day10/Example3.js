let marks = [85, 42, 76, 91, 38, 67, 55, 29, 80, 49];


let pass = 0;
let fail = 0;

let max = marks[0];
let min = marks[0];

for (let i = 0; i < marks.length; i++) {

    if (marks[i] >= 50) {
        console.log("Student " + (i + 1) + " - " + marks[i] + "- Pass");
        pass++;
    } else {
        console.log("Student " + (i + 1) + " - " + marks[i] + "- Fail");
        fail++;
    }

    if (marks[i] > max) {
        max = marks[i];
    }

    if (marks[i] < min) {
        min = marks[i];
    }
}

console.log("-------------------");
console.log("Maximum Marks:", max);
console.log("Minimum Marks:", min);
console.log("Total Pass:", pass);
console.log("Total Fail:", fail);