### 1. list map add a new Object:
```
this.list = this.list.map((item) => {
  return{
    ...item,
    sex:'gender'
  }
})
console.log('newList:',this.list);
```
### 2. reduce an array:
```
let array = [1,2,3];
let result = array.reduce(function(previousValue, currentValue)
    {
        return previousValue + currentValue
    },0)
console.log(result)      
``` 
### Difference between .on('click') vs .click()
```
If you call `.on()` without a selector parameter there is no performance improvement over using `.click()`
$("button.alert").click(function() {
    alert(1);
});
$("div#container").on('click', 'button.alert', function() {
    alert(1);
});
$("#element").off("click.someNamespace");
I would prefer `.on` over `.click` because the former can use less memory and work for dynamically added elements.
And Can use `.off` to remove the event.
```
### push() vs Array. unshift() 
```
the push() method adds elements to the end of an array, and unshift() adds elements to the beginning
```

### setInterval
```
A function to be executed every delay milliseconds. The first execution happens after delay milliseconds.
setInterval(fn(),1000)  加括号立即执行一次
setInterval(fn,1000) 不加括号，1秒后开始执行
```

### console
`console {debug: ƒ, error: ƒ, info: ƒ, log: ƒ, warn: ƒ, …}`

### splice vs slice
```
Use splice() when you need to modify the original array.
Use slice() when you want to extract part of an array without altering the original.
```

### btoa(string) 对字符串进行base64编码
```
const originalString = 'Hello world';
const encoded = btoa(originalString);
console.log(encoded); // 输出: SGVsbG8gd29ybGQ=
```

### atob(encodedBase64String) 对base64字符串进行解码
```
// 一个经过 Base64 编码的字符串
const encoded = 'SGVsbG8gd29ybGQ=';
// 使用 atob() 函数进行解码
const decoded = atob(encoded);
console.log(decoded); // 输出: Hello world
```






