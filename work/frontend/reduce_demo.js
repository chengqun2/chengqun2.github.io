let array = [1,2,3];
let result = array.reduce(function(previousValue, currentValue)
    {
        return previousValue + currentValue
    },0)
console.log(result)    