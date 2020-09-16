<template>
  <div class="upload_file">
    <el-row :gutter="20">
    <el-col :span="8" :offset="8"><div class="grid-content bg-purple">
      <el-input
        placeholder="请输入内容"
        v-model="filenickname"
        clearable><template slot="prepend">文件命名:</template>
      </el-input>
    </div></el-col>
    </el-row>

    <el-row :gutter="20">
    <el-col :span="8" :offset="8"><div class="grid-content bg-purple">
      <input type="file" id="myfile">
      <el-button type="primary submit" @click.prevent="upload" style="float: right; height: auto">上传</el-button>
    </div></el-col>
    </el-row>

    <el-row :gutter="20">
    <el-col :span="8" :offset="8"><div class="grid-content ">
      <el-progress type="line" :percentage="percentage" class="progress" :show-text="true"></el-progress>
    </div></el-col>
    </el-row>

    <el-dialog
      title="提示"
      :visible="dialogVisible"
      width="30%"
      :modal-append-to-body='false'
    >
      <span>文件上传成功</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="ensure">确 定</el-button>
      </span>
    </el-dialog>
<!--    <button type="submit" @click.prevent="upload">上传</button>-->
  </div>
</template>

<script>
export default {
  name: 'FileUpload',
  data () {
    return {
      filenickname: '新建文件',
      percentage: 0,
      dialogVisible: false
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
        url: 'http://172.20.3.107:8000/files/',
        method: 'post',
        data: form_data,
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        onUploadProgress: (progressEvent) => {
          let complete = (progressEvent.loaded / progressEvent.total).toFixed(2) * 100
          this.percentage = complete
          if (complete >= 100) {
            this.percentage = 0
            this.dialogVisible = true
          }
        }
      }).then(res => {
        console.log(res)
      })
    },
    ensure () {
      this.dialogVisible = false
    }
  }
}
</script>

<style>
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 40px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  input#myfile {
    float: left;
    font-size: 25px;
  }

</style>
