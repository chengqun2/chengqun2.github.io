<template>
    <view class="container">
        <view class="location-info">
            <text>Latitude: {{latitude}}</text>
            <text>Longitude: {{longitude}}</text>
            <text>Address: {{address}}</text>
        </view>
        
        <button @click="getLocation" type="primary">Get Current Location</button>
    </view>
</template>

<script>
export default {
    data() {
        return {
            latitude: '',
            longitude: '',
            address: ''
        }
    },
    methods: {
        getLocation() {
            // Request location permission
            uni.getLocation({
                type: 'gcj02', // gcj02 coordinate system for China, use 'wgs84' for other regions
                success: (res) => {
                    this.latitude = res.latitude
                    this.longitude = res.longitude
                    
                    // Reverse geocoding to get address
                    uni.chooseLocation({
                        latitude: res.latitude,
                        longitude: res.longitude,
                        success: (res) => {
                            this.address = res.address
                        },
                        fail: (err) => {
                            uni.showToast({
                                title: 'Failed to get address',
                                icon: 'none'
                            })
                        }
                    })
                },
                fail: (err) => {
                    uni.showToast({
                        title: 'Failed to get location',
                        icon: 'none'
                    })
                }
            })
        }
    }
}
</script>

<style>
.container {
    padding: 20px;
}

.location-info {
    margin-bottom: 20px;
}

.location-info text {
    display: block;
    margin-bottom: 10px;
}
</style>