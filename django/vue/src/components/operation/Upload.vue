<template>
<div class="upload_button">
    <input type="file" id="up" @change="FileUpload">
    <lable for="up"></lable>
</div>
</template>

<script>
export default{
    data:{
        refs: [
            'http://127.0.0.1:8000/upload'
        ]
    },
    methods:{
        FileUpload(e){
            this.file = e.target.files[0];
            this.errText = '';
            this.$emit('input', this.file);
            let formData = new FormData();
            formData.append("attachment", this.file[0]);
            this.$http.post(this.refs[0], formData,{
                headers:{
                    'Content-Type': 'multipart/form-data'
                }
            }).then(function(res){})
        }
    }
}
</script>

<style scoped>
.upload_button{
    position: relative;
}

input{
    position: absolute;
}

label{
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 10;
}
</style>