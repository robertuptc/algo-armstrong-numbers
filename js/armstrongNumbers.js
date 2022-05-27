// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(arr) {
  let answer = []
  
  for (let i = 0; i < arr.length; i++) {
    let newNum = arr[i].toString().split('').map((elem, _, arr) => elem ** arr.length).reduce((a,b) => a + b)
    if (newNum === arr[i]) {
      answer.push(newNum)
    }  
  } return answer
};




