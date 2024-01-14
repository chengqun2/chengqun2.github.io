### 1. list map add a new Object:
this.list = this.list.map((item) => {
  return{
    ...item,
    sex:'gender'
  }
})
console.log('newList:',this.list);
### 2. reduce an array:
let array = [1,2,3];
let result = array.reduce(function(previousValue, currentValue)
    {
        return previousValue + currentValue
    },0)
console.log(result)       