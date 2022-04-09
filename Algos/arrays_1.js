// function pushFront(arr, val) {
//     for (let x = arr.length - 1; x >= 0; x--) {
//         arr[x+1] = arr[x];
//     }
//     arr[0] = val;
// }
// let arr = [3, 5, 7, 9, 1];
// pushFront(arr, 2);
// console.log(arr)


// function popFront(arr) {
//     let num = arr[0];
//     for (let x = 1; x < arr.length; x++) {
//         arr[x-1] = arr[x];
//     }
//     arr.pop();
//     return num;
// }
// let arr = [3, 5, 7, 9, 1];
// let results = popFront(arr);
// console.log(results);
// console.log(arr);

function insert(arr, ind, val) {
    for (let x = arr.length - 1; x >= ind; x--) {
        // if (x == ind) {
        //     arr[x] = val;
        // }
        // else {
        // }
        arr[x+1] = arr[x];
    }
    arr[ind] = val;
}
let arr = [3, 5, 7, 9, 1];
insert(arr, 5, 8);
console.log(arr);

