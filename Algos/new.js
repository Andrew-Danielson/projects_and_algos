const str = 'racecar';
let i = 0;
let j = 0;
let found = true;
function palindrome(str){
    for(i = 0, j = str.length; i < str.length/2; i++, j--){
        if(str[i] != str[j]){
            found = false;
        }
    }
    if(found = true){
        console.log(str + ' is a palindrome');
    }
    else {
        console.log(str + ' is not a palindrome')
    }
}

console.log(palindrome(str));



class="table table-borderless"
class="overflow-auto border-2 border-dark"
class=" d-flex justify-content-between"
user_id = %(user_id)s AND chore_id = %(chore_id)s