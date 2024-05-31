### geo 
#### 添加 key为kk:location的geo数据
geoadd kk:location 120.346111 31.556381 kk1 120.375821 31.560368 kk2
#### 列出某个key的全部点位 
geopos kk:location 
#### 计算2个点位之间的距离,单位km （也可以指定米：m）
geodist kk:location kk1 kk2 km
#### 以某个点位为圆心，5KM距离为半径查找
georadius kk:location 120.346112 31.556382 5km