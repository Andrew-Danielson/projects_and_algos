// function reverse(arr) {
//     for (let x = 0; x < arr.length / 2; x++) {
//         let temp = arr[x];
//         arr[x] = arr[arr.length - 1 - x];
//         arr[arr.length - 1 - x] = temp;
//     }
// }

// let arr = [1,2,3,4,5,6]
// reverse(arr)
// console.log(arr)

// function rotate(arr, num) {
//     for (let x = 0; x < num; x++) {
//         let temp = arr[arr.length - 1];
//         for (let i = arr.length - 2; i >= 0; i--) {
//             arr[i + 1] = arr[i];
//         }
//         arr[0] = temp
//     }
// }

// let arr = [1,2,3,4,5,6]
// rotate(arr, 2)
// console.log(arr)

// function filter_range(arr, num1, num2) {
//     let i = 0;
//     for (let x = 0; x < arr.length; x++) {
//         if (arr[x] >= num1 && arr[x] <= num2) {
//             arr[i] = arr[x];
//             i ++;
//         }
//     }
//     arr.length = i;
// }

// let arr = [1,2,3,4,5,6]
// filter_range(arr, 2, 7)
// console.log(arr)

function concat(arr1, arr2) {
    let temp = [];
    let i = 0;
    for (let x = 0; x < arr1.length; x ++) {
        temp[i] = arr1[x];
        i ++;
    }
    for (let x = 0; x < arr2.length; x ++) {
        temp[i] = arr2[x];
        i ++;
    }
    return temp;
}

let arr1 = [1,2,3,4,5,6]
let arr2 = [1,2,3,4,5,6]
let results = concat(arr1,arr2);
console.log(results);