<template>
  <div class="upload_file">
    文件昵称
    <el-input
      placeholder="请输入内容"
      v-model="filenickname"
      clearable>
    </el-input>
    文件<input type="file" id="myfile"><br>
    <button type="submit" @click.prevent="upload">上传</button>
  </div>
</template>

<script>
export default {
  name: 'FileUpload',
  data () {
    return {
      filenickname: '新建文件'
    }
  },
  methods: {
    upload () {
      // eslint-disable-next-line camelcase
      let form_data = new FormData()
      const myfile = document.getElementById('myfile').files[0]
      form_data.append('name', this.filenickname)
      form_data.append('file_path', myfile, myfile.name)
      this.$axios({
        url: 'http://127.0.0.1:8000/files/',
        method: 'post',
        data: form_data,
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(res => {
        console.log(res)
      })
    }
  }
}
</script>

<style scoped>

</style>
