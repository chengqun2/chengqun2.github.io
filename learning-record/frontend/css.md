### display:flex
```
//垂直+水平居中
display: grid;
place-items: center;

//垂直居中
display: flex;
align-items: center; 
//水平居中
justify-content: center;  
```

### gap 定义元素之间的间距
```
//定义元素之间的间距
display: flex;
gap: 10px;
```

### 使用flex布局，让元素占满剩余空间
```
display: flex;
flex: 1;
```

### align-self 
align-self 交叉轴上的对齐方式
```
.flex-container {
    display: flex;
}

.flex-container .item-left {
    align-self: flex-start;
}

.flex-container .item-right {
    align-self: flex-end;
}
```